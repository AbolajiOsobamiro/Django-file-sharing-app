from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('appRequest.html', views.appRequests, name='apprequests'),
    path('bookRequest.html', views.bookRequests, name='bookrequests'),
    path('movieRequest.html', views.movieRequests, name='movierequests'),
    path('miscRequest.html', views.miscRequests, name='miscrequests'),
    path('appUpload.html', views.appupload, name='appuploads'),
    path('bookUpload.html', views.bookupload, name='bookuploads'),
    path('miscUpload.html', views.miscupload, name='miscuploads'),
    path('movieUpload.html', views.videoupload, name='movieuploads'),
    path('apps.html', views.apps, name='apps'),
    path('books.html', views.books, name='books'),
    path('misc.html', views.misc, name='misc'),
    path('movies.html', views.movies, name='movies'),
    path('requests2.html', views.request2, name='request2'),
    path('signup.html', views.register, name='register'),
    path('login.html', views.login, name='login'),
    path('logout', views.logout, name= 'logout'),
    path('appsearch.html', views.appsearch, name= 'appsearch'),
    path('booksearch.html', views.booksearch, name= 'booksearch'),
    path('miscsearch.html', views.miscsearch, name= 'miscsearch'),
    path('moviesearch.html', views.moviesearch, name= 'moviesearch'),
    path('libsearch.html', views.libsearch, name= 'libsearch')
]
