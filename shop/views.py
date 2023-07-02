from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from .models import *

class HomePageView(LoginRequiredMixin ,TemplateView):
    template_name = 'home.html'


#-------------------ADMIN VIEWS-------------------


#Categories

class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'category.html'


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'category_new.html' 
    fields = "__all__"
    success_url = reverse_lazy('category')


class CategoryDeleteView(LoginRequiredMixin, DeleteView): 
    model = Category 
    template_name = 'category_delete.html' 
    success_url = reverse_lazy('category')


#Product

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'product.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'product_new.html' 
    fields = "__all__"
    success_url = reverse_lazy('product')
    



class ProductDeleteView(LoginRequiredMixin, DeleteView): 
    model = Product 
    template_name = 'product_delete.html' 
    success_url = reverse_lazy('product')


#City

class CityListView(LoginRequiredMixin, ListView):
    model = City
    template_name = 'city.html'


class CityCreateView(LoginRequiredMixin, CreateView):
    model = City
    template_name = 'city_new.html' 
    fields = "__all__"
    success_url = reverse_lazy('city')


class CityDeleteView(LoginRequiredMixin, DeleteView): 
    model = City 
    template_name = 'city_delete.html' 
    success_url = reverse_lazy('city')

#Inventory

class StoreListView(LoginRequiredMixin, ListView):
    model = Store
    template_name = 'Store.html'


class StoreCreateView(LoginRequiredMixin, CreateView):
    model = Store
    template_name = 'Store_new.html' 
    fields = "__all__"
    success_url = reverse_lazy('store')


class StoreDeleteView(LoginRequiredMixin, DeleteView): 
    model = Store 
    template_name = 'Store_delete.html' 
    success_url = reverse_lazy('store')


class StoreProductListView(LoginRequiredMixin, ListView):
    model = StoreProduct
    template_name = 'StoreProduct.html'


class StoreProductCreateView(LoginRequiredMixin, CreateView):
    model = StoreProduct
    template_name = 'StoreProduct_new.html' 
    fields = "__all__"
    success_url = reverse_lazy('storeproduct')


class StoreProductDeleteView(LoginRequiredMixin, DeleteView): 
    model = StoreProduct 
    template_name = 'StoreProduct_delete.html' 
    success_url = reverse_lazy('storeproduct')

#Order

class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order.html'


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    template_name = 'order_update.html' 
    fields = "__all__"
    success_url = reverse_lazy('order')


class OrderDeleteView(LoginRequiredMixin, DeleteView): 
    model = Order 
    template_name = 'order_delete.html' 
    success_url = reverse_lazy('order')


#---------------------------------------------------------

#users purchaseable products based on their city
class UserProductListView(LoginRequiredMixin, ListView):
    model = StoreProduct
    template_name= 'home.html'
    
    def get_queryset(self):
        return StoreProduct.objects.filter(store__city=self.request.user.city)

#user order submit view    
@login_required(login_url='login')
def userOrderSubmitView(request, pk):
    if request.method == 'POST':
        product = StoreProduct.objects.get(id=pk)
        quantity = request.POST.get('quantity')
        if product.quantity >= int(quantity):
            product.quantity -= int(quantity)
            product.save()
            newOrder = Order.objects.create(username=request.user, product=product, quantity=quantity)
            newOrder.save()
            return render(request, 'order_success.html')
        else:
            return render(request, 'order_error.html')
        
    else:
        product = StoreProduct.objects.get(id=pk)
        context = {
                'product': product,
            }
        return render(request, 'userOrder.html', context)


#users previous orders view
class UserOrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name= 'userOrderList.html'
    
    def get_queryset(self):
        return Order.objects.filter(username=self.request.user)
