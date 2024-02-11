from django.contrib import admin
from .models import Page, Category

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')  # Ensure this order matches

admin.site.register(Category)
admin.site.register(Page, PageAdmin)
