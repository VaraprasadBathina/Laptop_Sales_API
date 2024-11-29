from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from django.http import JsonResponse
from django.db.models import Sum
from .models import SalesData

def state_wise_sales(request):
    data = (
        SalesData.objects.values('state')  # Group by 'state'
        .annotate(total_sales=Sum('sale_amount'))  # Sum 'sale_amount'
        .order_by('state')  # Optionally order by state
    )
    return JsonResponse(list(data), safe=False)
def brand_wise_sales(request):
    data = (
        SalesData.objects.values('product') # Group by 'product'
        .annotate(total_sales=Sum('sale_amount'))  # Sum 'sale_amount'
        .order_by('product')  # Optionally order by product
    )
    return JsonResponse(list(data), safe=False)


