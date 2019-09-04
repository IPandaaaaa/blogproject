from django.urls import path, re_path
from . import views

app_name = 'blog'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    # path('post/<int:pk>/', views.detail, name='detail'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='detail'),
    # path('archives/<int:year>/<int:month>/', views.archives, name='archives'),
    path('archives/<int:year>/<int:month>/', views.ArchiveView.as_view(), name='archives'),
    # path('category/<int:pk>/', views.category, name='category'),
    path('category/<int:pk>/', views.CategoryView.as_view(), name='category'),
    # path('author/<int:author_id>/', views.archivesbyauthor, name='author'),
    path('author/<int:author_id>/', views.ArchivebyauthorView.as_view(), name='author'),
    path('tag/<int:tag_id>', views.TagView.as_view(), name='tag'),
    path('search/', views.search, name='search'),
]
