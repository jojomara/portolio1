from django.db import models # type: ignore
from datetime import datetime
from django.contrib.auth.models import User # type: ignore


# Create your models here.
class Stocks(models.Model):
    item_name = models.CharField(max_length = 50, null = True, blank = True)
    stock_types = models.CharField(max_length = 50, null = True, blank = True)
    stock_date = models.DateTimeField(default=datetime.now())
    stock_time = models.TimeField(auto_now_add=True)
    total_quantity = models.IntegerField(default=0, null = True, blank = True)
    stock_cost = models.IntegerField(default = 0, null = True, blank = True)
    stock_dealer_name = models.CharField(max_length = 50, null = True, blank = True)
    stock_branch_name = models.CharField(max_length = 50, null = True, blank = True)
    stock_contact = models.CharField(max_length = 50, null = True, blank = True)
    unit_price = models.IntegerField(default = 0, null = True, blank = True)

    def __str__(self):
        return f"{self.item_name} - {self.total_quantity}"




    
    
class Sale(models.Model):
    # Associating property item with the name of stock being kept in the stock model
    item = models.ForeignKey(Stocks, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    amount_received = models.IntegerField(default=0, null=True, blank=True)
    issued_to = models.CharField(max_length=50, null=True, blank=True)
    unit_price = models.IntegerField(default=0, null=True, blank=True)
    stock_date = models.DateTimeField(default=datetime.now())
    stock_time = models.TimeField(auto_now_add=True)
    sales_agent = models.CharField(max_length=50, null=True, blank=True)


    
    def get_total(self):
    # Set default values to 0 if quantity or unit_price is None
        quantity = self.quantity if self.quantity is not None else 0
        unit_price = self.unit_price if self.unit_price is not None else 0
        total = quantity * unit_price
        return int(total)
    
    def get_total(self):
        total = self.quantity * self.item.unit_price
        return int(total)

    def get_change(self):
        change = self.get_total() - self.amount_received
        return abs(int(change))
    
    def __str__(self):
        return self.item.item_name


    def get_change(self):
        change = self.amount_received - self.get_total()
        return abs(int(change))

    def __str__(self):
        return self.item.item_name




class CreditSale(models.Model):
    buyer_name = models.CharField(max_length=100)
    national_id = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    contacts = models.CharField(max_length=15)
    amount_due = models.IntegerField()
    sales_agent_name = models.CharField(max_length=100)
    due_date = models.DateField()
    produce_name = models.CharField(max_length=100)
    produce_type = models.CharField(max_length=50)
    tonnage = models.IntegerField()
    dispatch_date = models.DateField()

    def __str__(self):
        return f"{self.buyer_name} - {self.produce_name}"
    

