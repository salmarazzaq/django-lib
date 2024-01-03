from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import datetime
def index(request):
    return render(request,'management/index.html',)
def BookListView(request):
    booklist = Book.objects.all()
    return render(request,'management/booklist.html',{'booklist':booklist})

def BookDetailview(request,pk):
    book = get_object_or_404(Book,id=pk)
    reviews=Reviews.objects.filter(book=book).exclude(review="none")
    try:
        std = Student.objects.get(enrollment=request.user)
        rev = Reviews.objects.get(review="none")
    except:
        pass
    return render(request,'management/bookdetail.html',locals())
@login_required
def BookCreate(request):
    if not request.user.is_superuser:
        return redirect('index')
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book')
    return render(request, 'management/form.html', locals())
def BookUpdate(request, pk):
    if not request.user.is_superuser:
        return redirect('index')
    obj = Book.objects.get(id=pk)
    form = BookForm(instance=obj)
    if request.method == 'POST':
        form = BookForm(data=request.POST, files=request.FILES, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('book')
    return render(request, 'management/form.html', locals())
@login_required
def BookDelete(request, pk):
    if not request.user.is_superuser:
        return redirect('index')
    obj = get_object_or_404(Book, pk=pk)
    obj.delete()
    return redirect('index')

def book_issue(request):
    if not request.user.is_superuser:
        return redirect('index')
    form = IssueForm()
    if request.method == 'POST':
        form = IssueForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book')
    return render(request, 'management/form.html', locals())
@login_required
def student_request_issue(request,pk ):
    obj = Book.objects.get(id=pk)
    stu=Student.objects.get(enrollment=request.user)
    s = get_object_or_404(Student, enrollment=str(request.user))
    if s.total_books_due < 10:
        message = "book has been isuued, You can collect book from library"
        a = Issue()
        a.student = s
        a.book = obj
        a.Issue_date= datetime.datetime.now()
        obj.available_copies = obj.available_copies - 1
        obj.save()
        stu.total_books_due=stu.total_books_due+1
        stu.save()
        a.save()
    else:
        message = "you have exceeded limit."
        return redirect('booklist')
    return render(request, 'management/result.html', locals())

@login_required
def StudentCreate(request):
    if not request.user.is_superuser:
        return redirect('index')
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            s=form.cleaned_data['enrollment']
            form.save()
            u=User.objects.get(username=s)
            s=Student.objects.get(enrollment=s)
            u.email=s.email
            u.save()
            return redirect('studentlist')
    return render(request, 'management/form.html', locals())
@login_required
def StudentUpdate(request, pk):
    if not request.user.is_superuser:
        return redirect('index')
    obj = Student.objects.get(id=pk)
    form = StudentForm(instance=obj)
    if request.method == 'POST':
        form = StudentForm(data=request.POST, files=request.FILES, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('index')
    return render(request, 'management/form.html', locals())


@login_required
def StudentDelete(request, pk):
    obj = get_object_or_404(Student, pk=pk)
    obj.delete()
    return redirect('index')

@login_required
def StudentList(request):
    student = Student.objects.all()
    return render(request, 'management/studentlist.html', {"students":student})

@login_required
def StudentDetail(request, pk):
    student = get_object_or_404(Student, id=pk)
    book=Issue.objects.filter(student=student)
    return render(request, 'management/studentdetail.html', locals())
@login_required



@login_required
def RatingUpdate(request, pk):
    obj =Reviews.objects.get(id=pk)
    form = RatingForm(instance=obj)
    if request.method == 'POST':
        form = RatingForm(data=request.POST, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('bookdetail',pk=obj.book.id)
    return render(request, 'management/form.html', locals())


@login_required
def RatingDelete(request, pk):
    obj = get_object_or_404(Reviews, pk=pk)
    st=Student.objects.get(enrollment=request.user)
    if not st==obj.student:
        return redirect('index')
    pk = obj.book.id
    obj.delete()
    return redirect('bookdetail',pk)







# def student_request_issue(request, pk):
    # obj = Book.objects.get(id=pk)
    # stu=Student.objects.get(enrollment=request.user)
    # s = get_object_or_404(Student, enrollment=str(request.user))
    # if s.total_books_due < 10:
    #     message = "book has been isuued, You can collect book from library"
    #     a = Issue()
    #     a.student = s
    #     a.book = obj
    #     a.Issue_date= datetime.datetime.now()
    #     obj.available_copies = obj.available_copies - 1
    #     obj.save()
    #     stu.total_books_due=stu.total_books_due+1
    #     stu.save()
    #     a.save()
    # else:
    #     message = "you have exceeded limit."
    #     return redirect('booklist')
    # return render(request, 'management/result.html', locals())








