from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import (
    MyTokenObtainPairView,
    RegisterView, UserFavoriteView,
)

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('favorite/<int:product_id>', UserFavoriteView.as_view(), name='heart'),
]
