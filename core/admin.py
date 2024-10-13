from django.contrib import admin
from .models import City, Category, Landmark, Hotel, Restaurant

admin.site.register(City)
admin.site.register(Category)
admin.site.register(Landmark)
admin.site.register(Hotel)
admin.site.register(Restaurant)
