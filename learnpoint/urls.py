from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^api/v1/', include('api.urls', namespace='api')),

    url(r'^admin/', admin.site.urls),
    url(r'^$', views.Landing_Page.as_view(), name='landing_page'),
    url(r'^home/$', views.Home.as_view(), name='Home'),
    url(r"^accounts/", include('accounts.urls', namespace='accounts')),
    url(r"^contactus/", views.contact_us_view, name='contactus'),
    url(r'^about/', views.About.as_view(), name='about'),
    url(r'^messages/', include('usermessages.urls', namespace='usermessages')),
    url(r'^test/', views.test_view, name='test'),
    url(r'^welcome_back/', views.WelcomeBack_temp.as_view(), name="welcome_back"),
    url(r'^add_avatar/$', views.WelcomeAddAvatar.as_view(), name='welcome_addavatar'),

    url(r"^class/", include('kelas.urls', namespace='kelas')),
    url(r'^activity/', include('activity.urls', namespace='activity')),
    url(r'^discover/', views.Discover.as_view(), name='discover'),

    url(r"^(?P<username>[^/]+)/", include('profiles.urls', namespace='profiles')),


]

if settings.DEBUG :
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'learnpoint.views.my_custom_page_not_found_view'
