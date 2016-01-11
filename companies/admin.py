from django.contrib import admin
from .models import Company, Industry

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
	list_filter = ('name', )
	list_display = ('name', 'company_size',)
	search_fields = ('name',)


@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
	list_display = ('name',)
	list_display = ('name',)
	search_fields = ('name',)

