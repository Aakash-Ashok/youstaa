from django.urls import path
from yousta.views import *


urlpatterns=[

path("signup/",SignUpView.as_view(),name="signup"),
path('signin',LoginView.as_view(),name="login"),
path("category/add/",CategoryCreateView.as_view(),name="category-create")

]