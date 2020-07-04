# coding=utf-8
from post.models import Post
from django.db.models import Count

def getRightInfo(request):

    # 获取分类信息
    r_catepost = Post.objects.values('category__cname', 'category').annotate(c=Count('*')).order_by('-c')

    # 获取近期文章
    r_recPost = Post.objects.all().order_by('-created')[:3]

    # 获取归档信息
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("select created, count('*') from t_post GROUP BY DATE_FORMAT(created, '%Y-%m') ORDER BY created desc")
    r_filePost = cursor.fetchall()

    return {'r_catepost': r_catepost, 'r_recPost': r_recPost, 'r_filePost': r_filePost}
