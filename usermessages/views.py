from django.template.context_processors import request
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import Http404
from django.db.models import Q

from .models import UserMessage
from .forms import ChatUserMessage
from accounts.models import User


class UserInbox(LoginRequiredMixin, ListView):
    model = User
    template_name = 'usermessages/user_inbox.html'
    context_object_name = 'users_sender'

    def get_login_url(self):
        return reverse('accounts:login')

    def get_queryset(self):
        return self.model.objects.filter(sent_messages__receiver=self.request.user).distinct()

class UserChatBox(LoginRequiredMixin, CreateView):
    form_class = ChatUserMessage
    template_name = 'usermessages/user_chatbox.html'

    def get_success_url(self):
        return reverse_lazy('usermessages:chatbox', kwargs={'pk':self.kwargs.get('pk')})

    def get(self, request, *args, **kwargs):
        if self.request.user.profile == self.kwargs.get('pk'):
            #bug! even 2 var the same wont raise http404 | bisa jadi untuk notes to self
            raise Http404
        messages.info(self.request, 'Ayo! book aktivitas open class mu sekarang!')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        post = super().post(request, *args, **kwargs)
        messages.success(self.request, 'Message sent!')
        return post

    def form_valid(self, form):
        user_message = form.save(commit=False)
        user_message.sender = self.request.user
        user_message.receiver = User.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_login_url(self):
        return reverse('accounts:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message_list'] = UserMessage.objects.filter(Q(receiver=self.request.user,
                                                            sender=User(pk=self.kwargs.get('pk'))
                                                            )| Q(receiver=User(pk=self.kwargs.get('pk')),sender=self.request.user))
        context['message_sender'] = self.request.user
        context['message_receiver'] = User.objects.get(pk=self.kwargs.get('pk'))
        return context
