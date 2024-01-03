"""Library_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from .feed import LatestEntriesFeed
from management import views


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('book/', views.BookListView, name='book'),
    path('book/issue', views.book_issue, name='book_issue'),
    path('book/<int:pk>/requestissue/', views.student_request_issue, name='requestissue'),
    path('book/<int:pk>', views.BookDetailview, name='bookdetail'),
    path('book/create/', views.BookCreate, name='bookcreate'),
    path('book/<int:pk>/update/', views.BookUpdate, name='bookupdate'),
    path('book/<int:pk>/delete/', views.BookDelete, name='bookdelete'),
    path('student/<int:pk>/delete/', views.StudentDelete, name='studentdelete'),
    path('student/create/', views.StudentCreate, name='studentcreate'),
    path('student<int:pk>/update/', views.StudentUpdate, name='studentupdate'),
    path('student/<int:pk>', views.StudentDetail, name='studentdetail'),
    path('student/', views.StudentList, name='studentlist'),
    path('feed/', LatestEntriesFeed(), name='feed'),
    path('rating/<int:pk>/update/', views.RatingUpdate, name='ratingupdate'),
    path('rating/<int:pk>/delete/', views.RatingDelete, name='ratingdelete'),
   
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




