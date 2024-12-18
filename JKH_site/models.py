from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class Category(models.Model):
    category_name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, )

    def __str__(self):
        return self.category_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, blank=True)
    company_info = models.TextField(blank=True)
    photo = models.ImageField(default='static/media/photos/default_photo.jpg', upload_to='static/media/photos')
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=25, blank=True)

    def save(self, *args, **kwargs):
        super().save()
        edit_image(self.photo.path)


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products', )
    product_category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,
                                         verbose_name='Выберите категорию')
    product_name = models.CharField(max_length=200, blank=False, unique=False)
    product_image = models.ImageField(default='static/media/products/default_image.jpg',
                                      upload_to='static/media/products')
    product_info = models.TextField(blank=True)
    product_price = models.DecimalField(max_digits=20, decimal_places=2)
    date_of_offering = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):
        super().save()
        edit_image(self.product_image.path)


def edit_image(image_path):
    img = Image.open(image_path)
    if img.height < img.width:
        left = (img.width - img.height) / 2
        right = (img.width + img.height) / 2
        top = 0
        bottom = img.height
        img = img.crop((left, top, right, bottom))
    elif img.height > img.width:
        left = 0
        right = img.width
        top = (img.height - img.width) / 2
        bottom = (img.width + img.height) / 2
        img = img.crop((left, top, right, bottom))
    img.thumbnail((400, 400))
    return img.save(image_path)
