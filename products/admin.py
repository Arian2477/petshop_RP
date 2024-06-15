from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin

from . import models


class CommentsInline(admin.TabularInline):
    model = models.Comment
    fields = ['author', 'body', 'active', ]
    extra = 1
# ModelAdminJalaliMixin


@admin.register(models.Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'slug', 'price', 'datetime_expiration', 'active', 'datetime_created', 'datetime_modified']

    inlines = [
        CommentsInline,
    ]


@admin.register(models.ProductWeight)
class ProductWeightAdmin(admin.ModelAdmin):
    list_display = ['product', 'title', 'description', ]


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', ]


@admin.register(models.SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', ]


@admin.register(models.Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['discount', 'description', ]


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'body', 'active', ]
