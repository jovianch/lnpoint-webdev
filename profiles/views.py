import os
import datetime

from django.contrib import messages
from .forms import EditProfileForm, EditUserForm
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from .models import Profile
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db import IntegrityError

from kelas.models import OpenClass
from activity.models import Activity
from accounts.models import User

def unfollow(request, username):
    user = request.user
    if user.is_authenticated:
        user_followed = User.objects.get(username=username)
        user.unfollow(user_followed)
        # messages.info(request, 'You unfollow {}'.format(username))
        return redirect(reverse_lazy('profiles:profiles', kwargs={'username':username}))
    else:
        return redirect(reverse('accounts:login'))

def follow(request, username):
    try:
        user = request.user
        if user.is_authenticated:
            user_followed = User.objects.get(username=username)
            user.follow(user_followed)
            # messages.success(request, 'You followed {}'.format(username))
            return redirect(reverse_lazy('profiles:profiles', kwargs={'username':username}))
        else:
            return redirect(reverse('accounts:login'))
    except IntegrityError:
        messages.error(request, 'Refresh to continue.')
        return redirect(reverse('profiles:profiles', kwargs={'username':username}))

#Activity list Pre for stories
class StoryProfileView(generic.DetailView):
    template_name = "profiles/story_profile.html"

    def get_object(self):
        username = self.kwargs.get('username')
        return Profile.objects.get(pk=username) 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        openclass_list_all = self.get_object().open_classes.all()
        activity_list_all = self.get_object().activities.all()
        activity_pre = []

        now = datetime.datetime.now()

        for activity in activity_list_all:
            if activity.status != 'POSTED':
                if((now.date() < activity.date_held) or (
                    now.date() == activity.date_held and
                    now.time() <= activity.time)):
                
                    activity_pre.append(activity)



        context['openclass_list'] = openclass_list_all
        context['activity_list'] = activity_pre
        context['partner'] = self.get_object()
        
        return context



class ProfileView(generic.DetailView):
    #model = Profile
    template_name = "profiles/user_profile.html"

    def get_object(self):
        username = self.kwargs.get('username')
        return User.objects.get(username=username).profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        activity_list = []

        for activity in self.get_object().activities.all():
            if activity.status == 'POSTED':
                if (activity.status == 'POSTED'):
                    # user who request in activity liked by list
                    for like in activity.liked_by.all():
                        if like.user.profile == self.get_object():
                            activity.is_liked = True
                activity_list.append(activity)

        user_object = User.objects.get(username=self.kwargs.get('username'))
        if user_object.followers.filter(pk=self.request.user.pk).exists():
            context['user_followed'] = True

        context['openclass_list'] = self.get_object().open_classes.all()
        context['activity_list'] = activity_list

        return context


@login_required(login_url='/accounts/login/')
def EditProfileView(request, username):

    user = request.user

    profile_data = Profile.objects.get(user=user)
    user_data = User.objects.get(username=user.username)

    profile_instance = {
            'avatar': profile_data.avatar,
            'bio': profile_data.bio,
    }

    user_instance = {
            'fullname': user_data.fullname,
    #        'username': user_data.username,
            'card_id': user_data.card_id,
            'phone_number': user_data.phone_number,
            'contact': user_data.contact,
            'institution': user_data.institution,
    }


    if request.method == 'POST':
        profile_form = EditProfileForm(request.POST, request.FILES, instance=profile_data)
        user_form = EditUserForm(request.POST, instance=user_data)

        forms = [profile_form, user_form]

        if all([f.is_valid() for f in forms]):
            profile = profile_form.save(commit=False)
            user = user_form.save(commit=False)

            if len(request.FILES) != 0:
                profile.avatar.name = profile.user.username + ".png"
                file_path = settings.MEDIA_ROOT + "\\profiles\\"+ profile.user.username+".png"
                if os.path.exists(file_path):
                    os.remove(file_path)

            user.save()
            profile.save()

            messages.success(request, 'You have updated your profile.')
            return redirect(reverse('profiles:profiles', kwargs={'username': user.username}))

    profile_form = EditProfileForm(initial=profile_instance)
    user_form = EditUserForm(initial=user_instance)

    context = {
        'user_form': user_form,
        'profile_form' : profile_form,
        'profile': profile_data,
        'user': user_data,
    }

    return render(request, 'profiles/edit_profile.html', context)


