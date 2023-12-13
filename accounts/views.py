from django.forms.models import BaseModelForm
from django.http import HttpResponse
from blogapp.models import Profile
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignupForm,EditSignupForm,PasswordChangingForm,ProfileForm
from django.shortcuts import render,redirect,get_object_or_404 

# Create your views here.
class CreateUserProfile(generic.CreateView):
    model = Profile
    form_class=ProfileForm
    template_name='registration/create_user_profile.html'

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class UserProfileView(generic.DetailView):
    model = Profile
    template_name= 'registration/user_profile.html'

    def get_context_data(self,*args, **kwargs):
        context = super(UserProfileView,self).get_context_data(*args,**kwargs)
        user_page= get_object_or_404(Profile, id=self.kwargs['pk'])
        context['user_page']=user_page
        return context

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/editprofilepage.html'
    fields=['bio','profile_pic','facebook_url','instagram_url','linkedin_url','github_url']
    success_url = reverse_lazy('home')


class PasswordChangeFormView(PasswordChangeView):
    form_class=PasswordChangingForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html',{})

class UserRegistrationView(generic.CreateView):
    form_class=SignupForm
    template_name='registration/register.html'
    success_url = reverse_lazy('login')

class EditProfileView(generic.UpdateView):
    form_class=EditSignupForm
    template_name='registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

    