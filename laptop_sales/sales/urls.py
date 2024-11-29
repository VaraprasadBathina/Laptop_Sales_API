from django.urls import path
from . import views

urlpatterns = [
    path('state-wise/', views.state_wise_sales, name='state_wise_sales'),
    path('brand-wise/', views.brand_wise_sales, name='brand_wise_sales'),
]
