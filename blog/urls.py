from django.urls import path
from . import views
from .views import (PubDetail, 
add_favorite_pub, 
mylist_pub, 
remove_favorite_pub,
liker,
PubCreatView,
PubvCreatView)

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog-app'),
    path('contacte/', views.ncontacte, name='nous-contacter'),
    path('liste/', views.listing, name='liste'),
    path('predications/', views.predication, name='predications'),
    path('pub/<int:pk>', PubDetail.as_view(), name='Pub-detail'),
    path('pub-add-favorite/<int:pub_id>', add_favorite_pub, name='favoris'),
    path('pub-remove-favorite/<int:pub_id>', remove_favorite_pub, name='remove'),
    path('liker/<int:pub_id>', liker, name='like'),
    path('mylist/', mylist_pub, name='mylist'),
    path('pub-new/', PubCreatView.as_view(), name='Publications'),
    path('pub-newv/', PubvCreatView.as_view(), name='Pub-video'),
]
