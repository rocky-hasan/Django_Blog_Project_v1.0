from django.urls import path
from .views import HomeView,ArticleDetailView,AddPostView,UpdatePostView,DeletePostView,AddCategoryView,categoryview,categorylistview,LikeView,AddCommentView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article-detail/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('updatepost/edit/<int:pk>/', UpdatePostView.as_view(), name='updatepost'),
    path('deletepost/delete/<int:pk>/', DeletePostView.as_view(), name='deletepost'),
    path('addpost/',AddPostView.as_view(),name='addpost' ),
    path('article-detail/<int:pk>/addcomment/',AddCommentView.as_view(),name='add_comment' ),
    path('addcategory/',AddCategoryView.as_view(),name='addcategory' ),
    path('category/<str:cats>',categoryview,name='category' ),
    path('category_list/',categorylistview,name='category_list' ),
    path('like/<int:pk>',LikeView,name='like_post' ),
]