from django.contrib.auth import login
from rest_framework import serializers

from main.models import Nav, Article, Carousel, Category
from passport.models import User


class NavSerializers(serializers.ModelSerializer):
    class Meta:
        model = Nav
        fields = ("id", 'name', 'url')


class ArticleListSerializers(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format="%Y-%m-%d", required=False, read_only=True)
    category = serializers.StringRelatedField()

    class Meta:
        model = Article
        fields = ("id", "category", "title", "img", "summary", "create_time", "view_counts", "comment_counts")


class HostArticleSerializers(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = Article
        fields = ("id", "title", "view_counts","category")


class CarouselLIstSerializers(serializers.ModelSerializer):
    class Meta:
        model = Carousel
        fields = ("id", "summary", "img", "article")


class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ("id","name")