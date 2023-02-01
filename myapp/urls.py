from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('allemp/', views.allEmp, name="allemp"),
    path('addemppage/', views.addEmpPage, name="addemppage"),
    path('addemp/', views.addEmp, name="addemp"),
    path('remove/', views.removeEmp, name="remove"),
    path('remove/<int:pk>', views.removeEmp, name="removeemp"),
    path('filter/', views.filterEmp, name="filter"),
]