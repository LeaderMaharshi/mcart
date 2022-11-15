from django.shortcuts import render
from store.models import Product

def home(request):
    popular_products = Product.objects.all().filter(is_available=True)[:4]
    new_arrives = Product.objects.all().order_by('-created_date')[:4]
    recommended_products = Product.objects.all().filter(is_available=True)[:4]
    
    context = {
        'popular_products': popular_products,
        'new_arrives': new_arrives,
        'recommended_products': recommended_products,
    }
    
    return render(request, 'home.html', context)