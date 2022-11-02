from django.shortcuts import render, redirect
from category.forms import CategoryForm
from category.models import Category


def list_category(request):
    categories = Category.objects.all().order_by()
    context = {
        'categories': categories
    }
    return render(request, 'category/list_category.html', context = context)


def add_category(request):
    form = CategoryForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('category:list_category')
    else:
        return render(request,'category/add_category.html', context)


def delete_category(request, pk):
    pk = int(pk)
    try:
        category_sel = Category.objects.get(pk = pk)
    except Category.DoesNotExist:
        return redirect('category:list_category')
    category_sel.delete()
    return redirect('category:list_category')


def edit_category(request, pk):
    pk = int(pk)
    try:
        category_sel = Category.objects.get(id = pk)
    except Category.DoesNotExist:
        return redirect('category:list_category')
    category_form = CategoryForm(request.POST or None, instance = category_sel)
    if category_form.is_valid():
        category_form.save()
        return redirect('category:list_category')
    return render(request, 'category/edit_category.html', {'category_form': category_form})
