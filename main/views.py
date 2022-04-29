from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Product, Owner
from django.urls import reverse
from django.shortcuts import redirect
from .forms import OwnerForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def index(request):
    name = 'zhansaya'
    # products = Product.objects.all()
    # products = Product.objects.get(name = "Test")
    if request.method =="POST":
        full_name=request.POST.get("full_name", "test")
        # owner = Owner(full_name = full_name)
        # owner.full_name += " edited"
        # owner.save()
        owner = OwnerForm(request.POST, request.FILES)
        owner.save()
        print(full_name)
        return redirect(reverse('main:index_page', args=()))
#     products = Product.objects.filter(cost__gt = 100)
#     return render(request, "main/index.html", {"name":name, "products":products})

    owners = Owner.objects.all()
    return render(request, "main/index.html", {"name":name,  "owners": owners})
# def welcome(request):
#     username = 'zhansaya'
#     return render(request, "main/welcome.html", {"username": username})
#
# class MyTemplateView(TemplateView):
#     template_name = 'main/c_based_temp.html'
#     def get_context_data(self,**kwargs):
#         return {}


def detail(request, id ):
    owner = Owner.objects.get(pk=id)
    return render(request, "main/detail.html", {"owner":owner})

def register(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        email = request.POST.get("email", None)
        first_name = request.POST.get("first_name", None)
        last_name = request.POST.get("last_name", None)
        user = User.objects.create_user(username=username,
                                       password=password,
                                       email=email,
                                       first_name=first_name,
                                       last_name=last_name
                                       )
        user.save()
        return redirect(reverse("main:login_page", args= ()))

    return render(request, "main/register_page.html", {})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect(reverse("main:profile_page", args= ()))
        else:
            return redirect(reverse("main:login_page", args= ()))
    return render(request, "main/login_page.html", {})

def profile(request):
    if request.user.is_authenticated:
        return render(request, "main/profile_page.html", {})

    else:
            return redirect(reverse("main:login_page", args= ()))

def logout_view(request):
    logout(request)
    return redirect(reverse("main:login_page", args =()))
