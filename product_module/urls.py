from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
    path('brand/<brand>', views.ProductListView.as_view(), name='product-brands-list'),
    path('cat/<cat>',views.ProductListView.as_view(),name='product-categories-list'),
    path('product-favorite', views.AddProductFavorite.as_view(), name='product-favorite'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product-detail'),
]
