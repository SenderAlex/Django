from django.contrib import admin
from .models import Mebel  # это добавили

# Register your models here.
admin.site.register(Mebel)  # Этот код импортирует модель Mebel и затем вызывает admin.site.register для ее регистрации.
