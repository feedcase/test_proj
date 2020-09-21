from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.views import View
from shop.models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from shop.forms import *
import datetime
from django.shortcuts import resolve_url


class Index(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        items = ShopItem.objects.all().order_by('post_date')[:4]
        feed = Feeds.objects.all()
        categories = Categories.objects.all()
        new_feeds = feed.order_by('news_post_date')[:2]
        days = new_feeds[0].news_post_date.day
        months = new_feeds[0].news_post_date.month
        return render(request, 'index.html', {'items': items, 'category': categories, 'feeds': new_feeds,
                                              'day': days, 'month': months})


class AboutPage(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'about-us.html')


class ContactsPage(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        form_components = FeedbackForm
        return render(request, 'contacts.html', {'form': form_components})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return self.get(request)
        else:
            return render(request, 'contacts.html', {'form': form})


class ProductsPage(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        items = ShopItem.objects.all()
        return render(request, 'products.html', {'items': items})


class Product(View):
    def get(self, request: HttpRequest, product_id: int) -> HttpResponse:
        item = ShopItem.objects.get(pk=product_id)
        category = Categories.objects.get(category=item.category_name)
        category_id = category.id
        return render(request, 'product.html', {'product': item, 'id': category_id})


class Login(View):
    def post(self, request: HttpRequest) -> HttpResponse:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            return render(request, '/', {'error': True})


class Registration(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'registration.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            return render(request, 'registration.html', {'error': 'Пароли не совпадают'})
        try:
            user = User.objects.create_user(username=username, password=password, email=email)
        except IntegrityError:
            return render(request, 'registration.html', {'error': 'Такое имя уже существует'})
        login(request, user)
        return redirect('/')


class Logout(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        logout(request)
        return redirect(request.META.get('HTTP_REFERER'))


class CategoriesView(View):
    def get(self, request: HttpRequest, category_id: int) -> HttpResponse:
        category = Categories.objects.get(pk=category_id)
        items = ShopItem.objects.filter(category_name=category.category)
        return render(request, 'categories.html', {'cat_items': items, 'category': category})


class Feed(View):
    def get(self, request: HttpRequest, news_id: int) -> HttpResponse:
        feed = Feeds.objects.get(pk=news_id)
        feeds_time = feed.news_post_date
        category = Categories.objects.get(category=feed.news_category)
        category_id = category.id
        days = feeds_time.strftime('%d')
        month = feeds_time.strftime('%m')
        return render(request, 'news.html', {'feeds': feed, 'day': days, 'month': month, 'id': category_id})


class AccountPage(View):
    # def get(self, request: HttpRequest) -> HttpResponse:
    #     if request.user.is_authenticated:
    #         ...
    # render(request, )
    #
    ...