from django.contrib import admin
from .forms import EntryForm, SavingsForm, MonthYearForm
from .models import Entry, Savings, MonthYear


# Register your models here.


class EntryFormAdmin(admin.ModelAdmin):
    list_display = ["date", "euros", "euros_sum", "daily_savings_display"]
    form = EntryForm
    ordering = ['-date']

admin.site.register(Entry, EntryFormAdmin)

# class Meta:
#     model = Entry
#     fields = ['date', 'euros', 'comments']
#     labels = {'date': 'Date', 'euros': 'Euros Spent', }
#     help_texts = {'date': 'Enter a date using the following format mm/dd/yyyy (default 3).', 'euros': 'enter the amount of euros spent(default 3).', }


class SavingsFormAdmin(admin.ModelAdmin):
    list_display = ["total_spent_euros", "total_spent_dollars", "total_savings", "total_savings_display"]
    form = SavingsForm


admin.site.register(Savings, SavingsFormAdmin)


class MonthYearFormAdmin(admin.ModelAdmin):
    list_display = ["month", "year", "total_spent_euros", "total_spent_dollars", "total_savings", "total_savings_display"]
    form = MonthYearForm

admin.site.register(MonthYear, MonthYearFormAdmin)