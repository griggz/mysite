from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class Entry(models.Model):
    date = models.DateField(blank=True, null=True,)
    euros = models.CharField(max_length=500, blank=True, null=True)
    comments = models.CharField(max_length=900, blank=True, null=True)
    euros_sum = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    xrate = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    dollars_sum = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    daily_savings_dollars = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    daily_savings_display = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('argent:detail', kwargs={'pk': self.pk})

    # def item_date(self):
    #     row_title = self.date
    #     return row_title

    # class Meta:
    #
    #     ordering = ['date']


class Savings(models.Model):
    total_spent_euros = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    total_spent_dollars = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    total_savings = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    total_savings_display = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('argent:detail', kwargs={'pk': self.pk})


class MonthYear(models.Model):
    month = models.CharField(max_length=500, blank=True, null=True)
    year = models.CharField(max_length=500, blank=True, null=True)
    total_spent_euros = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    total_spent_dollars = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    total_savings = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    total_savings_display = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('argent:detail', kwargs={'pk': self.pk})