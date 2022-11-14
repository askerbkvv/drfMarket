from django.urls import path

from . import views
from .views import DetailProducts, CreateProducts

app_name = "store"

urlpatterns = [
    path("", views.ProductListView.as_view(), name="store_home"),
    path("category/", views.CategoryListView.as_view(), name="categories"),
    # path("list/<slug:slug>/", views.Products.as_view(), name="product"),
    path("category/<slug:slug>/", views.CategoryItemView.as_view(), name="category_item"),
    path('detail/<int:pk>/', DetailProducts.as_view(), name="detail"),
    path('create/', CreateProducts.as_view(), name="create"),

]