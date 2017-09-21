from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.  0o
def signup(request):
    if request.method == 'POST':
        User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        print("post worked")
        render(request, 'accounts/signup.html')
    else:
        return render(request, 'accounts/signup.html')
