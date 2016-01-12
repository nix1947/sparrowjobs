from django.contrib import admin
from .models import Address
from companies.models import Company


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
	list_display = ['country', 'state']
	search_fields = ['country']

