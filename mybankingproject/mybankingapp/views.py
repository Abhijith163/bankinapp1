# mybankingapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from .models import Branch
from .forms import CustomUserCreationForm
from .forms import UserProfileForm



from .forms import CustomUserCreationForm
import json
from django.http import JsonResponse



def index(request):
    return render(request, 'index.html')

def branches(request):
    # Implement logic to get branches from the database
    branches = ['District 1', 'District 2', 'District 3', 'District 4', 'District 5']
    return render(request, 'branches.html', {'branches': branches})

def district_wikipedia(request, district):
    # Implement logic to redirect to the corresponding Wikipedia page
    return redirect('https://en.wikipedia.org/wiki/{}'.format(district))


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("Login successful. Redirecting...")
                return redirect('welcome')  # Assuming you have a URL pattern named 'welcome'
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})




def user_profile(request):
    print('ooooo')
    if request.method == 'POST':
        print("oo")
        form = UserProfileForm(request.POST)
        try:
            if form.is_valid():
                # Process the form data and save the user profile
                user_profile = form.save(commit=False)
                user_profile.user = request.user  # Assign the logged-in user
                user_profile.save()

                # Print the POST data
                print("POST data:", request.POST)

                return render(request, 'success.html', {'message': 'Application accepted'})
            # else:
            #     return render(request, 'success.html', {'message': 'Application failed'})

        except Exception as e:
            print(str(e))
    else:
        form = UserProfileForm()
    return render(request, 'user_profile.html', {'form': form})


def get_branches(request):
    district = request.GET.get('district')
    print(district)
    branches = Branch.objects.filter(district=district).all()
    print(branches.count())
    branches = json.dumps([{'name': branch.name, "id": branch.id} for branch in branches])
    print(branches)
    return JsonResponse({'branches': branches})

def welcome_view(request):
    return render(request, 'welcome.html')