from django.urls import path

from . import views

urlpatterns = [
    path("", views.units_collections, name="units_collections"),
    path("<int:unit_id>/", views.unit_detail, name="unit_detail"),
]
