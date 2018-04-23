def EditProfileView(request, pk):

    args = {'profile': Profile.objects.get(pk=request.user.pk), 'skills': Skill.objects.all()}
    form = EditProfileForm(initial={
                                    'avatar': args['profile'].avatar,
                                    'bio': args['profile'].bio,
                                    'class_description': args['profile'].class_description
                                    })
    args['form'] = form

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=Profile.objects.get(pk=request.user))
        if form.is_valid():
            profile = form.save(commit=False)

            if len(request.FILES) != 0:
                profile.avatar.name = profile.user.username + ".png"
                file_path = settings.MEDIA_ROOT + "\\profiles\\"+ profile.user.username+".png"
                if os.path.exists(file_path):
                    os.remove(file_path)

            profile.save()
            messages.add_message(request, messages.SUCCESS, "Profil telah teredit!")
            return HttpResponseRedirect(reverse_lazy('profiles:profiles', kwargs={'pk' : request.user.pk}))
        else:
            messages.add_message(request, messages.ERROR, "Salah memberikan input")

    return render(request, 'profiles/edit_profile.html', args)

def AddProfileSkill(request, skillname, pk):
    username = request.user.pk
    skill = Skill.objects.get(name=skillname)
    profile = Profile.objects.get(user=username)
    profile.skills.add(skill)
    profile.save()

    return HttpResponseRedirect(reverse('profiles:editprofile', kwargs={'pk': request.user.pk}))

def DeleteProfileSkill(request, skillname, pk):
    username = request.user.pk
    skill = Skill.objects.get(name=skillname)
    profile = Profile.objects.get(user=username)
    profile.skills.remove(skill)
    profile.save()

    return HttpResponseRedirect(reverse('profiles:editprofile', kwargs={'pk': request.user.pk}))



def AddCustomSkill(request, skillname, pk):
    profile = Profile.objects.get(user=request.user.pk)
    custom_skill = CustomSkill.object.create(
        name = skillname,
        profile=profile
    )
    custom_skill.save()

    return HttpResponseRedirect(reverse('profiles:editprofile', kwargs={'pk': request.user.pk}))


def DeleteCustomSkill(request, skillname, pk):
    profile = Profile.objects.get(pk=request.user.pk)
    custom_skill = CustomSkill.object.filter(
        name=skillname,
        profile=profile
    ).delete()
    custom_skill.save()

    return HttpResponseRedirect(reverse('profiles:editprofile', kwargs={'pk': request.user.pk}))
