# coding:utf-8
from django.db import models
from django.conf import settings



# Create your models here.
STATUS = {
    0: u'正常',
    1: u'草稿',
    2: u'删除',
}

# 资讯来源
NEWS = {
    0: u'oschina',
    1: u'chiphell',
    2: u'freebuf',
    3: u'cnBeta',
}


class Nav(models.Model):
    name = models.CharField(max_length=40, verbose_name=u'导航条内容')
    url = models.CharField(max_length=200, blank=True, null=True, verbose_name=u'指向地址')

    status = models.IntegerField(default=0, choices=STATUS.items(), verbose_name='状态')
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)

    class Meta:
        db_table = "tb_nav"
        verbose_name_plural = verbose_name = u"导航条"
        ordering = ['create_time']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=40, verbose_name=u'名称')
    parent = models.ForeignKey('self', default=None, blank=True, null=True, verbose_name=u'上级分类')
    rank = models.IntegerField(default=0, verbose_name=u'排序')
    status = models.IntegerField(default=0, choices=STATUS.items(), verbose_name='状态')

    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)

    class Meta:
        db_table = "tb_category"
        verbose_name_plural = verbose_name = u'分类'
        ordering = ['rank', '-create_time']

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'作者')
    category = models.ForeignKey(Category, verbose_name=u'分类')
    title = models.CharField(max_length=100, verbose_name=u'标题')
    en_title = models.CharField(max_length=100, verbose_name=u'英文标题')
    # img = models.CharField(max_length=200, default='/static/img/article/default.jpg')
    img = models.ImageField(default='/static/img/article/default.jpg')
    tags = models.CharField(max_length=200, null=True, blank=True, verbose_name=u'标签', help_text=u'用逗号分隔')
    summary = models.TextField(verbose_name=u'摘要')
    content = models.TextField(verbose_name=u'正文')

    view_times = models.IntegerField(default=0)
    zan_times = models.IntegerField(default=0)

    is_top = models.BooleanField(default=False, verbose_name=u'置顶')
    rank = models.IntegerField(default=0, verbose_name=u'排序')
    status = models.IntegerField(default=0, choices=STATUS.items(), verbose_name='状态')

    pub_time = models.DateTimeField(default=False, verbose_name=u'发布时间')
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True)

    def get_tags(self):
        return self.tags.split(',')

    class Meta:
        db_table = 'tb_Article'
        verbose_name_plural = verbose_name = u'文章'
        ordering = ['rank', '-is_top', '-pub_time', '-create_time']

    def __str__(self):
        return self.title


class Column(models.Model):
    name = models.CharField(max_length=40, verbose_name=u'专栏内容')
    summary = models.TextField(verbose_name=u'专栏摘要')
    article = models.ManyToManyField(Article, verbose_name=u'文章')
    status = models.IntegerField(default=0, choices=STATUS.items(), verbose_name='状态')
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)

    class Meta:
        db_table = "tb_column"
        verbose_name_plural = verbose_name = u'专栏'
        ordering = ['-create_time']

    def __str__(self):
        return self.name


class Carousel(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'标题')
    summary = models.TextField(blank=True, null=True, verbose_name=u'摘要')
    # img = models.CharField(max_length=200, verbose_name=u'轮播图片', default='/static/img/carousel/default.jpg')
    img = models.ImageField(max_length=200, verbose_name=u'轮播图片', default='/static/img/carousel/default.jpg')
    article = models.ForeignKey(Article, verbose_name=u'文章')
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)

    class Meta:
        db_table = 'tb_carousel'
        verbose_name_plural = verbose_name = u'轮播'
        ordering = ['-create_time']


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'标题')
    summary = models.TextField(verbose_name=u'摘要')
    news_from = models.IntegerField(default=0, choices=NEWS.items(), verbose_name='来源')
    url = models.CharField(max_length=200, verbose_name=u'源地址')

    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    pub_time = models.DateTimeField(default=False, verbose_name=u'发布时间')

    class Meta:
        db_table = 'tb_news'
        verbose_name_plural = verbose_name = u'资讯'
        ordering = ['-title']


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name=u'用户')
    article = models.ForeignKey(Article,verbose_name=u'文章')
    comment = models.TextField(verbose_name=u'评论内容')
    create_time = models.DateTimeField(u'创建时间',auto_now_add=True)

    class Meta:
        db_table = "tb_comment"
        verbose_name_plural = verbose_name = u'评论'
        ordering = ['-create_time']