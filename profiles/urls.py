from django.conf.urls import url
from . import views

app_name = "profiles"
urlpatterns=[
    url(r'^$', views.ProfileView.as_view(), name='profiles'),
    url(r'^edit/$', views.EditProfileView, name='editprofile'),
    url(r'^follow/$', views.follow, name='follow'),
    url(r'^unfollow/$', views.unfollow, name='unfollow'),
    url(r"^story/$", views.StoryProfileView.as_view(), name="stories"),
]
