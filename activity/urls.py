from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "activity"

urlpatterns = [
    url(r"^plan/$", views.ActivityPlanView, name='plan'),
    #url(r"^edit/(?P<pk>)\d+)/$", views.ActivityEditView, name='activity_edit'),
    url(r"^(?P<pk>\d+)/$", views.ActivityDetailView.as_view(), name="detail"),
    url(r"^(?P<pk>\d+)/done/$", views.ActivityDoneView.as_view(), name="done"),
    url(r"^(?P<pk>\d+)/delete/$", views.ActivityDeleteView, name='delete'),
    url(r"^(?P<pk>\d+)/join/$", views.ActivityJoinView, name='join'),
    url(r"^(?P<pk>\d+)/unjoin/$", views.ActivityUnJoinView, name='unjoin'),
    url(r"^(?P<pk>\d+)/like/$", views.ActivityLike, name='like'),
    url(r"^(?P<pk>\d+)/unlike/$", views.ActivityUnlike, name='unlike'),

]





