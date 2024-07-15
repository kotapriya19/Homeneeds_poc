
from django.shortcuts import render, redirect
from .models import Expense, Category
from .forms import ExpenseForm,MonthYearForm
from django.db.models import Sum
import datetime

def index(request):
    expenses = Expense.objects.all()
    return render(request, 'index.html', {'expenses': expenses})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)  # Print form errors in the console
    else:
        form = ExpenseForm()
    return render(request, 'gerocery.html', {'form': form})
      
def monthly_summary(request):
    today = datetime.date.today()
    current_month = today.month
    current_year = today.year

    if request.method == 'POST':
        form = MonthYearForm(request.POST)
        if form.is_valid():
            month = form.cleaned_data['month']
            year = form.cleaned_data['year']
        else:
            month = current_month
            year = current_year
    else:
        form = MonthYearForm(initial={'month': current_month, 'year': current_year})
        month = current_month
        year = current_year

    first_day_of_month = datetime.date(year, month, 1)
    last_day_of_month = (first_day_of_month + datetime.timedelta(days=32)).replace(day=1) - datetime.timedelta(days=1)
    
    expenses = Expense.objects.filter(date__gte=first_day_of_month, date__lte=last_day_of_month)
    total_amount = expenses.aggregate(total=Sum('amount'))['total'] or 0
    
    return render(request, 'monthly.html', {'form': form, 'expenses': expenses, 'total_amount': total_amount})

