from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .forms import *
from datetime import datetime
# Create your views here.


@login_required(login_url="/login/")
def recipes(request):
    if request.method == "POST":
        data = request.POST
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        user = request.user
        date_posted = data.get('date_posted')

        Recipe.objects.create(
            recipe_image=recipe_image,
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            user=user,
            date_posted=date_posted,
        )

        return redirect('/recipes/')

    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(
            recipe_name__icontains=request.GET.get('search'))

    context = {'recipes': queryset}
    return render(request, 'recipes.html', context)


def update_recipe(request, id):
    queryset = Recipe.objects.get(id=id)

    if request.method == "POST":
        data = request.POST

        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description

        if recipe_image:
            queryset.recipe_image = recipe_image

        queryset.save()
        return redirect('/recipes/')

    context = {'recipe': queryset}
    return render(request, 'update_recipes.html', context)


def delete_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/recipes/')


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid Username.")
            return redirect('/login/')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login/')

        else:
            login(request, user)
            return redirect('/recipes/')

    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')


def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request, "Username already taken.")
            return redirect('/register/')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )

        user.set_password(password)
        user.save()

        messages.info(request, "Account created successfully.")

        return redirect('/register/')

    return render(request, 'register.html')


def details_page(request, id):
    queryset = Recipe.objects.get(id=id)

    context = {'recipe': queryset}
    return render(request, 'details.html', context)


# class AddCommentView(CreateView):
#     model = Comment
#     template_name = 'add_comment.html'
#     fields = '__all__'


def add_comment(request, id):
    recipe = Recipe.objects.get(id=id)
    form = CommentForm(instance=recipe)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=recipe)
        if form.is_valid():
            name = request.user
            body = form.cleaned_data['body']
            c = Comment(post=recipe,
                        name=name,
                        body=body,
                        date_added=datetime.now()
                        )
            c.save()
            return redirect('/recipes/')
        else:
            print('form is invalid')
    else:
        form = CommentForm()

    context = {
        'form': form
    }

    return render(request, 'add_comment.html', context)
