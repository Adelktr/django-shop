from django.urls import path
from . import views

app_name = "shop"
urlpatterns = [
    path('', views.index, name="index"),
    path('create', views.create, name="create"),
    path('<id>', views.show, name="show" ),
    path('update/<id>', views.update, name="update" ),
    path('delete/<id>', views.delete, name="delete" ),
]