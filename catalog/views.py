from django.shortcuts import render, get_object_or_404

from catalog.models import Product


# Create your views here.

def home(request):
    return render(request, 'home.html')


def products_list(request):
    # Если есть связанные модели, используйте select_related или prefetch_related
    products = Product.objects.all().select_related('category')
    context = {"products": products}
    return render(request, "products_list.html", context)



def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, "product_detail.html", context)


# Задание 19.1
def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}) написал: {message}')
    return render(request, "contacts.html")