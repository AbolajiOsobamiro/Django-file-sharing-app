from django.conf import settings
from django.db.models import Count
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
import os
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . import forms 
from . import models


def appupload(request):
        form = forms.appUploadForm()
        if request.method == 'POST':

                form = forms.appUploadForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save();  #Save the form items to the database
                        return redirect("apps.html")
                else:
                        form = forms.appUploadForm()
                        return render(request, "appUpload.html", {"form": form})
                        
        else:
                return render(request, 'appUpload.html', {"form": form})
        
def bookupload(request):
        form = forms.bookUploadForm()
        if request.method == 'POST':
                form = forms.bookUploadForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save();  #Save the form items to the database
                        return redirect("books.html")
                else:
                        form = forms.bookUploadForm()
                        return render(request, "bookUpload.html", {"form": form})
                        
        else:
                return render(request, 'bookUpload.html', {"form": form})

def videoupload(request):
        form = forms.appUploadForm()
        if request.method == 'POST':
                form = forms.moviesUploadForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save();  #Save the form items to the database
                        return redirect("movies.html")
                else:
                        form = forms.moviesUploadForm()
                        return render(request, "movieUpload.html", {"form": form})
                        
        else:
                return render(request, 'movieUpload.html', {"form": form})

def miscupload(request):
        form = forms.appUploadForm()
        if request.method == 'POST':
                form = forms.miscUploadForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save();  #Save the form items to the database
                        return redirect("misc.html")
                else:
                        form = forms.miscUploadForm()
                        return render(request, "miscUpload.html", {"form": form})
                        
        else:
                return render(request, 'miscUpload.html', {"form": form})


def bookRequests(request):
        form = forms.bookRequestForm()
        if request.method == "POST":
                form = forms.bookRequestForm(request.POST)
                if form.is_valid():
                        form.save(); #Save the request to the database
                        return redirect("books.html")
                else:
                        form = forms.bookRequestForm()
                        return render(request, 'bookRequest.html', {'form': form})
        else:
                return render(request, "bookRequest.html", {"form": form})    
        
def appRequests(request):
        form = forms.appRequestForm()
        if request.method == "POST":
                form = forms.appRequestForm(request.POST)
                if form.is_valid():
                        form.save();   #Save the request to the database
                        return redirect("apps.html")
                else:
                        form = forms.appRequestForm()
                        return render(request, 'appRequest.html', {'form': form})
        else:
                return render(request, "appRequest.html", {"form": form})   
        
def movieRequests(request):
        form = forms.moviesRequestForm()
        if request.method == "POST":
                form = forms.moviesRequestForm(request.POST)
                if form.is_valid():
                        form.save();   #Save the request to the database
                        return redirect("movies.html")
                else:
                        form = forms.moviesRequestForm()
                        return render(request, 'movieRequest.html', {'form': form})
        else:
                return render(request, "movieRequest.html", {"form": form})   
        
def miscRequests(request):
        form = forms.miscRequestForm()
        if request.method == "POST":
                form = forms.miscRequestForm(request.POST)
                if form.is_valid():
                        form.save();  #Save the request to the database
                        return redirect("misc.html")
                else:
                        form = forms.miscRequestForm()
                        return render(request, 'miscRequest.html', {'form': form})
        else:
                return render(request, "miscRequest.html", {"form": form})   
    
def request2(request):
    try:
        instance1 = models.apprequest.objects.all()
        instance2 = models.bookrequest.objects.all()
        instance3 = models.moviesrequest.objects.all()
        instance4 = models.miscrequest.objects.all()

        # This extra function is meant to delete every request after they have been 
        # fulfilled. The titles of both the requests and uploads are appended to a
        # list, after which a for loop is run through each of them to check for any
        # matching elements, and delete the particular request object if there are.


        app_upload_name = models.appUpload.objects.annotate(Count('title'))
        app_req_name =  instance1.annotate(Count('requestname'))
        aReqNames = []
        aUplNames = []
        
        for b in app_upload_name:
            aUplNames.append(b)

        for a in app_req_name:
            aReqNames.append(a)

        for n in aReqNames:
            for m in aUplNames:
                if str(m).lower() == str(n).lower():
                    models.apprequest.objects.filter(requestname = n).delete()
        

        # Same explanation as above
        
        book_upload_name = models.bookUpload.objects.annotate(Count('title'))
        book_req_name =  instance2.annotate(Count('requestname'))
        bReqNames = []
        bUplNames = []
        
        for b in book_upload_name:
            bUplNames.append(b)

        for a in book_req_name:
            bReqNames.append(a)

        for n in bReqNames:
            for m in bUplNames:
                if str(m).lower() == str(n).lower():
                    models.apprequest.objects.filter(requestname = n).delete()

        
        # Same explanation as above
        movies_upload_name = models.moviesUpload.objects.annotate(Count('title'))
        movies_req_name =  instance3.annotate(Count('requestname'))
        MReqNames = []
        MUplNames = []
        
        for b in movies_upload_name:
            MUplNames.append(b)

        for a in movies_req_name:
            MReqNames.append(a)

        for n in MReqNames:
            for m in MUplNames:
                if str(m).lower() == str(n).lower():
                    models.apprequest.objects.filter(requestname = n).delete()

        
        # Same explanation as above
        misc_upload_name = models.miscUpload.objects.annotate(Count('title'))
        misc_req_name =  instance4.annotate(Count('requestname'))
        mReqNames = []
        mUplNames = []
        
        for b in misc_upload_name:
            mUplNames.append(b)

        for a in misc_req_name:
            mReqNames.append(a)

        for n in mReqNames:
            for m in mUplNames:
                if str(m).lower() == str(n).lower():
                    models.apprequest.objects.filter(requestname = n).delete()

        
        return render(request, 'requests2.html', {'instance1':instance1, 'instance2':instance2,
                                                  'instance3':instance3, 'instance4':instance4})

# If either list is empty,it leads to an IndexError. This exception handles that!
    except IndexError:
        return render(request, 'requests2.html', {'instance1':instance1, 'instance2':instance2,
                                                  'instance3':instance3, 'instance4':instance4})
     
def books(request):
        instance = models.bookUpload.objects.all()
        return render(request, 'books.html', {'instance':instance})

def apps(request):
        instance = models.appUpload.objects.all()
        return render(request, 'apps.html', {'instance':instance})
     
def index(request):
        # I want to display only five items from each category on the index page, 
        # therefore, I slice the list to show only the five latest items added!
        instance1 = models.appUpload.objects.order_by('-id')[:5]
        instance2 = models.bookUpload.objects.order_by('-id')[:5]
        instance3 = models.moviesUpload.objects.order_by('-id')[:5]
        instance4 = models.miscUpload.objects.order_by('-id')[:5]
        return render(request, 'index.html', {'instance1':instance1, 'instance2':instance2,
                                                'instance3':instance3, 'instance4':instance4})

def movies(request):
        instance = models.moviesUpload.objects.all()
        return render(request, 'movies.html', {'instance':instance})
     
def misc(request):
        instance = models.miscUpload.objects.all()
        return render(request, 'misc.html', {'instance':instance})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']


        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already in use!')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already in use!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();  #Creates a new user
                return redirect('login')
            
        else:
            messages.info(request, 'Passwords do not match!')
            return redirect('register')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials!')
            return redirect('login')
        
    else:
        return render(request, 'login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('/')


def download(request, path):
        file_path = os.path.join(settings.MEDIA_ROOT, path)
        
        if os.path.exists(file_path):
              with open(file_path, 'rb') as fh:
                     response = HttpResponse(fh.read(), 
                                             content_type="application/file")
                     response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
                     return response
        raise Http404


def appsearch(request):
       if request.method == 'POST':
              searched = request.POST['searched']
              # Here, I filter this class (appUpload) by the searched item, so only
              # instances containing the search item are returned

              instances = models.appUpload.objects.filter(title__contains=searched)
              number = len(instances)
              return render(request, 'appsearch.html', {'searched': searched, 'instances':instances, 'number':number})
       else:
              return render(request, 'appsearch.html')
       

def booksearch(request):
       if request.method == 'POST':
              searched = request.POST['searched']
              instances = models.bookUpload.objects.filter(title__contains=searched)
              number = len(instances)
              return render(request, 'booksearch.html' ,{'searched':searched, 'instances': instances, 'number':number})
       else:
              return render(request, 'booksearch.html')
       
def miscsearch(request):
       if request.method == 'POST':
              searched = request.POST['searched']
              instances = models.miscUpload.objects.filter(title__contains=searched)
              number = len(instances)
              return render(request, 'miscsearch.html', {'searched':searched, 'instances': instances, 'number':number})
       else:
              return render(request, 'miscsearch.html')
       
def moviesearch(request):
       if request.method == 'POST':
                searched = request.POST['searched']
                instances = models.moviesUpload.objects.filter(title__contains=searched)
                number = len(instances)
                return render(request, 'moviesearch.html', {'searched':searched, 'instances': instances, 'number':number})
       else:
              return render(request, 'moviesearch.html')
       

def libsearch(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        inst1= models.appUpload.objects.filter(title__contains=searched) 
        inst2 =  models.bookUpload.objects.filter(title__contains=searched) 
        inst3 =  models.moviesUpload.objects.filter(title__contains=searched) 
        inst4 =  models.miscUpload.objects.filter(title__contains=searched)
    # Here, I combine all the instances defined above in order to utilize
    # them all in my search method!
        instances = inst1.union(inst2).union(inst3).union(inst4)
        number = len(instances)
        return render(request, 'libsearch.html', {'searched':searched, 'instances': instances, 'number':number})
    else:
              return render(request, 'libsearch.html')



