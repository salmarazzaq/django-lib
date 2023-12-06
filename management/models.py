from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
from django.db.models.signals import post_save



class Book(models.Model):
    title = models.CharField(max_length=100,default='DEFAULT VALUE', blank=True,null=True)
    authar = models.CharField(max_length=100,default='DEFAULT VALUE', blank=True,null=True)
    description = models.TextField(max_length=1000,help_text="Enter description",default='DEFAULT VALUE', blank=True,null=True)
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    total_copies = models.IntegerField(null=True)
    available_copies = models.IntegerField(null=True)
    issue_date = models.DateTimeField(null=True)
    pic=models.ImageField(blank=True, null=True, upload_to='book_image')
    def get_absolute_url(self):
        return reverse('bookdetail', args=[str(self.id)])
    
    def __str__(self):
        return self.title


def create_user(sender, *args, **kwargs):
    if kwargs['created']:
        user = User.objects.create(username=kwargs['instance'],password="dummypass")
class Student(models.Model):
    enrollment = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=20)
    branch = models.CharField( max_length=50)
    contact_no = models.CharField( max_length=50)
    email = models.EmailField(unique=True)
    total_books_due=models.IntegerField(default=0)
    def __str__(self):
        return str(self.enrollment)
    
    
post_save.connect(create_user, sender=Student)


class Issue(models.Model):
    student = models.ForeignKey('Student',on_delete=models.CASCADE)
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    Issue_date = models.DateTimeField(null=True,blank=True)
    return_date = models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return self.student.name+'issued'+self.book.title
class Reviews(models.Model):
    review = models.CharField( max_length=100 ,default="none")
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    student = models.ForeignKey("Student",  on_delete=models.CASCADE)
    CHOICES = (
         ('0', '0'),
        ('.5', '.5'),
        ('1', '1'),


    )
    rating=models.CharField(max_length=3, choices=CHOICES, default='2')
