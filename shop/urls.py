from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    # Shop URL patterns

    # All products
    path('', views.product_list, name='product_list'),

    # All products filtered by category
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),

    # Single product by id
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
