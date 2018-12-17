from django.shortcuts import render
from rest_framework.generics import ListAPIView

# Create your views here.
from blog.utils.pagination import StandardResultsSetPagination
from main.models import Nav, Article, Carousel, Category
from main.serializers import NavSerializers, ArticleListSerializers, HostArticleSerializers, CarouselLIstSerializers, CategorySerializers


class NavAPIView(ListAPIView):

    serializer_class = NavSerializers
    queryset = Nav.objects.all()


class ArticleListAPIView(ListAPIView):

    serializer_class = ArticleListSerializers
    # queryset = Article.objects.order_by("create_time")
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        category = self.request.query_params.get('category')
        order_by = self.request.query_params.get('order_by')
        if not order_by:
            order_by = "create_time"
        if not category:
            category = "all"
        if category == 'all':
            return Article.objects.order_by("-{0}".format(order_by))
        else:
            category = Category.objects.get(name=category)
            return Article.objects.filter(category=category).order_by("-{0}".format(order_by))


class HostArticleAPIView(ListAPIView):

    serializer_class = HostArticleSerializers
    queryset = Article.objects.order_by("-view_counts")[:10]


class CarouselListAPIView(ListAPIView):

    serializer_class = CarouselLIstSerializers
    queryset = Carousel.objects.order_by("-create_time")[:5]


class CategoryListsAPIView(ListAPIView):

    serializer_class = CategorySerializers
    queryset = Category.objects.all()


