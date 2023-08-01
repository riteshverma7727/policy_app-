from django.contrib import admin
from .models import Policy

class PolicyAdmin(admin.ModelAdmin):
    list_display = ('application_number', 'customer_name', 'policy_status', 'date_of_birth', 'policy_cover')
    list_filter = ('policy_status', 'date_of_birth')
    search_fields = ('application_number', 'customer_name', 'email', 'phone_number')

admin.site.register(Policy, PolicyAdmin)
