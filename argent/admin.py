from django.contrib import admin
from .forms import CountryForm, CityForm, EntryForm, SavingsForm, MonthYearForm
from .models import Entry, Savings, MonthYear, Country, City


# Register your models here.


class EntryFormAdmin(admin.ModelAdmin):
    list_display = ["date", "city", "spending", "spending_sum", "daily_savings_display", "currency", "xrate"]
    form = EntryForm
    ordering = ['-date']


admin.site.register(Entry, EntryFormAdmin)


class CountryFormAdmin(admin.ModelAdmin):
    list_display = ["id", "country"]
    form = CountryForm


admin.site.register(Country, CountryFormAdmin)


class CityFormAdmin(admin.ModelAdmin):
    list_display = ["id", "city", "country"]
    form = CityForm


admin.site.register(City, CityFormAdmin)


class SavingsFormAdmin(admin.ModelAdmin):
    list_display = ["id", "total_spent", "total_spent_dollars", "total_savings", "total_savings_display"]
    form = SavingsForm


admin.site.register(Savings, SavingsFormAdmin)


class MonthYearFormAdmin(admin.ModelAdmin):
    list_display = ["month", "year", "total_spent", "total_spent_dollars", "total_savings", "total_savings_display"]
    form = MonthYearForm


admin.site.register(MonthYear, MonthYearFormAdmin)
