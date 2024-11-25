from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .forms import SaleForm, CreditSaleForm, StocksForm, AddForm
from .filters import StocksFilter
from django.contrib import messages
from .models import Stocks, Sale, CreditSale
#accessing our models so that we can get content out of them#
from groceryapp.models import Stocks,Sale
#borowing decorators from django to restrict access to our pages by putting @login required#
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request,'groceryapp/index.html')

@login_required
def home(request):
#we are creating avariable pointing it to all the objects in it#
    products = Stocks.objects.all().order_by('-id')
    #applying filters to the querryset#
    product_filters = StocksFilter(request.GET,queryset=products)
    products = product_filters.qs
    return render(request,'groceryapp/home.html',{'products':products,'product_filters':product_filters})

@login_required
def product_detail(request,product_id):
    product = Stocks.objects.get(id = product_id)
    return render(request,'groceryapp/product_detail.html',{'product':product})



@login_required
def manage_credit_sale(request, credit_sale_id=None):
    if credit_sale_id:
        credit_sale = get_object_or_404(CreditSale, id=credit_sale_id)
    else:
        credit_sale = None

    if request.method == 'POST':
        form = CreditSaleForm(request.POST, instance=credit_sale)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreditSaleForm(instance=credit_sale)

    return render(request, 'groceryapp/manage_credit_sale.html', {'form': form, 'credit_sale': credit_sale})

@login_required
def delete_credit_sale(request, credit_sale_id):
    credit_sale = get_object_or_404(CreditSale, id=credit_sale_id)
    credit_sale.delete()
    return redirect('home')


@login_required
def delete_detail(request,product_id):
    product = Stocks.objects.get(id = product_id)
    product.delete()
    return HttpResponseRedirect(reverse('home'))

@login_required
def issue_item(request, pk):
    # Use get_object_or_404 to handle the case where Stocks with pk does not exist
    issued_item = get_object_or_404(Stocks, id=pk)

    if request.method == 'POST':
        sales_form = SaleForm(request.POST)
        if sales_form.is_valid():
            new_sale = sales_form.save(commit=False)
            new_sale.item = issued_item
            new_sale.unit_price = issued_item.unit_price
            new_sale.save()
            
            # Update stock quantity
            issued_quantity = int(request.POST['quantity'])
            issued_item.total_quantity -= issued_quantity
            issued_item.save()
            
            return redirect('receipt')
    else:
        sales_form = SaleForm()

    return render(request, 'groceryapp/issue_item.html', {'sales_form': sales_form})

       
@login_required
def receipt(request):
    sales = Sale.objects.all().order_by('-id')
    return render(request,'groceryapp/receipt.html',{'sales':sales})

@login_required
def receipt_detail(request, receipt_id):
    receipt = Sale.objects.get(id=receipt_id)

    # Calculate the total price
    total_price = receipt.quantity * receipt.unit_price

    # Calculate the change
    change = receipt.amount_received - total_price

    # Pass the total price and change to the template
    context = {
        'receipt': receipt,
        'total_price': total_price,
        'change': change
    }

    return render(request, 'groceryapp/receipt_detail.html', context)




@login_required
def loginout(request):
    return render(request, 'groceryapp/logout.html')


@login_required
def daily_sales(request):
    sales = Sale.objects.all().order_by('-id')  # You can filter this to only show today's sales
    return render(request, 'groceryapp/daily_sales.html', {'sales': sales})


@login_required
def edit_sale(request, sale_id):
    sale = get_object_or_404(Sale, id=sale_id)

    if request.method == 'POST':
        sale_form = SaleForm(request.POST, instance=sale)
        if sale_form.is_valid():
            sale_form.save()
            return redirect('daily_sales')
        else:
            # If the form is invalid, it will render the errors back to the template
            return render(request, 'groceryapp/edit_sale.html', {'sale_form': sale_form, 'sale': sale})
    else:
        sale_form = SaleForm(instance=sale)

    return render(request, 'groceryapp/edit_sale.html', {'sale_form': sale_form, 'sale': sale})




@login_required
def add_stock(request):
    if request.method == 'POST':
        form = StocksForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Stock has been added successfully.')
            return redirect('home')
    else:
        form = StocksForm()

    return render(request, 'groceryapp/add_stock.html', {'form': form})


@login_required
def add_item(request, pk):
    issued_item = Stocks.objects.get(id=pk)
    
    # Initialize the form with data only if it's a POST request
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            added_quantity = int(request.POST.get('total_quantity'))
            issued_item.total_quantity += added_quantity
            issued_item.save()
            print(added_quantity)
            print(issued_item.total_quantity)
            return redirect('home')
    else:
        form = AddForm()  # For GET requests, initialize an empty form

    # Always return a response, even if it's a GET request or if the form is invalid
    return render(request, 'groceryapp/add_item.html', {'form': form})

            #TO add to the remaining stock quantity is increasing

        