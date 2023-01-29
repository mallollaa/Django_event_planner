from django.shortcuts import render , redirect
from users.forms import RegisterForm ,LoginForm
from django.contrib.auth import logout,login, authenticate
# Create your views here.
def register_user(request):
    form = RegisterForm()
    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():
            user =form.save(commit=False)
            user.set_password(user.password)
            user.save()
        
            login(request, user)

            return redirect('home')
    context = {
        'form': form
    }
    return render(request , 'register_form.html' ,context)

def get_login(request):
    return render (request,'login_forms.html')

def login_view(request):
    form = LoginForm() # we are passing an empty form 
    if request.method =='POST':
        form = login_view(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        auth_user = authenticate(username=username ,password=password)
        if auth_user is not None:
            login(request , auth_user)
            return redirect('home')
    context = {

			'form': form
		}
    return render(request, 'login_forms.html',context)
