from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from item.models import Item


@login_required(login_url='login')
def index(request):
    items = Item.objects.filter(created_by=request.user)
    return render(request, 'dashboard/index.html', {'items': items})
