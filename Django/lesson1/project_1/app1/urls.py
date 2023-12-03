from django.urls import path
from .import views

urlpatterns = [
    path('', views.main),
    path('items', views.show_all, name='items'),  # метод из views.py  корректировали 02.11.2023
    path('items_admin', views.show_all_admin, name='items_admin'),
    path('items/<int:item_id>', views.show_item, name='item'),  # Это добавили. Если используем items/<int:item_id>, то будем происходить
    # редирект на какой-то определенный url.
    path('update_item/<int:item_id>', views.update_item, name='update_item'),
    path('delete_item/<int:item_id>', views.delete_item, name='delete_item'),
    path('login', views.login, name='login'),
    path('logout', views.delete_item, name='logout'),
    path('register', views.SignUp.as_view(), name='register'),
]
