from django.contrib import admin
from .models import Stocks, CreditSale

class CreditSaleAdmin(admin.ModelAdmin):
    list_display = ('buyer_name', 'produce_name', 'amount_due', 'due_date')
    search_fields = ('buyer_name', 'produce_name')
    list_filter = ('due_date', 'dispatch_date')

# Register models with the admin site
admin.site.register(Stocks)
admin.site.register(CreditSale, CreditSaleAdmin)
