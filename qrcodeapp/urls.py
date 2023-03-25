from django.urls import path
from . import views

urlpatterns = [
    path('qr_gen/', views.qr_gen, name="qr_gen"),
]
