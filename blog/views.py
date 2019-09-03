from django.shortcuts import render
from django.http.response import HttpResponse
from blog.models import Post, Category
from django.shortcuts import get_object_or_404
from comments.forms import CommentForm
import markdown


# Create your views here.
def index(request):
    post_list = Post.objects.all().order_by('-created_time')  # -表示逆序
    return render(request, 'blog/index.html', context={
        'post_list': post_list
    })


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.increase_views()
    post.body = markdown.markdown(post.body, extensions=['markdown.extensions.extra',
                                                         'markdown.extensions.codehilite',
                                                         'markdown.extensions.toc', ])
    form = CommentForm()
    comment_list = post.comment_set.all()#因为有外键约束
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'blog/detail.html', context)


# 按日期归档
def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


# 分类
def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


# 按做作者归档
def archivesbyauthor(request, author_id):
    post_list = Post.objects.filter(author_id=author_id)
    return render(request, 'blog/index.html', context={'post_list': post_list})

