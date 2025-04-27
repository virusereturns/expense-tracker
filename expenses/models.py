from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        # Show parent -> child nicely if parent exists
        if self.parent:
            return f"{self.parent.name} -> {self.name}"
        return self.name

    class Meta:
        unique_together = ('user', 'name', 'parent')
        ordering = ['parent__name', 'name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount} {self.category}"

    class Meta:
        ordering = ['-date', '-created_at']
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'
