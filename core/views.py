from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from item.models import Category, Item
from .forms import SignUpForm


def index(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    return render(
        request, "core/index.html", context={"items": items, "categories": categories}
    )


def contact(request):
    return render(request, "core/contact.html")


class CustomLoginView(LoginView):
    template_name = 'core/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class CustomLogoutView(LogoutView):
    next_page = 'login'


def signup_view(request):
    form = SignUpForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, "core/signup.html", {"form": form})


# Validation For Google registration
def email_exist_with_us(request):
    messages.error(request, 'This email was registered with us! Try with your password')
    return redirect('login')
