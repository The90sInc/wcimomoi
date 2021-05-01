from . import views
from django.urls import path

urlpatterns = [
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('', views.PostList.as_view(), name='home'),
    path("<slug:slug>/delete/", views.BlogDeleteView.as_view(), name= "post_delete"),
    path("<slug:slug>/edit/", views.BlogUpdateView.as_view(), name= "post_edit"),
    path('post/new/', views.BlogCreateView.as_view(), name='post_new'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]

