from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm

def register(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'Your account has been created. You may now log in.')
      return redirect('pages-home')
  else:
    form = UserRegistrationForm()
  return render(request, 'accounts/register.html', {'form': form})
