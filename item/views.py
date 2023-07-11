from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Item, Category
from .forms import NewItemForm, EditItemForm


def search(request):
    query = request.GET.get("query", "")
    category_id = request.GET.get("catid", "")
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()

    if query:
        q = Q(name__icontains=query) | Q(description__icontains=query)
        items = Item.objects.filter(q)

    elif category_id:
        items = items.filter(category=category_id)

    return render(
        request,
        "item/search.html",
        {"items": items, "query": query, "categories": categories},
    )


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, "item/detail.html", {"item": item})


@login_required(login_url="login")
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect("dashboard:index")


@login_required(login_url="login")
def new_item(request):
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect("item_detail", pk=item.id)
    else:
        form = NewItemForm()

    return render(request, "item/new_item.html", {"form": form})


@login_required(login_url="login")
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item.save()
            return redirect("item_detail", pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, "item/edit_item.html", {"form": form})
