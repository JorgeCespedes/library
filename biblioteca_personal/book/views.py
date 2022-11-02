from django.shortcuts import render, redirect
from book.models import Book
from book.forms import BookForm
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def list_book(request):
    queryset = request.GET.get('search') # 'name' de la plantilla 'search'
    books = Book.objects.all().order_by('title')
    
    if queryset:
        books = Book.objects.filter(
            Q(title__icontains = queryset)
            )

    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'books': books,
        'page_obj': page_obj,
    }
    return render(request, 'book/list_book.html', context=context)


def add_book(request):
    form = BookForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home:list_book')
    else:
        return render(request, 'book/add_book.html', context)


def delete_book(request, pk):
    pk = int(pk)
    try:
        book_sel = Book.objects.get(pk = pk)
    except Book.DoesNotExist:
        return redirect('home:list_book')
    book_sel.delete()
    return redirect('home:list_book')


def edit_book(request, pk):
    pk = int(pk)
    try:
        book_sel = Book.objects.get(id = pk)
    except Book.DoesNotExist:
        return redirect('home:list_book')
    book_form = BookForm(request.POST or None, instance = book_sel)
    if book_form.is_valid():
        book_form.save()
        return redirect('home:list_book')
    context = {
        'book_sel': book_sel,
        'book_form': book_form,
    }
    return render(request, 'book/edit_book.html', context)


def detail_book(request, pk):
    pk = int(pk)
    
    book_detail = Book.objects.get(id = pk)
    rating = int(book_detail.rating)
    price = float(book_detail.price)
    context = {
        'book_detail': book_detail,
        'rating': rating,
        'price': price,
    }
    
    return render(request,'book/detail_book.html', context)


def report_status(request):
    book_all = Book.objects.all()
    book_count_all = book_all.count()
    
    read = book_all.filter(status='Read')
    read_count = read.count()
    
    noread = book_all.filter(status='No Read')
    noread_count = noread.count()
    
    reading = book_all.filter(status='Reading')
    reading_count = reading.count()
    
    porcentaje = 100
    book_count_all_percent = format(book_count_all/book_count_all*porcentaje, '.2f')
    read_count_percent = format(read_count/book_count_all*porcentaje, '.2f')
    noread_count_percent = format(noread_count/book_count_all*porcentaje, '.2f')
    reading_count_percent = format(reading_count/book_count_all*porcentaje, '.2f')

    context ={
        'book_all'      : book_all,
        'book_count_all': book_count_all,
        'read'          : read,
        'read_count'    : read_count,
        'noread'        : noread,
        'noread_count'  : noread_count,
        'reading'       : reading,
        'reading_count' : reading_count,
        'book_count_all_percent': book_count_all_percent,
        'read_count_percent'    : read_count_percent,
        'noread_count_percent'  : noread_count_percent,
        'reading_count_percent' : reading_count_percent,
      }
    
    return render(request, 'reports/report_status.html', context)