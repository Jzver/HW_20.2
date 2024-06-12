from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView
from catalog.models import Product
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


# Для простой страницы без контекста
class HomeView(TemplateView):
    template_name = 'home.html'


# Для списка продуктов
class ProductsListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products_list.html'
    queryset = Product.objects.all().select_related('category')


# Для детального просмотра продукта
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


# Для контактной формы
class ContactsView(FormView):
    template_name = 'contacts.html'
    success_url = '/thanks/'  # Укажите URL для перенаправления после успешной отправки

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}) написал: {message}')
        return HttpResponse('Сообщение отправлено')  # Или перенаправление на другую страницу
