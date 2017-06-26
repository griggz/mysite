from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class Entry(models.Model):
    CURRENCY_CHOICES = (
        ('EUR', '(EUR) Euro'),
        ('USD', '(USD) US Dollar'),
        ('GBP', '(GBP) United Kingdom Pound'),
        ('CZK', '(CZK) Czech Republic Koruna'),
        ('HUF', '(HUF) Hungary Forint'),
        ('CHF', '(CHF) Swiss Franc'),
    )
    date = models.DateField(blank=True, null=True)
    spending = models.CharField(max_length=500, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    spending_sum = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=900, blank=True, null=True, choices=CURRENCY_CHOICES)
    xrate = models.DecimalField(max_digits=9, decimal_places=4, blank=True, null=True,)
    dollars_sum = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    daily_savings_dollars = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    daily_savings_display = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('argent:detail', kwargs={'pk': self.pk})

    def item_date(self):
        row_title = self.date
        return row_title

    class Meta:

        ordering = ['-date']


class Savings(models.Model):
    total_spent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    total_spent_dollars = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    total_savings = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    total_savings_display = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('argent:detail', kwargs={'pk': self.pk})


class MonthYear(models.Model):
    month = models.CharField(max_length=500, blank=True, null=True)
    year = models.CharField(max_length=500, blank=True, null=True)
    total_spent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    total_spent_dollars = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    total_savings = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    total_savings_display = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('argent:detail', kwargs={'pk': self.pk})