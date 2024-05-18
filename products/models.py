from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator


# from ckeditor.fields import RichTextField

class Category(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    main_category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{str(self.main_category)} | {self.title}'


class Discount(models.Model):
    discount = models.FloatField()
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{str(self.discount)} | {self.description}'


class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT, related_name='products')
    title = models.CharField(max_length=100)
    short_description = models.TextField(blank=True)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    discounts = models.ManyToManyField(Discount, blank=True)
    inventory = models.IntegerField(validators=[MinValueValidator(0)])
    active = models.BooleanField(default=True)
    # slug = models.SlugField()
    # image = models.ImageField(_('Product Image'), upload_to='product/product_cover/', blank=True, )

    datetime_created = models.DateTimeField(_('Date Time of Creation'), default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])


class ProductWeight(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='weights', default=None)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title


# class ActiveCommentsManger(models.Manager):
#     def get_queryset(self):
#         return super(ActiveCommentsManger, self).get_queryset().filter(active=True)


class Comment(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments'
                               , verbose_name='Comment author')
    body = models.TextField(verbose_name=_('Comment Text'))

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=True)

    # Manager
    # objects = models.Manager()
    # active_comments_manager = ActiveCommentsManger()

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])
