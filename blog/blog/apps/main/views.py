from django.shortcuts import render
from rest_framework.generics import ListAPIView

# Create your views here.
from blog.utils.pagination import StandardResultsSetPagination
from main.models import Nav, Article, Carousel
from main.serializers import NavSerializers, ArticleListSerializers, HostArticleSerializers, CarouselLIstSerializers


class NavAPIView(ListAPIView):

    serializer_class = NavSerializers
    queryset = Nav.objects.all()


class ArticleListAPIView(ListAPIView):

    serializer_class = ArticleListSerializers
    queryset = Article.objects.order_by("create_time")
    pagination_class = StandardResultsSetPagination


class HostArticleAPIView(ListAPIView):

    serializer_class = HostArticleSerializers
    queryset = Article.objects.order_by("-view_times")[:10]


class CarouselList(ListAPIView):

    serializer_class = CarouselLIstSerializers
    queryset = Carousel.objects.order_by("-create_time")[:5]
