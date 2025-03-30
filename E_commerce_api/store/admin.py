from django.contrib import admin
from .models import Category, Product, Cart, CartItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'category', 'stock_quantity', 'user']
    list_filter = ['category', 'user']
    search_fields = ['name', 'description']
    list_editable = ['price', 'stock_quantity']
    raw_id_fields = ['category', 'user']
    ordering = ['id']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # إذا كان المستخدم مشرفًا، يمكنه رؤية كل المنتجات، غير ذلك فقط منتجاته
        if not request.user.is_superuser:
            queryset = queryset.filter(user=request.user)
        return queryset
class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1
    readonly_fields = ['product', 'quantity']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'get_total_items']
    inlines = [CartItemInline]
    search_fields = ['user__username']

    def get_total_items(self, obj):
        return obj.cartitem_set.count()

    get_total_items.short_description = 'عدد المنتجات'
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'cart', 'product', 'quantity']
    list_filter = ['cart', 'product']
    search_fields = ['product__name', 'cart__user__username']


admin.site.site_header = "لوحة إدارة المتجر"
admin.site.site_title = "إدارة المتجر"
admin.site.index_title = "مرحبًا بك في لوحة الإدارة"

