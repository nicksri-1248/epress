from django.db import models
from loginapp.models import User
from master.models import Item
from datetime import datetime
from django.utils import timezone

#ORDER

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=None)
    quantity = models.PositiveIntegerField()
    date_ordered = models.DateTimeField(auto_now_add=True)
    order_number = models.CharField(max_length=10)
    address = models.CharField(max_length=200, default='')
    address_line_1 = models.CharField(max_length=100, default='')
    address_line_2 = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=100, default='')
    zip_code = models.CharField(max_length=10, default='')
    delivery_date = models.DateField(default=datetime.now)
    delivery_time = models.TimeField(default=timezone.now)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} x {self.item.name}"

#ORDER

#ADDRESS

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.address_line_1}, {self.address_line_2}, {self.city}, {self.state} {self.zip_code}"

#ADDRESS