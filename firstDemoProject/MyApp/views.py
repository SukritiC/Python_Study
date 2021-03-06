from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.


# the function must accept request and give a response- django view
def index(request):
    # view must return a proper HTTP response - hence imported the above HttpResponse
    # return HttpResponse('Hello World')

    # passing the objects to the view
    list_books = Book.objects.all()
    # return HttpResponse(list_books)

    # creating context to pass objects to HTML page
    context = {
        'book_list':list_books
    }

    # rendering the template
    return render(request,'MyApp/index.html',context)


def detailed_book_view(request, book_id):
    book_info = Book.objects.get(id=book_id)
    context = {
        'book_info':book_info
    }
    # return HttpResponse("This is the book no %s"%book_id)

    return render(request, 'MyApp/book_details.html',context)




# creating a view isn't sufficient - it must be associated with a URL pattern
# first create a new URL Pattern inside urls.py