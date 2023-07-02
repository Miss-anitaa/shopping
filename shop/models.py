from django.db import models

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="نام")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="نام")
    price = models.IntegerField(verbose_name="قیمت")
    img = models.ImageField(upload_to="upload/", blank=True)
    quantity = models.PositiveIntegerField(verbose_name="مقدار هر بسته به گرم")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="دسته بندی")

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=200, verbose_name="نام")

    def __str__(self):
        return self.name
    
class Store(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="شهر")

    def __str__(self):
        return self.city.name

class StoreProduct(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="نام")
    store = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name="انبار")
    quantity = models.PositiveIntegerField(blank=False, verbose_name="تعداد")

    def __str__(self):
        return self.name.name
    

    
class Order(models.Model):
    from accounts.models import CustomUser

    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="سفارش دهنده")
    product = models.ForeignKey(StoreProduct, on_delete=models.CASCADE, verbose_name="محصول")
    quantity = models.PositiveIntegerField(blank=False, verbose_name="تعداد")

    SUBMITTED = 'ثبت شد'
    READY_TO_SEND = 'آماده ارسال'
    STATUS_CHOICES = [
        (SUBMITTED, 'ثبت شد'),
        (READY_TO_SEND, 'آماده ارسال'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=SUBMITTED, verbose_name="وضعیت")

    def __str__(self):
        return str ('{name} ({prod} * {quan})'.format(name=self.username.username, prod=self.product, quan=self.quantity))
        


