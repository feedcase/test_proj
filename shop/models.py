from django.db.models import *
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from test_proj import settings


# Create your models here.


class ShopItem(Model):
    title = CharField(max_length=32, null=False, blank=False)
    url_title = CharField(max_length=32, null=True, blank=False)
    description = TextField(null=False, default='Описание отсутсвует')
    price = DecimalField(max_digits=100, decimal_places=2)
    image = ImageField(upload_to=settings.MEDIA_ROOT, null=False)
    image_big = ImageField(upload_to=settings.MEDIA_ROOT, null=True)
    category_name = TextField(null=False, default='Без категории')
    post_date = DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title

    @property
    def formatted_price(self):
        return f'BYN {self.price}'


class Categories(Model):
    category = TextField(null=True)
    category_image = ImageField(upload_to=settings.MEDIA_ROOT, null=True)
    category_url = CharField(max_length=32, null=True)

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category


class Feeds(Model):
    title = CharField(max_length=32, null=False, blank=False)
    news_image = ImageField(upload_to=settings.MEDIA_ROOT, null=False)
    news_body = CharField(max_length=1000, null=False, blank=False)
    news_post_date = DateTimeField(auto_now_add=True)
    news_category = TextField(null=True, default='Без категории')
    news_big_image = ImageField(upload_to=settings.MEDIA_ROOT, null=True)

    class Meta:
        verbose_name = 'Публикацию'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title


def validate_name(name: str) -> bool:
    import re
    if not re.fullmatch('[а-я, А-Я]+', name):
        raise ValidationError('Invalid name')


class FeedbackModel(Model):
    name = CharField(max_length=100, null=False, blank=False, validators=[validate_name])
    email = EmailField(null=False, blank=False)
    message = CharField(max_length=100, null=False, blank=False)
    phone = CharField(max_length=14, null=False)
    comments = CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Обратная связь'

    def __str__(self):
        return self.name
