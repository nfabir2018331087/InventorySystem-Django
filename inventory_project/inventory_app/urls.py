from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('create/', views.product_create_view, name="create_product"),
    path('products/', views.products_view, name="products"),
    path('update/<int:product_id>/', views.product_update_view, name="update_product"),
    path('delete/<int:product_id>/', views.product_delete_view, name="delete_product"),
    path('contact/', views.contact_view, name="contact"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]