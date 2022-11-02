from django.shortcuts import render, redirect
from author.forms import AuthorForm
from author.models import Author
from django.core.paginator import Paginator
from django.db.models import Q


def list_author(request):
    queryset = request.GET.get('search')
    authors = Author.objects.all().order_by('full_name')

    if queryset:
        authors = Author.objects.filter(
            Q(full_name__icontains = queryset)
            )

    paginator = Paginator(authors, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'authors': authors,
        'page_obj': page_obj,
    }
    return render(request, 'author/list_author.html', context)


def add_author(request):
    form = AuthorForm()
    context = {
        'form': form,
    }

    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('author:list_author')
    else:
        return render(request,'author/add_author.html', context)


def delete_author(request, pk):
    pk = int(pk)
    try:
        author_sel = Author.objects.get(pk = pk)
    except Author.DoesNotExist:
        return redirect('author:list_author')
    author_sel.delete()
    return redirect('author:list_author')


def edit_author(request, pk):
    pk = int(pk)
    try:
        author_sel = Author.objects.get(id = pk)
    except Author.DoesNotExist:
        return redirect('author:list_author')
    author_form = AuthorForm(request.POST or None, instance = author_sel)
    if author_form.is_valid():
        author_form.save()
        return redirect('author:list_author')
    return render(request, 'author/edit_author.html', {'author_form': author_form})
