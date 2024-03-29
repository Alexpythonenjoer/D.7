from django.urls import path
# Импортируем созданное нами представление
from .views import PostsList, PostsDetail, PostsCreate, PostsUpdate, PostsDelete


urlpatterns = [
   path('news/', PostsList.as_view()),
   path('<int:pk>', PostsDetail.as_view(), name='posts_detail'),
   path('create/', PostsCreate.as_view(), name='posts_create'),
   path('<int:pk>/edit/', PostsUpdate.as_view(), name='posts_update'),
   path('<int:pk>/delete/', PostsDelete.as_view(), name='posts_delete'),
   path('articles/create/', PostsCreate.as_view(), name='article_create'),
   path('<int:pk>/edit/,', PostsUpdate.as_view(), name='article_update'),
   path('<int:pk>/delete/', PostsDelete.as_view(), name='article_delete')

]
