from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, permissions
from .models import Product, Cart, CartItem
from .serializers import ProductSerializer, CartItemSerializer, UpdateUserSerializer, ChangePasswordSerializer, LogoutSerializer, AddToCartSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated,AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class RegisterView(APIView):
    permission_classes = [AllowAny]
    @swagger_auto_schema(request_body=RegisterSerializer)
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    @swagger_auto_schema(request_body=ProductSerializer)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AddToCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    @swagger_auto_schema(request_body=AddToCartSerializer)

    def post(self, request):
        # استخدام AddToCartSerializer للتحقق من المدخلات
        serializer = AddToCartSerializer(data=request.data)

        if serializer.is_valid():
            product_id = serializer.validated_data.get("product_id")
            quantity = serializer.validated_data.get("quantity", 1)

            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return Response({"error": "Product is not available"}, status=status.HTTP_404_NOT_FOUND)

            # الحصول أو إنشاء سلة المستخدم
            cart, created = Cart.objects.get_or_create(user=request.user)
            # الحصول أو إنشاء عنصر السلة
            item, created = CartItem.objects.get_or_create(cart=cart, product=product)

            item.quantity += quantity  # إضافة الكمية الجديدة
            item.save()

            return Response({
                "message": "Product successfully added to the cart",
                "quantity": item.quantity
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RemoveFromCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('product_id', openapi.IN_QUERY, description="ID of the product to remove from cart", type=openapi.TYPE_INTEGER)
        ]
    )
    def post(self, request):
        product_id = request.data.get("product_id")
        cart = Cart.objects.get(user=request.user)
        CartItem.objects.filter(cart=cart, product_id=product_id).delete()
        return Response({"message": "Product removed from cart"})

class ProductSearchView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('name', openapi.IN_QUERY, description="Product name", type=openapi.TYPE_STRING),
            openapi.Parameter('category', openapi.IN_QUERY, description="Product category", type=openapi.TYPE_STRING),
            openapi.Parameter('price_min', openapi.IN_QUERY, description="Minimum price", type=openapi.TYPE_NUMBER),
            openapi.Parameter('price_max', openapi.IN_QUERY, description="Maximum price", type=openapi.TYPE_NUMBER),
        ]
    )
    def get(self, request):
        name = request.GET.get('name')
        category = request.GET.get('category')
        products = Product.objects.all()
        price_min = request.GET.get('price_min', None)
        price_max = request.GET.get('price_max', None)
        if name:
            products = products.filter(name__icontains=name)

        if category:
            products = products.filter(category__name__icontains=category)

        if price_min:
            products = products.filter(price__gte=price_min)

        if price_max:
            products = products.filter(price__lte=price_max)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UpdateUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

from django.contrib.auth import update_session_auth_hash

class ChangePasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]


    @swagger_auto_schema(request_body=ChangePasswordSerializer)

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if not user.check_password(serializer.validated_data['old_password']):
                return Response({'error': 'old is wronge'}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(serializer.validated_data['new_password'])
            user.save()
            update_session_auth_hash(request, user)

            return Response({'success': 'sessful change update '}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(request_body=LogoutSerializer)
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            if not refresh_token:
                return Response({'error':'refresh is required'}, status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"detail": "Successfully logged out"}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": "Invalid token or other issue occurred", "details": str(e)}, status=status.HTTP_400_BAD_REQUEST)