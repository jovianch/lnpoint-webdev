
import datetime
from itertools import chain

from django.views.generic import TemplateView, DetailView, FormView, UpdateView, View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate
from django.db.models import Q

from accounts.models import User
from profiles.models import Profile
from kelas.models import OpenClass
from activity.models import Activity
from accounts.forms import LoginForm

from . import forms

class Landing_Page(FormView):
    form_class = LoginForm
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('Home'))
        else:
            return super().get(request,*args,**kwargs)

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(self.request, **self.get_form_kwargs())

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        next_url = self.request.GET.get('next', None)
        if next_url:
            return "{}".format(next_url)
        else:
            return reverse_lazy('Home')

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

class About(TemplateView):
    template_name = 'about.html'

class Home(LoginRequiredMixin,DetailView):
    model = Profile
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = datetime.datetime.now()
        openclass_list = OpenClass.objects.all().order_by('-id')[:11]

        #Story Querysets
        story_partner = []
        
        #Home Querysets
        #my_openclass = []
        activity_posted = []

        for activity in self.get_queryset():
            if (activity.status == 'POSTED'):
                # user who request in activity liked by list
                for like in activity.liked_by.all():
                    if like.user.profile == self.get_object():
                        activity.is_liked = True
                activity_posted.append(activity)
            # get story query for all activity pre        
            elif (activity.partner != self.get_object() and
                activity.partner not in story_partner):
                    if((now.date() < activity.date_held) or (
                        now.date() == activity.date_held and
                        now.time() <= activity.time)):
                
                        story_partner.append(activity.partner)

        for openclass in openclass_list:
            # get story query for open class
            if (openclass.partner != self.get_object() and
                openclass.is_active and
                openclass.partner not in story_partner):

                story_partner.append(openclass.partner)
            # get my open class
            #elif (openclass.partner == self.get_object()):

            #    my_openclass.append(openclass)


        #if OpenClass.objects.filter(partner='tec_itb').exists():
        #   context['recommended_openclass'] = OpenClass.objects.get(partner='tec_itb')
        context['activity_posted'] = activity_posted
        #context['my_openclass'] = my_openclass
        context['story_partner'] = story_partner


        return context

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_queryset(self):
        #profile = Profile.objects.filter(user__followers=self.request.user)
        #qs = OpenClass.objects.filter(partner__in=profile)
        qs = Activity.objects.all().order_by('-date_held')
        return qs

    def get(self, request, *args, **kwargs):
        get = super().get(request,*args,**kwargs)
        try:
            user_activities = self.get_queryset().filter(partner=self.get_object())

            now = datetime.datetime.now()

            for activity in user_activities:
                if ((now.date() > activity.date_held or (
                    now.date() == activity.date_held and now.time() >= activity.time)) and
                    activity.status != 'POSTED'):
                    return redirect(reverse('activity:done', kwargs={'pk':activity.pk}))
                
        except Activity.DoesNotExist:
            pass
        if request.user.phone_number:
            return get
        return HttpResponseRedirect(reverse('welcome_back'))
        
class Discover(ListView):
    activity_model = Activity
    openclass_model = OpenClass
    user_model = User
    template_name = 'search_result_main.html'
    context_object_name = 'SearchResult'
    paginate_by = 10

    def get_queryset(self):
        if self.request.GET.get("q"):
            query = self.request.GET.get("q")
            openclass_list = self.openclass_model.objects.filter(Q(categories__name__icontains=query)| Q(
                                                    tags__name__icontains=query)|
                                                    Q(description__icontains=query) | Q(
                                                    location_name__icontains=query)| Q(partner__user__username__icontains=query)).distinct()

            user_list = self.user_model.objects.filter(Q(username__icontains=query) |
                                                       Q(fullname__icontains=query) |
                                                       Q(profile__bio__icontains=query)).distinct()

            activity_list = self.activity_model.objects.filter(Q(description__icontains=query)|
                                                       Q(location_name__icontains=query)|
                                                       Q(name__icontains=query)|
                                                       Q(partner__user__username__icontains=query)).distinct()
    

            object_list = list(chain(openclass_list, user_list, activity_list))
            return object_list
        else:
            openclass_list = self.openclass_model.objects.filter(is_active=True)
            activity_list = self.activity_model.objects.exclude(status='POSTED')
            object_list = list(chain(openclass_list,activity_list))
            return object_list


class WelcomeBack_temp(LoginRequiredMixin, UpdateView):
    template_name = "welcomeback_temporary.html"
    form_class = forms.TemporaryForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_login_url(self):
        return reverse('accounts:login')

    def get_success_url(self, **kwargs):
        return reverse_lazy('Home')    

class WelcomeAddAvatar(LoginRequiredMixin, UpdateView):
    template_name = 'welcome_addavatar.html'    
    form_class = forms.AddAvatarForm

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_login_url(self):
        return reverse('accounts:login')

    def get_success_url(self, **kwargs):
        return reverse('Home')

def my_custom_page_not_found_view(request):
    return render(request, '404.html', )

def test_view(request):
    if not request.user.is_superuser:
        return render(request, '404.html')
    else:
        return render(request, 'test_form.html')

def contact_us_view(request):
    form = forms.ContactUsForm()
    if request.method == 'POST':
        form = forms.ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                'Kontak dari {}'.format(form.cleaned_data['nama']),
                form.cleaned_data['question'],
                '{nama} <{email}>'.format(**form.cleaned_data),
                ['dev@lnpoint.com']
            )
            messages.add_message(request, messages.SUCCESS,
                                 'Terimakasih telah menghubungi kami!')
            return HttpResponseRedirect(reverse('contactus'))
    return render(request, 'contact_us_form.html', {'form': form})
