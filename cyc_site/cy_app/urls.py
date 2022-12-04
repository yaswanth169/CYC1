from django.urls import path
from . import views

urlpatterns=[
    path("",views.sample,name="full_page"),
    path("getres/",views.getres),
    path("signup/",views.signup,name="signup"),
    path("signin/",views.signin,name="signin"),
    path("pss/",views.postsignup,name="psss"),
    path("checkuser/",views.checkuser,name="checkuser"),
    path("forgot1/",views.forgot1,name="frr"),
    path("recoverypass/",views.recoverypass,name="recovery"),
    path("updatepass/",views.checknewpass,name="checknew"),
    path("recoverdng/",views.recoverdng,name="recoverdng")
]