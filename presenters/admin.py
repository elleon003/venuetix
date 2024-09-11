from django.contrib import admin
from .models import Presenter


@admin.register(Presenter)
class PresenterAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'website')
    list_filter = ('name',)
    search_fields = ('user__email', 'name')
    prepopulated_fields = {'slug': ('name', )}
