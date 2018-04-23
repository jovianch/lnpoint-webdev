from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from api.views import accounts, kelas
from django.conf.urls import url

urlpatterns = [
    url(r'^token/refresh/$', refresh_jwt_token),
    url(r'^token/verify/$', verify_jwt_token),

    url(r'^users/login/$', obtain_jwt_token),
    url(r'^users/register/$', accounts.RegisterView.as_view()),
    url(r'^users/me/$', accounts.MeView.as_view()),

    url(r'^categories/$', kelas.CategoryView.as_view()),

    url(r'^classes/$', kelas.OpenClassView.as_view())
]
