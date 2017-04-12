from django.forms import ModelForm
from .models import Entry, Savings, MonthYear
from django.db.models import Sum
from datetime import datetime
import datetime as dt
import calendar
from django.core.validators import ValidationError
from forex_python.converter import CurrencyRates

today_date = dt.date.today()
cr = CurrencyRates()


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['date', 'euros', 'comments', 'euros_sum', 'xrate', 'dollars_sum', 'daily_savings_dollars', 'daily_savings_display']
        # exclude = ('euros_sum',)
        labels = {'date': 'Date', 'euros': 'Euros Spent', 'xrate': 'Exchange Rate', 'daily_savings_dollars': 'Daily Savings', 'daily_savings_display': 'Convert Savings'}
        help_texts = {'date': 'Enter a date using the following format mm/dd/yyyy.', 'euros': 'Enter the total amount of euros spent.', }

    def clean_date(self):
        date_data = self.cleaned_data['date']
        exist_count = Entry.objects.filter(date=date_data).count()

        if not self.instance.pk:
            if not date_data:
                raise ValidationError('Enter a date')

            elif today_date < date_data:
                raise ValidationError('Invalid date - entry cannot be in the future')

            elif exist_count >= 1:
                raise ValidationError('This entry already exists')

        elif not date_data:
            raise ValidationError('Enter a date')

        elif today_date < date_data:
            raise ValidationError('Invalid date - entry cannot be in the future')

        return date_data

    def clean_euros(self):
        if not self.instance.pk:
            euros_data = self.cleaned_data['euros']
            euros_data_break = euros_data.replace(',', '')
            euros_data_split = euros_data_break.split()
            euros_data_list = [float(a) for a in euros_data_split]
            euros_data_display = (", ".join(repr(e) for e in euros_data_list))

            if not euros_data:
                raise ValidationError('Please enter your receipt totals.')

            return euros_data_display

        else:
            euros_data = self.cleaned_data['euros']
            euros_data_break = euros_data.replace(',', '')
            euros_data_split = euros_data_break.split()
            euros_data_list = [float(a) for a in euros_data_split]
            euros_data_display = (", ".join(repr(e) for e in euros_data_list))

        return euros_data_display

    def clean_euros_sum(self):
        euros_data = self.cleaned_data.get("euros")
        if not euros_data:
            raise ValidationError('Error')
        else:
            euros_data_break = euros_data.replace(',', '')
            euros_data_split = euros_data_break.split()
            euros_data_list = [float(a) for a in euros_data_split]
            daily_spent = sum(euros_data_list)
            euros_sum = "{0:.2f}".format(daily_spent)

        return euros_sum

    def clean_dollars_sum(self):
        euros_data = self.cleaned_data.get("euros")
        xrate_date = self.cleaned_data.get(str("date"))
        if not euros_data:
            raise ValidationError('Error')
        else:
            euros_data_break = euros_data.replace(',', '')
            euros_data_split = euros_data_break.split()
            euros_data_list = [float(a) for a in euros_data_split]
            daily_spent = sum(euros_data_list)
            prior_date_rate = cr.get_rate('EUR', 'USD', xrate_date)
            xrate = prior_date_rate
            dollars_sum = daily_spent * xrate
            dollars_sum_format = "{0:.2f}".format(dollars_sum)

        return dollars_sum_format

    def clean_xrate(self):
        xrate_date = self.cleaned_data.get(str("date"))
        if not xrate_date:
            raise ValidationError('Error')
        else:
            prior_date_rate = cr.get_rate('EUR', 'USD', xrate_date)
            xrate = "{0:.2f}".format(prior_date_rate)

        return xrate

    def clean_daily_savings_dollars(self):
        euros_data = self.cleaned_data.get("euros")
        date_data = self.cleaned_data.get('date')
        exist_count = Entry.objects.filter(date=date_data).count()
        if not self.instance.pk:
            if not date_data:
                raise ValidationError('Enter a date')

            elif today_date < date_data:
                raise ValidationError('Invalid date - entry cannot be in the future')
            elif not euros_data:
                raise ValidationError('*')
            elif exist_count >= 1:
                raise ValidationError('This entry already exists')
            else:
                euros_data_break = euros_data.replace(',', '')
                euros_data_split = euros_data_break.split()
                euros_data_list = [float(a) for a in euros_data_split]
                daily_spent = sum(euros_data_list)
                xrate_date = self.cleaned_data.get(str("date"))
                prior_date_rate = cr.get_rate('EUR', 'USD', xrate_date)
                xrate = prior_date_rate
                if date_data < dt.date(2017, 2, 1):
                    dollars_sum = daily_spent * xrate - 93
                    dollars_sum_format = "{0:.2f}".format(dollars_sum)
                else:
                    dollars_sum = daily_spent * xrate - 87
                    dollars_sum_format = "{0:.2f}".format(dollars_sum)

                return dollars_sum_format
        else:
            euros_data_break = euros_data.replace(',', '')
            euros_data_split = euros_data_break.split()
            euros_data_list = [float(a) for a in euros_data_split]
            daily_spent = sum(euros_data_list)
            xrate_date = self.cleaned_data.get(str("date"))
            prior_date_rate = cr.get_rate('EUR', 'USD', xrate_date)
            xrate = prior_date_rate
            if date_data < dt.date(2017, 2, 1):
                dollars_sum = daily_spent * xrate - 93
                dollars_sum_format = "{0:.2f}".format(dollars_sum)
            else:
                dollars_sum = daily_spent * xrate - 87
                dollars_sum_format = "{0:.2f}".format(dollars_sum)

            return dollars_sum_format

    def clean_daily_savings_display(self):
        euros_data = self.cleaned_data.get("euros")
        date_data = self.cleaned_data.get('date')
        exist_count = Entry.objects.filter(date=date_data).count()
        if not self.instance.pk:
            if not date_data:
                raise ValidationError('Enter a date')

            elif today_date < date_data:
                raise ValidationError('Invalid date - entry cannot be in the future')
            elif not euros_data:
                raise ValidationError('*')
            elif exist_count >= 1:
                raise ValidationError('This entry already exists')
            else:
                euros_data_break = euros_data.replace(',', '')
                euros_data_split = euros_data_break.split()
                euros_data_list = [float(a) for a in euros_data_split]
                daily_spent = sum(euros_data_list)
                xrate_date = self.cleaned_data.get(str("date"))
                prior_date_rate = cr.get_rate('EUR', 'USD', xrate_date)
                xrate = prior_date_rate
                if date_data < dt.date(2017, 2, 1):
                    dollars_sum = daily_spent * xrate - 93
                    absolute = abs(dollars_sum)
                    dollars_sum_format = ("{0:.2f}".format(absolute))
                else:
                    dollars_sum = daily_spent * xrate - 87
                    absolute = abs(dollars_sum)
                    dollars_sum_format = ("{0:.2f}".format(absolute))

                return dollars_sum_format
        else:
            euros_data_break = euros_data.replace(',', '')
            euros_data_split = euros_data_break.split()
            euros_data_list = [float(a) for a in euros_data_split]
            daily_spent = sum(euros_data_list)
            xrate_date = self.cleaned_data.get(str("date"))
            prior_date_rate = cr.get_rate('EUR', 'USD', xrate_date)
            xrate = prior_date_rate
            if date_data < dt.date(2017, 2, 1):
                dollars_sum = daily_spent * xrate - 93
                absolute = abs(dollars_sum)
                dollars_sum_format = ("{0:.2f}".format(absolute))
            else:
                dollars_sum = daily_spent * xrate - 87
                absolute = abs(dollars_sum)
                dollars_sum_format = ("{0:.2f}".format(absolute))

            return dollars_sum_format


class SavingsForm(ModelForm):
    class Meta:
        model = Savings
        fields = ['total_spent_euros', 'total_spent_dollars', 'total_savings', 'total_savings_display']
        # exclude = ('euros_sum',)
        labels = {'total_spent_euros': 'Total €€€ Spending', 'total_spent_dollars': 'Total $$$ Spending', 'total_savings': 'Total $$$ Savings', 'total_savings_display': 'Total $$$ Savings(ABS)'}
        # help_texts = {'date': 'Enter a date using the following format mm/dd/yyyy.', 'euros': 'Enter the total amount of euros spent.', }

    def clean_total_spent_euros(self):
        sum_euros = Entry.objects.aggregate(s=Sum('euros_sum')).get('s')
        sum_format = "{0:.2f}".format(sum_euros)

        return sum_format

    def clean_total_spent_dollars(self):
        sum_dollars = Entry.objects.aggregate(s=Sum('dollars_sum')).get('s')
        sum_formats = "{0:.2f}".format(sum_dollars)

        return sum_formats

    def clean_total_savings(self):
        sum_savings = Entry.objects.aggregate(s=Sum('daily_savings_dollars')).get('s')
        sum_format = "{0:.2f}".format(sum_savings)

        return sum_format

    def clean_total_savings_display(self):
        sum_savings = Entry.objects.aggregate(s=Sum('daily_savings_dollars')).get('s')
        absolute = abs(sum_savings)
        sum_format = "{0:.2f}".format(absolute)

        return sum_format


class MonthYearForm(ModelForm):
    class Meta:
        model = MonthYear
        fields = ['month', 'year', 'total_spent_euros', 'total_spent_dollars', 'total_savings', 'total_savings_display']
        # exclude =
        labels = {'month': 'Month', 'year': 'Year', 'total_spent_euros': 'Total €€€ Spending', 'total_spent_dollars': 'Total $$$ Spending', 'total_savings': 'Total $$$ Savings', 'total_savings_display': 'Total $$$ Savings(ABS)'}
        # help_texts =

    def clean_year(self):
        # 2016
        # edate = datetime.strptime('1/1/2016', '%m/%d/%Y')

        # 2017
        edate = datetime.strptime('1/1/2017', '%m/%d/%Y')

        year = edate.year

        return year

    def clean_month(self):
        # January
        # jan = datetime.strptime('1/1/2016', '%m/%d/%Y')
        # month = calendar.month_name[jan.month]

        # February
        # feb = datetime.strptime('2/1/2016', '%m/%d/%Y')
        # month = calendar.month_name[feb.month]

        # March
        mar = datetime.strptime('3/1/2016', '%m/%d/%Y')
        month = calendar.month_name[mar.month]

        # April
        # apr = datetime.strptime('4/1/2016', '%m/%d/%Y')
        # month = calendar.month_name[apr.month]

        # May
        # may = datetime.strptime('5/1/2016', '%m/%d/%Y')
        # month = calendar.month_name[may.month]

        # June
        # june = datetime.strptime('6/1/2016', '%m/%d/%Y')
        # month = calendar.month_name[june.month]

        # July
        # july = datetime.strptime('7/1/2016', '%m/%d/%Y')
        # month = calendar.month_name[july.month]

        # August
        # aug = datetime.strptime('8/1/2016', '%m/%d/%Y')
        # month = calendar.month_name[aug.month]

        # September
        # sept = datetime.strptime('9/1/2016', '%m/%d/%Y')
        # month = calendar.month_name[sept.month]

        # October
        # oct = datetime.strptime('10/1/2016', '%m/%d/%Y')
        # month = calendar.month_name[oct.month]

        # November
        # nov = datetime.strptime('11/1/2016', '%m/%d/%Y')
        # month = calendar.month_name[nov.month]

        # December
        # dec = datetime.strptime('12/1/2016', '%m/%d/%Y')
        # month = calendar.month_name[dec.month]

        return month

    def clean_total_spent_euros(self):

        # January
        # sum_euros = Entry.objects.filter(date__range=('2017-1-1', '2017-1-31')).aggregate(s=Sum('euros_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_euros)

        # February17
        # sum_euros = Entry.objects.filter(date__range=('2017-2-1', '2017-2-28')).aggregate(s=Sum('euros_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_euros)

        # March
        sum_euros = Entry.objects.filter(date__range=('2017-3-1', '2017-3-31')).aggregate(s=Sum('euros_sum')).get('s')
        sum_format = "{0:.2f}".format(sum_euros)

        # April
        # sum_euros = Entry.objects.filter(date__range=('2017-4-1', '2017-4-30')).aggregate(s=Sum('euros_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_euros)

        # May
        # sum_euros = Entry.objects.filter(date__range=('2017-5-1', '2017-5-31')).aggregate(s=Sum('euros_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_euros)

        # June
        # sum_euros = Entry.objects.filter(date__range=('2017-6-1', '2017-6-31')).aggregate(s=Sum('euros_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_euros)

        # July
        # sum_euros = Entry.objects.filter(date__range=('2017-7-1', '2017-7-31')).aggregate(s=Sum('euros_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_euros)

        # August
        # sum_euros = Entry.objects.filter(date__range=('2017-8-1', '2017-8-31')).aggregate(s=Sum('euros_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_euros)

        # September
        # sum_euros = Entry.objects.filter(date__range=('2017-9-1', '2017-9-30')).aggregate(s=Sum('euros_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_euros)

        # October
        # sum_euros = Entry.objects.filter(date__range=('2017-10-1', '2017-10-31')).aggregate(s=Sum('euros_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_euros)

        # November
        # sum_euros = Entry.objects.filter(date__range=('2016-11-1', '2016-11-30')).aggregate(s=Sum('euros_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_euros)

        # December
        # sum_euros = Entry.objects.filter(date__range=('2016-12-1', '2016-12-31')).aggregate(s=Sum('euros_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_euros)

        return sum_format

    def clean_total_spent_dollars(self):

        # January
        # sum_dollars = Entry.objects.filter(date__range=('2017-1-1', '2017-1-31')).aggregate(s=Sum('dollars_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_dollars)

        # February17
        # sum_dollars = Entry.objects.filter(date__range=('2017-2-1', '2017-2-28')).aggregate(s=Sum('dollars_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_dollars)

        # March
        sum_dollars = Entry.objects.filter(date__range=('2017-3-1', '2017-3-31')).aggregate(s=Sum('dollars_sum')).get('s')
        sum_format = "{0:.2f}".format(sum_dollars)

        # April
        # sum_dollars = Entry.objects.filter(date__range=('2017-4-1', '2017-4-30')).aggregate(s=Sum('dollars_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_dollars)

        # May
        # sum_dollars = Entry.objects.filter(date__range=('2017-5-1', '2017-5-31')).aggregate(s=Sum('dollars_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_dollars)

        # June
        # sum_dollars = Entry.objects.filter(date__range=('2017-6-1', '2017-6-31')).aggregate(s=Sum('dollars_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_dollars)

        # July
        # sum_dollars = Entry.objects.filter(date__range=('2017-7-1', '2017-7-31')).aggregate(s=Sum('dollars_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_dollars)

        # August
        # sum_dollars = Entry.objects.filter(date__range=('2017-8-1', '2017-8-31')).aggregate(s=Sum('dollars_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_dollars)

        # September
        # sum_dollars = Entry.objects.filter(date__range=('2017-9-1', '2017-9-30')).aggregate(s=Sum('dollars_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_dollars)

        # October
        # sum_dollars = Entry.objects.filter(date__range=('2017-10-1', '2017-10-31')).aggregate(s=Sum('dollars_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_dollars)

        # November
        # sum_dollars = Entry.objects.filter(date__range=('2016-11-1', '2016-11-30')).aggregate(s=Sum('dollars_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_dollars)

        # December
        # sum_dollars = Entry.objects.filter(date__range=('2016-12-1', '2016-12-31')).aggregate(s=Sum('dollars_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_dollars)

        return sum_format

    def clean_total_savings(self):

        # January
        # sum_savings = Entry.objects.filter(date__range=('2017-1-1', '2017-1-31')).aggregate(s=Sum('daily_savings_dollars')).get('s')
        # sum_format = "{0:.2f}".format(sum_savings)

        # February17
        # sum_savings = Entry.objects.filter(date__range=('2017-2-1', '2017-2-28')).aggregate(s=Sum('daily_savings_dollars')).get('s')
        # sum_format = "{0:.2f}".format(sum_savings)

        # March
        sum_savings = Entry.objects.filter(date__range=('2017-3-1', '2017-3-31')).aggregate(s=Sum('daily_savings_dollars')).get('s')
        sum_format = "{0:.2f}".format(sum_savings)

        # April
        # sum_savings = Entry.objects.filter(date__range=('2017-4-1', '2017-4-30')).aggregate(s=Sum('daily_savings_dollars')).get('s')
        # sum_format = "{0:.2f}".format(sum_savings)

        # May
        # sum_savings = Entry.objects.filter(date__range=('2017-5-1', '2017-5-31')).aggregate(s=Sum('daily_savings_dollars')).get('s')
        # sum_format = "{0:.2f}".format(sum_savings)

        # June
        # sum_savings = Entry.objects.filter(date__range=('2017-6-1', '2017-6-31')).aggregate(s=Sum('daily_savings_dollars')).get('s')
        # sum_format = "{0:.2f}".format(sum_savings)

        # July
        # sum_savings = Entry.objects.filter(date__range=('2017-7-1', '2017-7-31')).aggregate(s=Sum('daily_savings_dollars')).get('s')
        # sum_format = "{0:.2f}".format(sum_savings)

        # August
        # sum_savings = Entry.objects.filter(date__range=('2017-8-1', '2017-8-31')).aggregate(s=Sum('daily_savings_dollars')).get('s')
        # sum_format = "{0:.2f}".format(sum_savings)

        # September
        # sum_savings = Entry.objects.filter(date__range=('2017-9-1', '2017-9-30')).aggregate(s=Sum('daily_savings_dollars')).get('s')
        # sum_format = "{0:.2f}".format(sum_savings)

        # October
        # sum_savings = Entry.objects.filter(date__range=('2017-10-1', '2017-10-31')).aggregate(s=Sum('daily_savings_dollars')).get('s')
        # sum_format = "{0:.2f}".format(sum_savings)

        # November
        # sum_savings = Entry.objects.filter(date__range=('2016-11-1', '2016-11-30')).aggregate(s=Sum('daily_savings_dollars')).get('s')
        # sum_format = "{0:.2f}".format(sum_savings)

        # December
        # sum_savings = Entry.objects.filter(date__range=('2016-12-1', '2016-12-31')).aggregate(s=Sum('daily_savings_dollars')).get('s')
        # sum_format = "{0:.2f}".format(sum_savings)

        return sum_format

    def clean_total_savings_display(self):

        # January
        # sum_savings = Entry.objects.filter(date__range=('2017-1-1', '2017-1-31')).aggregate(s=Sum('daily_savings_dollars')).get('s')
        # absolute = abs(sum_savings)
        # sum_format = "{0:.2f}".format(absolute)

        # February17
        # sum_savings = Entry.objects.filter(date__range=('2017-2-1', '2017-2-28')).aggregate(s=Sum('daily_savings_dollars')).get('s')
        # absolute = abs(sum_savings)
        # sum_format = "{0:.2f}".format(absolute)

        # March
        # sum_savings = Entry.objects.filter(date__range=('2017-3-1', '2017-3-31')).aggregate(s=Sum('daily_savings_dollars')).get('s')
        # absolute = abs(sum_savings)
        # sum_format = "{0:.2f}".format(absolute)

        # April
        # sum_savings = Entry.objects.filter(date__range=('2017-4-1', '2017-4-30')).aggregate(s=Sum('daily_savings_dollars')).get('s')
        # absolute = abs(sum_savings)
        # sum_format = "{0:.2f}".format(absolute)

        # May
        # sum_savings = Entry.objects.filter(date__range=('2017-5-1', '2017-5-31')).aggregate(s=Sum('daily_savings_dollars')).get('s')
        # absolute = abs(sum_savings)
        # sum_format = "{0:.2f}".format(absolute)

        # June
        # sum_savings = Entry.objects.filter(date__range=('2017-6-1', '2017-6-31')).aggregate(s=Sum('daily_savings_dollars')).get('s')
        # absolute = abs(sum_savings)
        # sum_format = "{0:.2f}".format(absolute)

        # July
        # sum_savings = Entry.objects.filter(date__range=('2017-7-1', '2017-7-31')).aggregate(s=Sum('daily_savings_dollars')).get('s')
        # absolute = abs(sum_savings)
        # sum_format = "{0:.2f}".format(absolute)

        # August
        # sum_savings = Entry.objects.filter(date__range=('2017-8-1', '2017-8-31')).aggregate(s=Sum('daily_savings_dollars')).get('s')
        # absolute = abs(sum_savings)
        # sum_format = "{0:.2f}".format(absolute)

        # September
        # sum_savings = Entry.objects.filter(date__range=('2017-9-1', '2017-9-30')).aggregate(s=Sum('daily_savings_dollars')).get('s')
        # absolute = abs(sum_savings)
        # sum_format = "{0:.2f}".format(absolute)

        # October
        # sum_savings = Entry.objects.filter(date__range=('2017-10-1', '2017-10-31')).aggregate(s=Sum('daily_savings_dollars')).get('s')
        # absolute = abs(sum_savings)
        # sum_format = "{0:.2f}".format(absolute)

        # November
        # sum_savings = Entry.objects.filter(date__range=('2016-11-1', '2016-11-30')).aggregate(s=Sum('daily_savings_dollars')).get('s')
        # absolute = abs(sum_savings)
        # sum_format = "{0:.2f}".format(absolute)

        # December
        # sum_savings = Entry.objects.filter(date__range=('2016-12-1', '2016-12-31')).aggregate(s=Sum('daily_savings_dollars')).get('s')
        # absolute = abs(sum_savings)
        # sum_format = "{0:.2f}".format(absolute)

        return sum_format

