from django.contrib import admin
from expenses.models import Category, Expense


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('amount', 'category', 'date', 'created_at')
