from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = "class"

urlpatterns = (
    #url(r"^search/$", views.SearchKelas.as_view(), name='search'),
    #url(r"^request/(?P<pk>\w+)/$", views.RequestKelasView, name='request'),
    #url(r"^success/$", views.RequestSuccessfulView.as_view(), name='request_successful'),
    url(r"^post/$", views.OpenClassPostView, name='openclass_post'),
    url(r"^edit/(?P<pk>\d+)/$", views.OpenClassEditView, name='edit'),
    url(r"^(?P<pk>\d+)/delete/$", views.OpenClassDeleteView, name='delete'),
    #url(r"^$", view.InfoKelas.as_view(),namespace='infokelas'),
)