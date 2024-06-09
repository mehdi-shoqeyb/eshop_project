from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .forms import ContactUsModelForm
from .models import ContactUs,ProfileModel

# Create your views here.
from django.urls import reverse


class ContactUsView(CreateView):
    model = ContactUs
    template_name = 'contact_module/contact_us_page.html'
    form_class = ContactUsModelForm
    success_url = '/'
#
# def store_file(file):
#     with open('temp/images.jpg',"wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)
class CreatProfilePageView(CreateView):
    model = ProfileModel
    template_name = 'contact_module/creat_profile_page.html'
    fields = '__all__'
    success_url = '/'

class ProfileView(ListView):
    template_name = 'contact_module/profiles_list_page.html'
    model = ProfileModel
    context_object_name = 'profiles'
