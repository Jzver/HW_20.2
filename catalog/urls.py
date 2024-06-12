from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomeView, ProductsListView, ProductDetailView, ContactsView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductsListView.as_view(), name='products_list'),
    path("products/<int:pk>/", ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', ContactsView.as_view(), name='contacts')
]

