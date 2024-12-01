from django.shortcuts import render, redirect
from .forms import SignupForm, PostCreateForm, UserUpdateForm, ProfileUpdateForrm, PostUpdateForm
from .models import Post, Profile
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def signup(request):
    if request.method == 'POST':
        forms = SignupForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('login')
    else:
        forms = SignupForm()
    context = {
        "forms":forms
    }
    return render(request, 'registration/signup.html', context)


def log_out(request):
    logout(request)
    return redirect('login')


@login_required
def home(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        forms = PostCreateForm(request.POST)
        if forms.is_valid():
            instance = forms.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('home')
    else:
        forms = PostCreateForm()
    context = {
        "posts": posts,
        "forms":forms
    }
    return render(request, 'base/home.html', context)

@login_required
def profile(request):
    profile = Profile.objects.all()
    context = {
        "posts": profile,
    }
    return render(request, 'base/profile.html', context)

@login_required
def profile_edit(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST or None, instance=request.user)
        p_form = ProfileUpdateForrm(request.POST or None, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForrm(instance=request.user.profile)

    context = {
        "u_form": u_form,
        "p_form": p_form,
    }
    return render(request, 'base/profile_edit.html', context)


@login_required
def post_edit(request, pk):
    posts = Post.objects.get(id=pk)
    if request.method == 'POST':
        forms = PostUpdateForm(request.POST, instance=posts)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    else:
        forms = PostUpdateForm(instance=posts)

    context = {
        "forms": forms,
    }
    return render(request, 'base/post_edit.html', context)


@login_required
def post_delete(request, pk):
    posts = Post.objects.get(id=pk)
    if request.method == 'POST':
        posts.delete()
        return redirect('home')
    return render(request, 'base/post_delete.html')