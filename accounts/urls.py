from django.conf.urls import url
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from . import views

app_name = "accounts"
urlpatterns = (
    url(r"^signup/$", views.SignUpView.as_view(), name="signup"),
    url(r"^verify/(?P<username>[^/]+)$", views.VerifyView.as_view(), name="verify"),
    url(r"^verify/done/$", views.VerifyDone.as_view(), name="verify_done"),
    url(r"^login/$", views.LoginView.as_view(), name="login"),
    url(r"^signout/$", views.SignoutView.as_view(), name='signout'),
    url(r"^change/password/$", views.PasswordChangeView, name="change_password"),
    url(r"^close/$", views.AccountCloseView, name="account_close"),
    url(r"^close/done/$", TemplateView.as_view(
        template_name='accounts/account_close_done.html'),
        name="account_close_done")
)
