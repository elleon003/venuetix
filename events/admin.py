from django.contrib import admin
from .models import Category, Event

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'price',
        'date',
        'start_time',
        'end_time',
        'available',
        'created',
        'updated',
    ]
    list_filter = ['available', 'created', 'updated', 'date']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name','date')}