from multiprocessing.resource_tracker import register

from django.contrib import admin
from .models import Candy, Supplier

# Register your models here.

class SupplierAdmin(admin.ModelAdmin):

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser


class CandyAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return obj and obj.supplier.user == request.user

    def has_view_permission(self, request, obj=None):
        return True

admin.site.register(Candy)
admin.site.register(Supplier)