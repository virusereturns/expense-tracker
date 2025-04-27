from django import forms
from expenses.models import Expense, Category
from expenses.utils import get_local_today


class ExpenseForm(forms.ModelForm):
    parent_category = forms.ModelChoiceField(
        queryset=Category.objects.filter(parent__isnull=True),
        required=True,
        label="Big Category"
    )
    category_name = forms.CharField(max_length=100, required=True, label="Specific Category")

    class Meta:
        model = Expense
        fields = ['amount', 'description', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

        self.fields['date'].initial = get_local_today()

        # Filter parent categories to only this user's categories
        self.fields['parent_category'].queryset = Category.objects.filter(user=self.user, parent__isnull=True)

    def save(self, commit=True):
        expense = super().save(commit=False)

        parent = self.cleaned_data['parent_category']
        category_name = self.cleaned_data['category_name'].strip()

        # Try to find existing child category
        category, created = Category.objects.get_or_create(
            user=self.user,
            name=category_name,
            parent=parent,
        )

        expense.user = self.user
        expense.category = category

        if commit:
            expense.save()
        return expense
