from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Book
# Create your views here.
def helloView(request):
    books= Book.objects.all()
    return render(request,"signup.html",{"books":books})

def viewbooks(request):
    books = Book.objects.all()
    return render(request, "viewb.html",{"books":books})

def addBookView(request):
    return render(request,"addb.html")

def addBook(request):
    if request.method=="POST":
        t=request.POST["title"]
        p=request.POST["price"]
        a=request.POST["authors"]
        pu=request.POST["publisher"]
        pa=request.POST["page"]
        print(t,p,a,pu,pa)
        book=Book()
        book.title=t
        book.price=p
        book.authors=a
        book.publisher=pu
        book.page=pa
        
        book.save()
        return HttpResponseRedirect('/view-books/')

def editBook(request):
    if request.method=="POST":
        t=request.POST["title"]
        p=request.POST["price"]
        a=request.POST["authors"]
        pu=request.POST["publisher"]
        pa=request.POST["page"]
        print(t,p,a,pu,pa)
        book=Book.objects.get(id=request.POST['bid'])
        book.title=t
        book.price=p
        book.authors=a
        book.publisher=pu
        book.page=pa
        
        book.save()
        return HttpResponseRedirect('/view-books/')
    

def editBookView(request):
    book=Book.objects.get(id=request.GET['bookid'])
    return render(request,"editb.html",{"book":book})

def deleteBookView(request):
    book=Book.objects.get(id=request.GET['bookid'])
    book.delete()
    return HttpResponseRedirect('/view-books/')
