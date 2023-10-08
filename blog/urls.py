from django.urls import path
from . import views




urlpatterns = [
    path('',views.home,name='blog_home'),
    path('about/',views.about,name='blog_about'),
    path('contact/',views.contact,name='blog_contact'),
    path('post/<int:id>/',views.post_detail,name='blog_post'),

]
