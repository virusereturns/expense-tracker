from django.views.generic import CreateView, ListView
from .models import Expense
from .forms import ExpenseForm
from django.urls import reverse_lazy
from expenses.utils import get_local_today
from django.db.models import Sum


class ExpenseCreateView(CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expenses/expense_form.html'
    success_url = reverse_lazy('expenses:expense_list')  # You can later change this

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        return super().form_valid(form)


class ExpenseListView(ListView):
    model = Expense
    template_name = 'expenses/expense_list.html'
    context_object_name = 'expenses'

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        filter_by = self.request.GET.get('filter', 'this_month')  # default to this_month

        today = get_local_today()

        if filter_by == 'today':
            queryset = queryset.filter(date=today)
        elif filter_by == 'this_month':
            queryset = queryset.filter(date__year=today.year, date__month=today.month)
        else:
            queryset = queryset  # no extra filter for 'all'

        return queryset.order_by('-date', '-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        filter_by = self.request.GET.get('filter', 'this_month')
        context['filter_by'] = filter_by

        expenses_queryset = self.get_queryset()

        # Dynamic summary by big (parent) categories
        big_category_summaries = []

        # Find all parent categories for the user
        parent_categories = self.request.user.category_set.filter(parent__isnull=True).order_by('name')

        for parent in parent_categories:
            # Sum all expenses where the expense.category.parent == this parent
            total = (
                expenses_queryset.filter(category__parent=parent).aggregate(total_amount=Sum('amount'))[
                    'total_amount'
                ]
                or 0
            )
            big_category_summaries.append(
                {
                    'name': parent.name,
                    'total': total,
                }
            )

        context['big_category_summaries'] = big_category_summaries

        return context
