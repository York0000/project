from django.contrib import admin

from contact.models import ContactModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email']
    list_display = ['name', 'email']
    list_filter = ['name', 'email']
