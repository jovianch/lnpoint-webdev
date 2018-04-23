from django.conf.urls import url
from . import views

app_name = "usermessages"
urlpatterns=[
    url(r'^$', views.UserInbox.as_view(), name='inbox'),
    url(r"^chat/(?P<pk>[^/]+)/$", views.UserChatBox.as_view(), name='chatbox'),
]
