from django.contrib import admin

from apps.products.models import Category, Product, ProductImage, ProductReview


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    search_fields = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}
    list_per_page = 20


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "price", "category"]
    search_fields = ["name", "slug", "category__name"]
    prepopulated_fields = {"slug": ("name",)}
    list_per_page = 20


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ["product", "image"]
    search_fields = ["product__name", "image"]
    list_per_page = 20


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ["product", "user", "rating", "created_at"]
    search_fields = ["product__name", "user__username"]
    list_per_page = 20
