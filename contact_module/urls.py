from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.ContactUsView.as_view(), name='contact_us_page'),
    path('creat-profile/', views.CreatProfilePageView.as_view(), name='craet-profil-page'),
    path('profiles/', views.ProfileView.as_view(), name='profiles_page'),
]
