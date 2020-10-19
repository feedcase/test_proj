"""test_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from shop.rest import router
from django.urls import path, re_path, include
from shop import views
from django.conf.urls.static import static
from test_proj import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^create/$', views.order_create, name='order_create'),
    path('', views.Index.as_view()),
    path('api/', include(router.urls)),
    path('login', views.Login.as_view(), name='login'),
    path('logout', views.Logout.as_view(), name='logout'),
    path('reset-password', views.ResetPassword.as_view(), name='reset-password'),
    path('registration', views.Registration.as_view(), name='registration'),
    path('products', views.ProductsPage.as_view(), name='products'),
    path('about-us', views.AboutPage.as_view(), name='about-us'),
    path('contacts', views.ContactsPage.as_view(), name='contacts'),
    path('category/<int:category_id>', views.CategoriesView.as_view(), name='category'),
    path('products/<int:product_id>', views.Product.as_view(), name='product'),
    path('', views.Index.as_view(), name='index'),
    path('feed/<int:news_id>', views.Feed.as_view(), name='new'),
    path('account/<int:user_id>', views.AccountPage.as_view(), name='account')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
