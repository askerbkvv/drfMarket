from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import (
    MyTokenObtainPairSerializer,
    RegisterSerializer,
    FavoriteSerializer,
)
from .permissions import AnonPermissionOnly, IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .models import User
from rest_framework import generics, status
from products.models import Product
from rest_framework.response import Response


class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AnonPermissionOnly]
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AnonPermissionOnly]
    serializer_class = RegisterSerializer


class UserFavoriteView(generics.UpdateAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        # print(kwargs['product_id'])
        product = Product.objects.get(id=kwargs['product_id'])
        # print('asd')
        # print(request.user)
        # print(request.user.heart.all())
        if request.user and product:
            if product in request.user.heart.all():
                request.user.heart.remove(product)
                request.user.save()
                return Response(data={"status": "removed"}, status=status.HTTP_200_OK)
            else:
                request.user.heart.add(product)
                request.user.save()
                return Response(data={"status": "added"}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)




