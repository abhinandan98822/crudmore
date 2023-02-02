from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.RegisterView,name='register'),
    path('table/',views.Table,name='table'),
    path('edit/<int:id>',views.Edit,name='edit'),
    path('update/<int:id>',views.Update,name='update'),
    path('delete/<int:id>',views.Delete,name='delete'),
    path('search',views.Search,name='search'),
]