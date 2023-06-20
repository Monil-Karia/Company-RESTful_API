from django.contrib import admin
from api.models import Company, Employee

# Customizing the display and search fields for the Company model in the admin interface
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'type')  # Display these fields in the list view
    search_fields = ('name', 'location',)  # Enable searching based on these fields

# Customizing the display and filter options for the Employee model in the admin interface
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company')  # Display these fields in the list view
    list_filter = ('company',)  # Enable filtering based on the 'company' field

# Registering the models and their respective admin customization
admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
