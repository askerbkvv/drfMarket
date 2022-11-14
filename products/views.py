from django.views.generic import DetailView
from rest_framework import generics, mixins

from users.permissions import RolePermissions
from . import models
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# class Products(generics.RetrieveAPIView):
#     lookup_field = "slug"
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


class CategoryItemView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return models.Product.objects.filter(
            category__in=Category.objects.get(slug=self.kwargs["slug"]).get_descendants(include_self=True)
        )


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.filter(level=1)
    serializer_class = CategorySerializer


class DetailProducts(
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.RetrieveAPIView,
    mixins.ListModelMixin
):
    permission_classes = [RolePermissions]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def put(self, *args, **kwargs):
        return self.update(*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CreateProducts(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = [RolePermissions]
    serializer_class = ProductSerializer
    passed_id = None

    def get_queryset(self):
        request = self.request
        qs = Product.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)


