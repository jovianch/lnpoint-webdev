from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, UpdateView
from django.forms.formsets import formset_factory
from django.db import IntegrityError, transaction
from django.contrib import messages
from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


import datetime

from .models import Tag, Activity, Like
from .forms import ActivityForm, ActivityDoneForm

from kelas.forms import TagForm, BaseTagFormSet


@login_required(login_url='/accounts/login/')
def ActivityPlanView(request):

    user = request.user

    if not user.is_verified:
        messages.info(request, 'You have to verify to plan activity')
        return redirect(reverse_lazy('accounts:verify', kwargs={'username':user.username}))

    TagFormSet = formset_factory(TagForm, formset=BaseTagFormSet)

    activity_form = ActivityForm()

    if request.method == 'POST':
        tag_formset = TagFormSet(request.POST, prefix="tag")
        activity_form = ActivityForm(request.POST)

        forms = [tag_formset, activity_form]

        if all([f.is_valid() for f in forms]):
            activity = activity_form.save(commit=False)
            activity.partner = user.profile

            activity_tags = []

            for tag_form in tag_formset:
                tag = tag_form.cleaned_data.get('tag')
                try:
                    old_tag = Tag.objects.get(name=tag)
                    activity_tags.append(old_tag)
                except Tag.DoesNotExist:
                    if tag:
                        new_tag = Tag(name=tag)
                        new_tag.save()
                        activity_tags.append(new_tag)
                        #bagaimana cara tag dengan name tersebut sudah ada tanpa looping ke database

            try:
                with transaction.atomic():
                    activity.save()
                    activity.tags.add(*activity_tags)
                    messages.success(request, 'Your activity added to Activities nearby')
                    return redirect(reverse('Home'))

            except IntegrityError:
                messages.error(request, 'There is something wrong.')
                return redirect(reverse('profiles:profiles', kwargs={'username': user.username}))


    tag_formset = TagFormSet(prefix="tag")

    context = {
        'activity_form' : activity_form,
        'tag_formset' : tag_formset,
        'profile': user.profile,
    }

    return render(request, 'activity/activity_plan.html', context)


@login_required(login_url='/accounts/login/')
def ActivityDeleteView(request, pk):
    partner = request.user.profile
    activity = Activity.objects.get(pk=pk)
    if activity.partner == partner:
        activity.delete()
        messages.success(request, 'You deleted an activity')
    else:
        messages.error(request, 'You cant delete others activity!')
    return redirect(reverse('Home'))

@login_required(login_url='/accounts/login/')
def ActivityJoinView(request, pk):
    try:
        user = request.user
        if user.is_authenticated:
            activity_requested = Activity.objects.get(pk=pk)
            if activity_requested.partner.user != user:
                activity_requested.join_activity(user)
                messages.success(request, 'You join {} activity.'.format(activity_requested.partner))
                #return redirect(reverse_lazy('profiles:profiles', kwargs={'username':user.username}))
                return redirect(reverse('Home'))
        else:
            return redirect(reverse('accounts:login'))
    except IntegrityError:
        messages.error(request, 'Refresh to continue.')
        return redirect(reverse('profiles:profiles', kwargs={'username':user.username}))

@login_required(login_url='/accounts/login/')
def ActivityUnJoinView(request,pk):
    user = request.user
    activity_requested = Activity.objects.get(pk=pk)
    if activity_requested.partner.user != user:
        activity_requested.unjoin_activity(user)
        messages.info(request, 'You leave {} activity'.format(activity_requested.partner))
        return redirect(reverse('Home'))


@login_required(login_url='/accounts/login/')
def ActivityLike(request,pk):
    try:
        user = request.user
        if user.is_authenticated:
            activity_liked = Activity.objects.get(pk=pk)
            activity_liked.like_activity(user)
            # messages.success(request, 'You like this activity.')
            return redirect(reverse_lazy('profiles:profiles', kwargs={'username':user.username}))
            return redirect(reverse('activity:detail', kwargs={'pk':pk}))
        else:
            return redirect(reverse('accounts:login'))
    except IntegrityError:
        messages.error(request, 'Refresh to continue.')
        return redirect(reverse('profiles:profiles', kwargs={'username':user.username}))

@login_required(login_url='/accounts/login/')
def ActivityUnlike(request,pk):
    user = request.user
    activity_liked = Activity.objects.get(pk=pk)
    activity_liked.unlike_activity(user)
    # messages.info(request, 'You unlike this activity')
    return redirect(reverse('activity:detail', kwargs={'pk':pk}))

"""
@login_required(login_url='/accounts/login/')
def ActivityEditView(request):
    user = request.user

    TagFormSet = formset_factory(TagForm, formset=BaseTagFormSet)
    
    activity_form = ActivityForm()
"""
class ActivityDoneView(UpdateView):
    template_name = 'activity/activity_done.html'
    form_class = ActivityDoneForm

    def get_object(self):
        obj = Activity.objects.get(pk=self.kwargs['pk'])
        return obj

    def get(self, request, *args, **kwargs):
        get = super().get(request, *args, **kwargs)
        now = datetime.datetime.now()

        if self.get_object().partner != self.request.user.profile:
            messages.error(self.request, 'You cant post someone else Activity!')
            return redirect(reverse('Home'))

        if (self.get_object().date_held >= now.date() and 
            self.get_object().time >= now.time()):
            messages.error(self.request, 'You cant post activity thats not yet held')
            return redirect(reverse('Home'))
        
        return get

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activity'] = self.get_object()
        return context

    def get_success_url(self, **kwargs):
        obj = self.get_object()
        obj.status = 'POSTED'
        obj.save()
        messages.success(self.request, 'You post an Activity!')
        return reverse_lazy('Home')

class ActivityDetailView(DetailView,LoginRequiredMixin):
    template_name = "activity/activity_view.html"
    model = Activity

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        activity = self.model.objects.get(pk=self.kwargs['pk'])
        user_who_liked = []
        
        if activity.status != 'POSTED':
            messages.info(request, 'this activity not yet posted')
            return redirect(render('Home'))

        for like in activity.liked_by.all():
            user_who_liked.append(like.user)

        context['user_who_liked'] = user_who_liked    
        context['activity'] = activity
        return context





