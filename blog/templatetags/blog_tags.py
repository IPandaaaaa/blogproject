# 存放自定义模板标签


from django import template
from blog.models import Post, Category
from django.db.models.aggregates import Count

register = template.Library()


# 注册自定义模板标签

@register.simple_tag  # 将函数注册为模板标签 template_label
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():  # 实现归档
    date_list = Post.objects.dates('created_time', 'month', order='DESC')
    date_list_t = []
    for date in date_list:
        date_num = Post.objects.filter(created_time__year=date.year,created_time__month=date.month).count()
        date_list_t.append({'year':date.year,'month':date.month,'num':date_num})
    return date_list_t


@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
    # num_posts__gt为查询表达式  过滤掉没有post的分类
