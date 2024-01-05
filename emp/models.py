from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image,ImageDraw

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()
    
    def __str__(self):
        return "%s %s %s" %(self.first_name, self.last_name, self.phone)
    
class cursol(models.Model):
    img=models.ImageField(upload_to='static/%y/%m/%d/')
    title=models.CharField(max_length=100)
    sub_title=models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
class about_photo1(models.Model):
    img=models.ImageField(upload_to='imges/')
    name=models.CharField(max_length=100)
    role=models.CharField(max_length=100)
    quotes=models.TextField()

    def __str__(self):
         return self.name

class about_photo2(models.Model):
    img=models.ImageField(upload_to='imges/')
    name=models.CharField(max_length=100)
    role=models.CharField(max_length=100)
    quotes=models.TextField()

    def __str__(self):
         return self.name
    
class about_photo3(models.Model):
    img=models.ImageField(upload_to='imges/')
    name=models.CharField(max_length=100)
    role=models.CharField(max_length=100)
    quotes=models.TextField()

    def __str__(self):
         return self.name
    
class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()


class Profile(models.Model):
   otp=models.CharField(max_length=6,null=True,blank=True)

class Website(models.Model):
    name=models.CharField(max_length=100)
    qrcode=models.ImageField(upload_to='imges/',blank=True)

    def __str__(self): 
         return self.name
    
    def save(self,*args,**kwargs):
        url = 'http://127.0.0.1:8000/'
        # Generate the QR code using the full URL of your website
        qrcodeimg = qrcode.make(url)
        canvas=Image.new('RGB',(330,330),'white')
        drw=ImageDraw.Draw(canvas)
        canvas.paste(qrcodeimg)
        fname=f'qr_code-{self.name}.png'
        buffer=BytesIO()
        canvas.save(buffer,'PNG')
        self.qrcode.save(fname,File(buffer),save=False)
        canvas.close()
        super().save(*args,**kwargs)

class Contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    description=models.TextField()

    def __str__(self): 
        return f'Message from {self.name}'
    
