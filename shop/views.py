from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.views import View
from shop.models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from shop.forms import *
from orders.models import OrderItem
from orders.forms import OrderCreateForm
from cart.cart import Cart
from cart.forms import CartAddProductForm


def order_create(request):
    cart = Cart(request)
    form = OrderCreateForm(request.POST)
    if form.is_valid():
        order = form.save()
        for item in cart:
            OrderItem.objects.create(order=order,
                                     product=item['product'],
                                     price=item['price'],
                                     quantity=item['quantity'])
        cart.clear()
        return render(request.META.get('HTTP_REFERER'))


class Index(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        items = ShopItem.objects.all().order_by('post_date')[:4]
        feed = Feeds.objects.all()
        categories = Categories.objects.all()
        new_feeds = feed.order_by('news_post_date')[:2]
        return render(request, 'index.html', {'items': items, 'category': categories, 'feeds': new_feeds})


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
        cart_product_form = CartAddProductForm()
        return render(request, 'product.html', {'product': item, 'id': category_id,
                                                'cart_product_form': cart_product_form})


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
        return redirect('index')


class CategoriesView(View):
    def get(self, request: HttpRequest, category_id: int) -> HttpResponse:
        category = Categories.objects.get(pk=category_id)
        items = ShopItem.objects.filter(category_name=category.category)
        return render(request, 'categories.html', {'cat_items': items, 'category': category})


class Feed(View):
    def get(self, request: HttpRequest, news_id: int) -> HttpResponse:
        feed = Feeds.objects.get(pk=news_id)
        category = Categories.objects.get(category=feed.news_category)
        category_id = category.id
        return render(request, 'news.html', {'feeds': feed, 'id': category_id})


class AccountPage(View):
    def get(self, request: HttpRequest, user_id: int) -> HttpResponse:
        if request.user.is_authenticated:
            account = request.user
            feed = Feeds.objects.all().order_by('news_post_date')
            cart = Cart(request)
            order = OrderItem.objects.filter(order__email=account.email)
            return render(request, 'account.html', {'acc': account,
                                                    'feeds': feed,
                                                    'cart': cart,
                                                    'order': order})
        else:
            redirect('/')


class ResetPassword(View):
    def post(self, request: HttpRequest) -> HttpResponse:
        old_password = request.POST['old_password']
        new_password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if new_password and new_password != confirm_password or new_password == old_password:
            return render(request, 'account.html', {'error': 'Старый и новый пароли совпадают'})
        if new_password != confirm_password:
            return render(request, 'account.html', {'error': 'Пароли не совпадают'})
        user = User.objects.get(username__exact=request.user.username)
        user.set_password(new_password)
        user.save()
        login(request, user)
        return redirect(request.META.get('HTTP_REFERER'))
