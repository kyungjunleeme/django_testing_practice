from products import views
from django.urls import path

app_name = "products"

urlpatterns = [
    path("<int:pk>/", views.product_detail, name="product_detail"),
]
