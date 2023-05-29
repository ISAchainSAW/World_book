from django.contrib import admin
from django.urls import path, include
from catalog import views
from catalog.views import AuthorAPIView


urlpatterns = [
    path('', views.index, name='index'),
    path('api/v1/authorlist/', AuthorAPIView.as_view()),
    path('admin/', admin.site.urls),
    path(r'^books/$', views.BookListView.as_view(), name='books'),
    path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    path(r'author/', views.AuthorListView.as_view(), name='authors'),
    path('accounts/', include('django.contrib.auth.urls')),
]
