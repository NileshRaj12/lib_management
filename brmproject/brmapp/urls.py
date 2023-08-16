
from django.contrib import admin
from django.urls import path,include,re_path
from .views import helloView,addBookView,addBook,editBook,editBookView,deleteBookView,viewbooks
from login.views import loginaction
from signup.views import signaction
urlpatterns = [
    
    path("",helloView),
    path("view-books/",viewbooks),
    path("add-book/",addBookView),
    path("add-book/add",addBook),
    path("edit-book/",editBookView),
    path("edit-book/edit",editBook),
    path("delete-book",deleteBookView),
    path("login/",loginaction),
    path("signup/",signaction),
    
]