from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post

from comments.models import Comment
from comments.forms import CommentForm


# Create your views here.

def post_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)#找到要评论的文章
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)  # 利用表单的数据生成 Comment 模型类的实例，但还不保存评论数据到数据库
            comment.post = post
            comment.save()
            return redirect(post)#会自动调用get_absolute_url 方法 找到URL
        else:
            comment_list = post.comment_set.all()#因为外键关联 所以可以用comment_set.all()反向查询所有comment
            #comment_list = Comment.objects.filter(post = post)
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'blog/detail.html', context=context)
    return redirect(post)
