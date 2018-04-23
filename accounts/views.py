from django.template.context_processors import request
from django.views.generic import CreateView , RedirectView, FormView, UpdateView, View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth import login, logout as auth_logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect

from django.conf import settings

from . import forms
from .models import User

#CBV

class SignUpView(CreateView, SuccessMessageMixin):
    form_class = forms.SignUpForm
    template_name = "accounts/signup.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('profiles:profiles',kwargs={'username':request.user.username}))
        else:
            return super().get(request,*args,**kwargs)

    def form_valid(self, form):
        global user_signup
        user_signup = form.save()
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        login(self.request, user_signup)
        messages.success(self.request, 'Akun kamu berhasil terdaftar')
        return reverse_lazy('welcome_addavatar')



class LoginView(FormView):
    form_class = forms.LoginForm
    template_name = "accounts/login.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('profiles:profiles',kwargs={'username':request.user.username}))
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

class SignoutView(View):
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return HttpResponseRedirect(reverse_lazy('accounts:login'))

class VerifyView(LoginRequiredMixin, UpdateView):
    template_name = "accounts/account_verify.html"
    form_class = forms.VerifyForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_login_url(self):
        return reverse('accounts:login')

    def get_success_url(self, **kwargs):
        return reverse_lazy('accounts:verify_done')

class VerifyDone(TemplateView):
    template_name = "accounts/verify_successful.html"



#FBV
@login_required
def PasswordChangeView(request):
    """Ganti Password"""
    user = request.user
    if request.method == 'POST':
        form = forms.ChangePasswordForm(request.POST, user=user)

        if form.is_valid():
            new_password = make_password(form.cleaned_data['new_password'])
            user.password = new_password
            user.save()

            messages.success(request, 'Password kamu berhasil diubah')

    else:
        form = forms.ChangePasswordForm(user=user)

    context = {
        'form': form
    }
    return render(request, 'accounts/password_change.html', context)

@login_required
def AccountCloseView(request):
    """Hapus Akun"""
    user = request.user

    if request.method == 'POST':
        form = forms.AccountCloseForm(request.POST, user=user)

        if form.is_valid():
            user.is_active = False
            user.save()
            auth_logout(request)
        return redirect(reverse('accounts:account_close_done'))

    else:
        form = forms.AccountCloseForm(user=user)

    context = {
        'form': form
    }
    return render(request, 'accounts/account_close.html', context)
# PasswordResetView Menyusul setelah email server on


