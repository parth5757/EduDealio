from django.shortcuts import render, redirect
from app.views import BaseView
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView
from app.views import SuperUserView,BaseView

# Create your views here.


class MyLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_invalid(self, form):
        messages.error(self.request, 'invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
    

class RegisterUser(CreateView):
        """Create at User Registration"""

        model = User  # model name
        template_name = "register.html"
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "is_active",
        ]  # field that want to send from user
        success_url = reverse_lazy("login")

        """check form is valid or not if valid than executr"""

        def form_valid(self, form):
            form.instance.password = make_password(form.cleaned_data["password"])
            form.save()
            return super().form_valid(form)

        # to check error
        # def form_invalid(self, form):
        #     for error in form.errors:
        #         print("==> error:", error)
        #     return super().form_invalid(form)
