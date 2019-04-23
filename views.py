from django.shortcuts import render
from .models import Registration,LeaveApplication,Complaint
from .forms import RegisterForm,LeaveApplicationForm,ComplaintForm,UserLoginForm
from django.shortcuts import redirect 
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm  
from django.urls import reverse
from django.http import HttpResponseRedirect




def index(request):
    
    return render(request,'system/index.html',{})
def contact(request):
    
    return render(request,'system/contact.html',{})
def about(request):
    
    return render(request,'system/about.html',{})

def profile(request):
    
    return render(request,'system/profile.html',{})

def admin_profile(request):
    user = request.user
    return render(request,'system/admin_profile.html',{})

def post_detail(request,pk):
    post = get_object_or_404(Registration,pk=pk)
    return render(request, 'system/post_detail.html', {'post': post})

def post_list(request):
    posts = Registration.objects.all()
    return render(request, 'system/post_list.html', {'posts':posts})

def leave_list(request):
    posts = LeaveApplication.objects.all()
    return render(request, 'system/leave_list.html', {'posts':posts})

def complaint_list(request):
    posts = Complaint.objects.all()
    return render(request, 'system/complaint_list.html', {'posts':posts})
    


def student_registration(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = RegisterForm()
    return render(request, 'system/sign_up.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Registration, pk=pk)
    if request.method == "POST":
        form = RegisterForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = RegisterForm(instance=post)
    return render(request, 'system/sign_up.html', {'form': form})






def login_view(request):
    
    next = request.GET.get('next')

    form = UserLoginForm(request.POST or None)
    
    if form.is_valid():
        name = form.cleaned_data.get('name')
        password = form.cleaned_data.get('password')
        #user1=Registration.objects.get(name=name)
        #request.session['member']=name.pk
        user = authenticate(name = name,password = password)
        login(request,user)
        if next :
            return redirect(next)
        
        return HttpResponseRedirect(reverse('profile'))
        #user1=Registration.objects.get(name=form.cleaned_data.get('name'))
        #request.session['member']=user1.id
    context = {
        'form':form,
        }
   
    return render(request,"system/login.html",context)

def leave_application(request):
    if request.method == "POST":
        form = LeaveApplicationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/')
    else:
        form = LeaveApplicationForm()
    return render(request, 'system/leave.html', {'form': form})

def complaint(request):
    if request.method == "POST":
        form = ComplaintForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/')
    else:
        form = ComplaintForm()
    return render(request, 'system/complaint.html', {'form': form})

   



def admin_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('admin_profile'))
        else:
            context['error'] = "Provide Valid Credentials"
            return render(request,"system/log.html",context)

    else:
        return render(request,"system/log.html",context)



