from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    title = models.CharField(("Kategori"), max_length=50)
    slug = models.SlugField(("slug"))
    
    def __str__(self):
        return self.title   

class News(models.Model):
    category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE, null=True)
    title = models.CharField(("Başlık"), max_length=50)
    text = models.TextField(("Haber"))
    date_now = models.DateField(("Tarih"), auto_now=False, auto_now_add=False)
    author = models.CharField(("Yazar"), max_length=50)
    image = models.ImageField(("Haber Resim"), upload_to="", max_length=None,null=True)
    
    left = models.BooleanField(("Öne Çıkanlarda Göster"), default=False)
    slider = models.BooleanField(("Sliderda Göster"), default=False)
    slug = models.SlugField(("slug"),blank=True)
    
    def __str__(self):
        return self.title
    
    def save(self):
        self.slug = slugify(self.title)
        super().save()
    
class Contact(models.Model):
    fullname = models.CharField(("Ad-Soyad"), max_length=50)
    email = models.EmailField(("Email"), max_length=254)
    title = models.TextField(("Konu"))
    message = models.TextField(("Messaj"))
    date_now = models.DateTimeField(("Tarih-Saat"), auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.fullname

    
class Comment(models.Model):
    news = models.ForeignKey(News, verbose_name=("Haber"), on_delete=models.CASCADE, null=True)
    fullname = models.CharField(("Ad - Soyad"), max_length=50)
    comment = models.TextField(("Yorum"),null=True)
    date_now = models.DateTimeField(("Tarih Saat"), auto_now=False, auto_now_add=True, null=True)

    def __str__(self):
        return self.news.title
 

class Userinfo(models.Model):
    user = models.OneToOneField(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    hidden_password = models.CharField(("Gizli Yanıt"), max_length=50)
    
    def __str__(self):
        return self.user.username
    