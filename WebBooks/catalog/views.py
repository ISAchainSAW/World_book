from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInstance, Book, Author, Genre
from django.views import generic
from rest_framework import generics
from serializers import AuthorSerializier


# Create your views here.
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4


class BookDetailView(generic.DetailView):
    model = Book


class BookListView(generic.ListView):
    model = Book
    paginate_by = 3


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact=2).count()
    num_authors = Author.objects.count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(request, 'index.html', context={'num_books': num_books,
                                                  'num_instances': num_instances,
                                                  'num_instances_available': num_instances_available,
                                                  'num_authors': num_authors,
                                                  'num_visits': num_visits,
                                                  }
                  # 'num_visits': num_visits},
                  )


class AuthorAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializier
