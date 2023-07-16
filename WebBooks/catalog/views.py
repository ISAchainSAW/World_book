from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import BookInstance, Book, Author, Genre
from django.views import generic
from .serializers import AuthorSerializier



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
    )


class AuthorAPIView(APIView):

    def get(self, request):

        w = Author.objects.all()
        serializer = AuthorSerializier(data=request.data)
        return Response({'get': AuthorSerializier(w, many=True).data})

    def post(self, request):
        serializer = AuthorSerializier(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        try:
            instance = Author.objects.get(pk=pk)
        except:
            return Response({"error": "Method Put not allowed"})

        serializer = AuthorSerializier(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, pk, format=None):
        instance = Author.objects.get(pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
