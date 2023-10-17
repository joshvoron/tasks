from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy,reverse
from .forms import UserCreateForm, UserUpdateForm, UserLoginForm, UserDeleteForm
from .models import CustomUser
from django.contrib.messages.views import SuccessMessageMixin

def profile(request):
    user = UserUpdateForm.objects.get(username=request.user.username)
    context = {
        'user' : user,
    }
    return render(request,'profile.html',context)


class RegistrationView(CreateView, SuccessMessageMixin):
    model = CustomUser
    template_name = 'register.html'
    success_message = 'Your registration was successful!'
    form_class = UserCreateForm
    success_url = '/'



class UserLoginView(LoginView):
    template_name = 'login.html'
    form_class = UserLoginForm
    def get_success_url(self):
        url = '/'
        return url

class PasswordUpdateView(PasswordChangeView):
    template_name = 'changepassword.html'

    def get_success_url(self):
        user_id = self.request.user.id
        return reverse('logout')

    def get_object(self, queryset=None):
        user_id = self.kwargs['pk']
        return get_object_or_404(CustomUser, pk=user_id)

class UserDeleteView(DeleteView):
    template_name = 'deleteaccount.html'
    model = CustomUser
    success_url = '/'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['User'] = self.request.user
        return context

class UpdateProfileView(UpdateView):
    template_name='profile.html'
    form_class = UserUpdateForm
    model = CustomUser
    def get_success_url(self):
        user_id = self.request.user.id
        return reverse("profile", kwargs={'pk' : user_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs['pk']
        context['user'] = get_object_or_404(CustomUser, pk=user_id)
        context['User'] = self.request.user
        return context

    def get_object(self, queryset=None):
        user_id = self.kwargs['pk']
        return get_object_or_404(CustomUser, pk=user_id)




