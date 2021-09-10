from django.contrib.auth import login, authenticate
from person.forms import SingUpForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required

from person.choices import ProfileRoles

# Create your views here.


@permission_required('profile.administrator_access')
def signup_view(request):
    form = SingUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.first_name = form.cleaned_data.get('first_name')
        user.last_name = form.cleaned_data.get('last_name')
        user.email = form.cleaned_data.get('email')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user.profile.rol = form.cleaned_data.get('rol')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('index')
    return render(request, 'singup.html', {'form': form})
