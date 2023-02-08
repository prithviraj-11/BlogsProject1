from django.shortcuts import render,redirect,HttpResponse
from .models import UserInfo,BlogDetails
from datetime import datetime
from .forms import BlogDetailsForm
from django.contrib import messages

# Create your views here.
def home(request):
    blogs=BlogDetails.objects.exclude(published_date__isnull=True)
    return render(request,"index.html",{"blogs":blogs})

def SignUp(request):
    if(request.method=="GET"):
        return render(request,"SignUp.html",{})
    else:
        uname=request.POST["uname"]
        pwd=request.POST["pwd"]

        #Already Exist
        try:
            user=UserInfo.objects.get(username=uname)
        except:
            user=UserInfo(uname,pwd)
            user.save()
        else:
            messages.error(request,"User Name Already Present!! Please Use another User Name and Password.")
            return redirect(SignUp)
            #return HttpResponse("User Name Already Present")
        request.session["uname"]=uname
        messages.success(request,"Done")
        return redirect(home)

def login(request):
    if(request.method=="GET"):
        return render(request,"Login.html",{})
    else:
        #Check UserName and Password
        uname=request.POST["uname"]
        pwd=request.POST["pwd"]
        try:
            user=UserInfo.objects.get(username=uname,password=pwd)
        except:
            messages.error(request,"Invalid Credentials!! Please Enter Valid User Name and Password.")
            return redirect(login)

        #usernmae in session
        request.session["uname"]=uname
        return redirect(home)

def logout(request):
    request.session.clear()
    return redirect(home)

def addBlog(request):
    if request.method == 'POST':
        form = BlogDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
            form = BlogDetailsForm()
    return render(request, 'AddBlog.html', {'form': form})

def updateBlog(request,id):
    if request.method == 'POST':
        title=request.POST['title']
        author=request.POST['author']
        content=request.POST['content']
        old_blog=BlogDetails.objects.get(id=id)
        old_blog.title=title
        old_blog.author=author
        old_blog.content=content
        old_blog.save()
        messages.success(request,"Post updated Successful")
        return redirect(home)
    return render(request, 'UpdateBlog.html',{})