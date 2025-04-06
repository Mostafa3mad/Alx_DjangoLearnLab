from django.urls import path
from .views import RegisterView,ProductCreateView, AddToCartView, RemoveFromCartView,ProductSearchView, UserProfileView,ChangePasswordView,LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView




app_name = 'store'
urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/logout/', LogoutView.as_view(), name='logout'),

    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/product/add/', ProductCreateView.as_view(), name='add-product'),
    path('api/cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    path('api/cart/remove/', RemoveFromCartView.as_view(), name='remove-from-cart'),
    # Search
    path('search/', ProductSearchView.as_view(), name='product-search'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password')

]
