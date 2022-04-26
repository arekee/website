from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('', views.main, name='main'),
    path('places',views.places, name='places'),
    path('login', views.login, name='login'),
    #path('sign-up', views.signup, name='signup'),
    path('basket', views.basket, name='basket'),
    path('main', views.main, name='main '),
    path('hotels', views.hotels, name='hotels'),
    path('upload/', views.upload, name='add-comment'),
    path('update/<int:comment_id>', views.update_Comment),
    path('delete/<int:comment_id>', views.delete_Comment),
    path('post/<slug:post_slug>', views.show_post, name='post'),
    path('signup', views.signup, name='signup'),
    path('create', views.create, name='create'),
    path('send/', views.send_message, name='send')

]