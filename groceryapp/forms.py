from django import forms
from django.core.exceptions import ValidationError
from .models import Sale, CreditSale, Stocks


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['quantity', 'amount_received', 'issued_to']

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity is None or quantity <= 0:
            raise ValidationError("Quantity must be greater than zero.")
        return quantity

    def clean_unit_price(self):
        unit_price = self.cleaned_data.get('unit_price')
        if unit_price is None or unit_price < 0:
            raise ValidationError("Unit price must be a positive number.")
        return unit_price   

class CreditSaleForm(forms.ModelForm):
    class Meta:
        model = CreditSale
        fields = ['buyer_name', 'national_id', 'location', 'contacts', 'amount_due', 'sales_agent_name', 'due_date', 'produce_name', 'produce_type', 'tonnage', 'dispatch_date']



class StocksForm(forms.ModelForm):
    class Meta:
        model = Stocks
        fields = ['item_name', 'stock_types', 'stock_date', 'total_quantity', 'stock_cost', 'stock_dealer_name', 'stock_branch_name', 'stock_contact', 'unit_price']


class   AddForm(forms.ModelForm):
    class Meta:
        model = Stocks
        fields = ['total_quantity']        


