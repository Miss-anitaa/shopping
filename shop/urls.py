from django.urls import path
from .views import *

urlpatterns = [
    path('manage', HomePageView.as_view(), name='admin'),

    path('manage/category', CategoryListView.as_view(), name="category"),
    path('manage/category/new', CategoryCreateView.as_view(), name="category_new"),
    path('manage/category/<int:pk>/delete/', CategoryDeleteView.as_view(), name="category_delete"),

    path('manage/product', ProductListView.as_view(), name="product"),
    path('manage/product/new', ProductCreateView.as_view(), name="product_new"),
    path('manage/product/<int:pk>/delete/', ProductDeleteView.as_view(), name="product_delete"),

    path('manage/city', CityListView.as_view(), name="city"),
    path('manage/city/new', CityCreateView.as_view(), name="city_new"),
    path('manage/city/<int:pk>/delete/', CityDeleteView.as_view(), name="city_delete"),

    path('manage/Store', StoreListView.as_view(), name="store"),
    path('manage/Store/new', StoreCreateView.as_view(), name="store_new"),
    path('manage/Store/<int:pk>/delete/', StoreDeleteView.as_view(), name="store_delete"),

    path('manage/StoreProduct', StoreProductListView.as_view(), name="storeproduct"),
    path('manage/StoreProduct/new', StoreProductCreateView.as_view(), name="storeproduct_new"),
    path('manage/StoreProduct/<int:pk>/delete/', StoreProductDeleteView.as_view(), name="storeproduct_delete"),

    path('manage/order', OrderListView.as_view(), name="order"),
    path('manage/order/<int:pk>/update/', OrderUpdateView.as_view(), name="order_update"),
    path('manage/order/<int:pk>/delete/', OrderDeleteView.as_view(), name="order_delete"),

    path('', UserProductListView.as_view(), name='home'),
    path('userOrder/<int:pk>', userOrderSubmitView, name="userOrder"),
    path('orderList', UserOrderListView.as_view(), name='orderList'),
]
