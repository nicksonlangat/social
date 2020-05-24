from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('new/post', views.PostCreate.as_view(), name='create'),
    path('post/<slug:slug>/edit/', views.PostUpdate.as_view(), name='edit'),
    path('post/<slug:slug>/delete/', views.PostDelete.as_view(), name='delete'),
]
