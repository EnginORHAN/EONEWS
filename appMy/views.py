from django.shortcuts import render,redirect
from appMy.models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def indexPage(request, slug=None):
    header_section = True
    if slug:
        news_list = News.objects.filter(category__slug=slug).order_by("-id")
        header_section = False
    else:
        news_list = News.objects.all().order_by("-id")
        
    category_list = Category.objects.all()
    news_left = News.objects.filter(left=True).order_by("-date_now")
    news_slider = News.objects.filter(slider=True).order_by("-date_now")
    context={
        "header_section":header_section,
        "category_list":category_list,
        "news_slider":news_slider,
        "news_left":news_left,
        "news_list":news_list,
    }
    return render(request, "index.html", context)

def detailPage(request,slug):
    news = News.objects.get(slug=slug)
    category_list = Category.objects.all()
    comment_list = Comment.objects.filter(news=news)
    
  
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        message = request.POST.get("comment")
        
        comment = Comment(fullname = fullname, comment = message, news=news)
        comment.save()
        return redirect("detailPage", slug)
    
    context = {
        "category_list":category_list,
        "news":news,
        "comment_list":comment_list,
    }
    return render (request,"detail.html",context)


def contactPage(request):
    category_list = Category.objects.all()
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        title = request.POST.get("title")
        message = request.POST.get("message")
        
        contact = Contact(fullname=fullname, email=email, title=title, message=message)
        contact.save()
        return redirect("contactPage")

    context = {
        "category_list":category_list,
    }
    return render(request , "contact.html", context)



def loginPage(request):
    category_list=Category.objects.all()
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            
            if user:
                login(request,user)
                return redirect("indexPage")
            else:
                messages.error(request,"Kullanıcı Adı veya Şifre Hatalı")
    
    context={
        "category_list":category_list
    }
    return render(request, "user/login.html", context)

def registerPage(request):
    category_list = Category.objects.all()
    
    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        
        if password1 == password2:
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    
                    user = User.objects.create_user(first_name=name, last_name=surname, email=email, username=username, password=password1)
                    
                    user.save()
                    return redirect("loginPage")
    
    context = {
        "category_list":category_list
    }
    return render(request,"user/signup.html",context)

def logoutUser(request):
    logout(request)
    return redirect("indexPage")

def passwordChange(request):
    categor_list = Category.objects.all()
    
    if request.method=="POST":
        username = request.POST.get("username")
        hp = request.POST.get("hiddenpassword")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        try:
            user = User.objects.get(username=username)
            if password1 == password2:
                if user.userinfo.hidden_password == hp:
                    user.set_password(password1)
                    user.save()
                    
                    messages.success(request, "Şifre Başarıyla Değişti")
                    return redirect("loginPage")
            
            else:
                messages.error(request, "Şifreler Aynı Değil")
            
        except:
            messages.error(request,"Kullanıcı kayıtlı değil")
    context={
        "category_list":categor_list
    }
    return render(request,"user/password.html",context)
@login_required(login_url="loginPage")
def hesapPage(request):
    category_list = Category.objects.all()
    
    if request.method =="POST":
        submit=request.POST.get("submit")
        if submit=="userSubmit":
            username=request.POST.get("username")
            password=request.POST.get("password")
            if request.user.check_password(password):
                request.user.username=username
                request.user.save()
                return redirect("hesapPage")

        elif submit=="emailSubmit":
            email=request.POST.get("email")
            password=request.POST.get("password")
            if request.user.check_password(password):
                request.user.email=email
                request.user.save()
                return redirect("hesapPage")

        elif submit == "passwordSubmit":
            password=request.POST.get("password")
            password1=request.POST.get("password1")
            password2=request.POST.get("password2")
            if request.user.check_password(password):
                if password1==password2:
                    request.user.set_password(password1)
                    request.user.save()
                    return redirect("loginPage")
        
    context={
        "category_list":category_list
    }
    return render(request,"hesap.html",context)