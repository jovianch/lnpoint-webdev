from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib import messages
from django.http import Http404
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Tag, Category, OpenClass
from .forms import TagForm, BaseTagFormSet, OpenClassForm, OpenClassEditForm
from django.forms.formsets import formset_factory
from django.db import IntegrityError, transaction
from django.contrib.auth.decorators import login_required
from accounts.models import User
from profiles.models import Profile
from .models import OpenClass
from itertools import chain


import datetime

class RequestSuccessfulView(generic.TemplateView):
    template_name = "kelas/request_successful.html"


@login_required(login_url='/accounts/login/')
def OpenClassPostView(request):

    user = request.user

    if not user.is_verified:
        messages.info(request, 'You have to be verify to share open class')
        return redirect(reverse_lazy('accounts:verify', kwargs={'username':user.username}))



    openclass_form = OpenClassForm()

    if request.method == 'POST':
        openclass_form = OpenClassForm(request.POST)
        
        if openclass_form.is_valid():
            openclass = openclass_form.save(commit=False)
            openclass.partner = user.profile

            category = openclass_form.cleaned_data.get('categories')
            new_category = Category.objects.get(name=category.name)
            #Hit db! adakah cara lain agar tidak hit db category?

            try:
                with transaction.atomic():
                    openclass.save()
                    openclass.categories.add(new_category)
                    messages.success(request, 'You post an Open Class.')
                    return redirect(reverse('profiles:profiles', kwargs={'username': user.username}))

            except IntegrityError:
                messages.error(request, 'There is something wrong.')
                return redirect(reverse('profiles:profiles', kwargs={'username': user.username}))


    context = {
        'openclass_form' : openclass_form,
        'profile': user.profile,
    }

    return render(request, 'kelas/openclass_post.html', context)




@login_required(login_url='/accounts/login/')
def OpenClassDeleteView(request, pk):
    partner = request.user.profile
    openclass = OpenClass.objects.get(pk=pk)
    if openclass.partner == partner:
        openclass.delete()
        messages.success(request, 'You deleted an open class post')
    else:
        messages.error(request, 'You cant delete others open class!')
    return redirect(reverse('Home'))


@login_required(login_url='/accounts/login/')
def OpenClassEditView(request, pk):
    user = request.user

    TagFormSet = formset_factory(TagForm, formset=BaseTagFormSet)

    openclass_data = get_object_or_404(OpenClass, partner=user.profile, pk=pk)
 


    openclass_instance = {
            'is_active': openclass_data.is_active,
    }

    if request.method == 'POST':
        openclass_form = OpenClassEditForm(request.POST, instance=openclass_data)

        if openclass_form.is_valid():
            openclass = openclass_form.save(commit=False)
            openclass.partner = user.profile
            try:
                with transaction.atomic():
                    openclass.save()
                    messages.success(request, 'You edit open class post')
                    return redirect(reverse('profiles:profiles', kwargs={'username': user.username}))

            except IntegrityError:
                messages.error(request, 'There is something wrong.')
                return redirect(reverse('profiles:profiles', kwargs={'username': user.username}))

    openclass_form = OpenClassEditForm(initial=openclass_instance)

    context = {
        'openclass_form' : openclass_form,
        'openclass_data': openclass_data,
        'profile': Profile.objects.get(user=user),
    }

    return render(request, 'kelas/openclass_edit.html', context)
