from django.contrib import admin
from django.urls import path, include
from catalog import views


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path(r'^books/$', views.BookListView.as_view(), name='books'),
    path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    path(r'author/', views.AuthorListView.as_view(), name='authors'),
    path('accounts/', include('django.contrib.auth.urls')),
]
