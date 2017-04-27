from django.contrib import admin
from .forms import EntryForm, SavingsForm, MonthYearForm
from .models import Entry, Savings, MonthYear


# Register your models here.


class EntryFormAdmin(admin.ModelAdmin):
    list_display = ["date", "spending", "spending_sum", "daily_savings_display", "currency", "xrate"]
    form = EntryForm
    ordering = ['-date']

admin.site.register(Entry, EntryFormAdmin)

# class Meta:
#     model = Entry
#     fields = ['date', 'spending', 'comments']
#     labels = {'date': 'Date', 'spending': 'spending Spent', }
#     help_texts = {'date': 'Enter a date using the following format mm/dd/yyyy (default 3).', 'spending': 'enter the amount of spending spent(default 3).', }


class SavingsFormAdmin(admin.ModelAdmin):
    list_display = ["id", "total_spent", "total_spent_dollars", "total_savings", "total_savings_display"]
    form = SavingsForm


admin.site.register(Savings, SavingsFormAdmin)


class MonthYearFormAdmin(admin.ModelAdmin):
    list_display = ["month", "year", "total_spent", "total_spent_dollars", "total_savings", "total_savings_display"]
    form = MonthYearForm

admin.site.register(MonthYear, MonthYearFormAdmin)