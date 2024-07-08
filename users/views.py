from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm

User = get_user_model()


class Register(View):
    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            form.save()
            print("User saved successfully")
            return redirect('/admin')
        else:
            print("Form is not valid")
            print(form.errors)
        return render(request, 'register.html', {'form': form})
