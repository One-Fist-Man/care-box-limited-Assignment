from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]

