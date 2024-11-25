from django.contrib import admin
from django.urls import path
#we are accessing the views file of this very app(adminapp)
from groceryapp import views
from .views import issue_item, add_stock,add_item
#we are accessing the functionality to login#
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path('',views.index,name = 'index'),
    path('home/',views.home,name = 'home'),
    path('manage_credit_sale/', views.manage_credit_sale, name='add_credit_sale'),  # For adding a new credit sale
    path('edit_credit_sale/<int:credit_sale_id>/', views.manage_credit_sale, name='edit_credit_sale'),  # For editing an existing credit sale
    path('delete_credit_sale/<int:credit_sale_id>/', views.delete_credit_sale, name='delete_credit_sale'),
    path('logout/',auth_views.LoginView.as_view(template_name = 'groceryapp/logout.html'),name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name = 'groceryapp/login.html'),name='login'),
    path('home/<int:product_id>/',views.product_detail,name = 'product_detail'),
    path('delete/<int:product_id>/',views.delete_detail,name = 'delete_detail'),
    path('issue_item/<int:pk>/', issue_item, name='issue_item'),
    path('receipt/',views.receipt,name='receipt'),
    path('receipt/<int:receipt_id>/',views.receipt_detail, name='receipt_detail'),
    path('daily_sales/', views.daily_sales, name='daily_sales'), 
    path('edit_sale/<int:sale_id>/', views.edit_sale, name='edit_sale'),
    path('add_stock/', views.add_stock, name='add_stock'),

    path('add_item/<int:pk>/', add_item, name='add_item'),

    



]







