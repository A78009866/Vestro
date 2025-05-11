from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('order/<int:product_id>/', views.create_order, name='create_order'),
    path('order/success/', views.order_success, name='order_success'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-product/', views.add_product, name='add_product'),
    path('edit-product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('toggle-product/<int:product_id>/', views.toggle_product, name='toggle_product'),
    path('confirm-order/<int:order_id>/', views.confirm_order, name='confirm_order'),
    path('login/', auth_views.LoginView.as_view(template_name='store/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
]