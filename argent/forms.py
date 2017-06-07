from django.forms import ModelForm, HiddenInput
from .models import Entry, Savings, MonthYear
from django.db.models import Sum
from datetime import datetime
import datetime as dt
from django.core.validators import ValidationError
from forex_python.converter import CurrencyRates
import calendar


cr = CurrencyRates()


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        widgets = {'dollars_sum': HiddenInput(), 'xrate': HiddenInput, 'daily_savings_dollars': HiddenInput, 'daily_savings_display': HiddenInput, 'spending_sum': HiddenInput}
        fields = ['date', 'spending', 'currency', 'comments', 'spending_sum', 'xrate', 'dollars_sum', 'daily_savings_dollars', 'daily_savings_display']
        # exclude = ('spending_sum',)
        labels = {'date': 'Date', 'spending': 'Spending', 'xrate': 'Exchange Rate', 'daily_savings_dollars': 'Daily Savings', 'daily_savings_display': 'Convert Savings'}
        help_texts = {'date': 'Enter the date of spending.', 'spending': 'Enter your receipts/spending.', 'currency': 'Select the currency used when spending.'}

    def clean_date(self):
        today_date = dt.date.today()
        date_data = self.cleaned_data['date']
        exist_count = Entry.objects.filter(date=date_data).count()

        if not self.instance.pk:
            if not date_data:
                raise ValidationError('Enter a date')

            elif date_data > today_date:
                raise ValidationError('Invalid date - entry cannot be in the future')

            elif exist_count >= 1:
                raise ValidationError('This entry already exists')

        elif not date_data:
            raise ValidationError('Enter a date')

        elif date_data > today_date:
            raise ValidationError('Invalid date - entry cannot be in the future')

        return date_data

    def clean_spending(self):
        if not self.instance.pk:
            spending_data = self.cleaned_data['spending']
            spending_data_break = spending_data.replace(',', '')
            spending_data_split = spending_data_break.split()
            spending_data_list = [float(a) for a in spending_data_split]
            spending_data_display = (", ".join(repr(e) for e in spending_data_list))

            if not spending_data:
                raise ValidationError('Please enter your receipt totals.')

            return spending_data_display

        else:
            spending_data = self.cleaned_data['spending']
            spending_data_break = spending_data.replace(',', '')
            spending_data_split = spending_data_break.split()
            spending_data_list = [float(a) for a in spending_data_split]
            spending_data_display = (", ".join(repr(e) for e in spending_data_list))

        return spending_data_display

    def clean_spending_sum(self):
        spending_data = self.cleaned_data.get("spending")
        if not spending_data:
            raise ValidationError('Error')
        else:
            spending_data_break = spending_data.replace(',', '')
            spending_data_split = spending_data_break.split()
            spending_data_list = [float(a) for a in spending_data_split]
            daily_spent = sum(spending_data_list)
            spending_sum = "{0:.2f}".format(daily_spent)

        return spending_sum

    def clean_dollars_sum(self):
        spending_data = self.cleaned_data.get("spending")
        xrate_date = self.cleaned_data.get(str("date"))
        currency = self.cleaned_data.get("currency")
        curr = currency
        if not spending_data:
            raise ValidationError('Error')
        elif curr == 'USD':
            spending_data_break = spending_data.replace(',', '')
            spending_data_split = spending_data_break.split()
            spending_data_list = [float(a) for a in spending_data_split]
            daily_spent = sum(spending_data_list)
            dollars_sum_format = "{0:.2f}".format(daily_spent)

        else:
            spending_data_break = spending_data.replace(',', '')
            spending_data_split = spending_data_break.split()
            spending_data_list = [float(a) for a in spending_data_split]
            daily_spent = sum(spending_data_list)
            prior_date_rate = cr.get_rate(curr, 'USD', xrate_date)
            xrate = prior_date_rate
            dollars_sum = daily_spent * xrate
            dollars_sum_format = "{0:.2f}".format(dollars_sum)

        return dollars_sum_format

    def clean_currency(self):
        currency = self.cleaned_data.get("currency")
        if not currency:
            raise ValidationError('Please select a currency')

        return currency

    def clean_xrate(self):
        xrate_date = self.cleaned_data.get(str("date"))
        currency = self.cleaned_data.get("currency")
        curr = currency
        if not xrate_date:
            raise ValidationError('Error')
        elif curr == 'USD':
            xrate = None
        else:
            prior_date_rate = cr.get_rate(curr, 'USD', xrate_date)
            xrate = "{0:.4f}".format(prior_date_rate)

        return xrate

    def clean_daily_savings_dollars(self):
        today_date = dt.date.today()
        spending_data = self.cleaned_data.get("spending")
        date_data = self.cleaned_data.get('date')
        exist_count = Entry.objects.filter(date=date_data).count()
        currency = self.cleaned_data.get("currency")
        curr = currency
        if not self.instance.pk:
            if not date_data:
                raise ValidationError('Enter a date')
            elif today_date < date_data:
                raise ValidationError('Invalid date - entry cannot be in the future')
            elif not spending_data:
                raise ValidationError('*')
            elif exist_count >= 1:
                raise ValidationError('This entry already exists')
            else:
                spending_data_break = spending_data.replace(',', '')
                spending_data_split = spending_data_break.split()
                spending_data_list = [float(a) for a in spending_data_split]
                daily_spent = sum(spending_data_list)
                xrate_date = self.cleaned_data.get(str("date"))
                if curr == 'USD':
                    dollars_sum_format = "{0:.2f}".format(daily_spent)

                elif date_data < dt.date(2017, 2, 1):
                    prior_date_rate = cr.get_rate(curr, 'USD', xrate_date)
                    xrate = prior_date_rate
                    dollars_sum = daily_spent * xrate - 93
                    dollars_sum_format = "{0:.2f}".format(dollars_sum)

                else:
                    prior_date_rate = cr.get_rate(curr, 'USD', xrate_date)
                    xrate = prior_date_rate
                    dollars_sum = daily_spent * xrate - 87
                    dollars_sum_format = "{0:.2f}".format(dollars_sum)

                return dollars_sum_format
        else:
            spending_data_break = spending_data.replace(',', '')
            spending_data_split = spending_data_break.split()
            spending_data_list = [float(a) for a in spending_data_split]
            daily_spent = sum(spending_data_list)
            xrate_date = self.cleaned_data.get(str("date"))
            if curr == 'USD':
                dollars_sum_format = "{0:.2f}".format(daily_spent)

            elif date_data < dt.date(2017, 2, 1):
                prior_date_rate = cr.get_rate(curr, 'USD', xrate_date)
                xrate = prior_date_rate
                dollars_sum = daily_spent * xrate - 93
                dollars_sum_format = "{0:.2f}".format(dollars_sum)

            else:
                prior_date_rate = cr.get_rate(curr, 'USD', xrate_date)
                xrate = prior_date_rate
                dollars_sum = daily_spent * xrate - 87
                dollars_sum_format = "{0:.2f}".format(dollars_sum)

            return dollars_sum_format

    def clean_daily_savings_display(self):
        today_date = dt.date.today()
        spending_data = self.cleaned_data.get("spending")
        date_data = self.cleaned_data.get('date')
        exist_count = Entry.objects.filter(date=date_data).count()
        currency = self.cleaned_data.get("currency")
        curr = currency
        if not self.instance.pk:
            if not date_data:
                raise ValidationError('Enter a date')

            elif today_date < date_data:
                raise ValidationError('Invalid date - entry cannot be in the future')
            elif not spending_data:
                raise ValidationError('*')
            elif exist_count >= 1:
                raise ValidationError('This entry already exists')
            else:
                spending_data_break = spending_data.replace(',', '')
                spending_data_split = spending_data_break.split()
                spending_data_list = [float(a) for a in spending_data_split]
                daily_spent = sum(spending_data_list)
                xrate_date = self.cleaned_data.get(str("date"))
                if curr == 'USD':
                    absolute = abs(daily_spent)
                    dollars_sum_format = ("{0:.2f}".format(absolute))
                elif date_data < dt.date(2017, 2, 1):
                    prior_date_rate = cr.get_rate(curr, 'USD', xrate_date)
                    xrate = prior_date_rate
                    dollars_sum = daily_spent * xrate - 93
                    absolute = abs(dollars_sum)
                    dollars_sum_format = ("{0:.2f}".format(absolute))
                else:
                    prior_date_rate = cr.get_rate(curr, 'USD', xrate_date)
                    xrate = prior_date_rate
                    dollars_sum = daily_spent * xrate - 87
                    absolute = abs(dollars_sum)
                    dollars_sum_format = ("{0:.2f}".format(absolute))

                return dollars_sum_format
        else:
            spending_data_break = spending_data.replace(',', '')
            spending_data_split = spending_data_break.split()
            spending_data_list = [float(a) for a in spending_data_split]
            daily_spent = sum(spending_data_list)
            xrate_date = self.cleaned_data.get(str("date"))
            if curr == 'USD':
                absolute = abs(daily_spent)
                dollars_sum_format = ("{0:.2f}".format(absolute))
            elif date_data < dt.date(2017, 2, 1):
                prior_date_rate = cr.get_rate(curr, 'USD', xrate_date)
                xrate = prior_date_rate
                dollars_sum = daily_spent * xrate - 93
                absolute = abs(dollars_sum)
                dollars_sum_format = ("{0:.2f}".format(absolute))
            else:
                prior_date_rate = cr.get_rate(curr, 'USD', xrate_date)
                xrate = prior_date_rate
                dollars_sum = daily_spent * xrate - 87
                absolute = abs(dollars_sum)
                dollars_sum_format = ("{0:.2f}".format(absolute))

            return dollars_sum_format


class SavingsForm(ModelForm):
    class Meta:
        model = Savings
        fields = ['total_spent', 'total_spent_dollars', 'total_savings', 'total_savings_display']
        # exclude = ('spending_sum',)
        labels = {'total_spent': 'Total €€€ Spending', 'total_spent_dollars': 'Total $$$ Spending', 'total_savings': 'Total $$$ Savings', 'total_savings_display': 'Total $$$ Savings(ABS)'}
        # help_texts = {'date': 'Enter a date using the following format mm/dd/yyyy.', 'spending': 'Enter the total amount of spending spent.', }

    def clean_total_spent(self):
        sum_spending = Entry.objects.aggregate(s=Sum('spending_sum')).get('s')
        sum_format = "{0:.2f}".format(sum_spending)

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
        fields = ['month', 'year', 'total_spent', 'total_spent_dollars', 'total_savings', 'total_savings_display']
        # exclude =
        labels = {'month': 'Month', 'year': 'Year', 'total_spent': 'Total €€€ Spending', 'total_spent_dollars': 'Total $$$ Spending', 'total_savings': 'Total $$$ Savings', 'total_savings_display': 'Total $$$ Savings(ABS)'}
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
        # mar = datetime.strptime('3/1/2016', '%m/%d/%Y')
        # month = calendar.month_name[mar.month]

        # April
        # apr = datetime.strptime('4/1/2016', '%m/%d/%Y')
        # month = calendar.month_name[apr.month]

        # May
        # may = datetime.strptime('5/1/2016', '%m/%d/%Y')
        # month = calendar.month_name[may.month]

        # June
        june = datetime.strptime('6/1/2016', '%m/%d/%Y')
        month = calendar.month_name[june.month]

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

    def clean_total_spent(self):

        # January
        # sum_spending = Entry.objects.filter(date__range=('2017-1-1', '2017-1-31')).aggregate(s=Sum('spending_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_spending)

        # February17
        # sum_spending = Entry.objects.filter(date__range=('2017-2-1', '2017-2-28')).aggregate(s=Sum('spending_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_spending)

        # March
        # sum_spending = Entry.objects.filter(date__range=('2017-3-1', '2017-3-31')).aggregate(s=Sum('spending_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_spending)

        # April
        # sum_spending = Entry.objects.filter(date__range=('2017-4-1', '2017-4-30')).aggregate(s=Sum('spending_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_spending)

        # May
        # sum_spending = Entry.objects.filter(date__range=('2017-5-1', '2017-5-31')).aggregate(s=Sum('spending_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_spending)

        # June
        sum_spending = Entry.objects.filter(date__range=('2017-6-1', '2017-6-31')).aggregate(s=Sum('spending_sum')).get('s')
        sum_format = "{0:.2f}".format(sum_spending)

        # July
        # sum_spending = Entry.objects.filter(date__range=('2017-7-1', '2017-7-31')).aggregate(s=Sum('spending_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_spending)

        # August
        # sum_spending = Entry.objects.filter(date__range=('2017-8-1', '2017-8-31')).aggregate(s=Sum('spending_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_spending)

        # September
        # sum_spending = Entry.objects.filter(date__range=('2017-9-1', '2017-9-30')).aggregate(s=Sum('spending_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_spending)

        # October
        # sum_spending = Entry.objects.filter(date__range=('2017-10-1', '2017-10-31')).aggregate(s=Sum('spending_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_spending)

        # November
        # sum_spending = Entry.objects.filter(date__range=('2016-11-1', '2016-11-30')).aggregate(s=Sum('spending_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_spending)

        # December
        # sum_spending = Entry.objects.filter(date__range=('2016-12-1', '2016-12-31')).aggregate(s=Sum('spending_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_spending)

        return sum_format

    def clean_total_spent_dollars(self):

        # January
        # sum_dollars = Entry.objects.filter(date__range=('2017-1-1', '2017-1-31')).aggregate(s=Sum('dollars_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_dollars)

        # February17
        # sum_dollars = Entry.objects.filter(date__range=('2017-2-1', '2017-2-28')).aggregate(s=Sum('dollars_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_dollars)

        # March
        # sum_dollars = Entry.objects.filter(date__range=('2017-3-1', '2017-3-31')).aggregate(s=Sum('dollars_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_dollars)

        # April
        # sum_dollars = Entry.objects.filter(date__range=('2017-4-1', '2017-4-30')).aggregate(s=Sum('dollars_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_dollars)

        # May
        # sum_dollars = Entry.objects.filter(date__range=('2017-5-1', '2017-5-31')).aggregate(s=Sum('dollars_sum')).get('s')
        # sum_format = "{0:.2f}".format(sum_dollars)

        # June
        sum_dollars = Entry.objects.filter(date__range=('2017-6-1', '2017-6-31')).aggregate(s=Sum('dollars_sum')).get('s')
        sum_format = "{0:.2f}".format(sum_dollars)

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
        # sum_savings = Entry.objects.filter(date__range=('2017-3-1', '2017-3-31')).aggregate(s=Sum('daily_savings_dollars')).get('s')
        # sum_format = "{0:.2f}".format(sum_savings)

        # April
        # sum_savings = Entry.objects.filter(date__range=('2017-4-1', '2017-4-30')).aggregate(s=Sum('daily_savings_dollars')).get('s')
        # sum_format = "{0:.2f}".format(sum_savings)

        # May
        # sum_savings = Entry.objects.filter(date__range=('2017-5-1', '2017-5-31')).aggregate(s=Sum('daily_savings_dollars')).get('s')
        # sum_format = "{0:.2f}".format(sum_savings)

        # June
        sum_savings = Entry.objects.filter(date__range=('2017-6-1', '2017-6-31')).aggregate(s=Sum('daily_savings_dollars')).get('s')
        sum_format = "{0:.2f}".format(sum_savings)

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
        sum_savings = Entry.objects.filter(date__range=('2017-6-1', '2017-6-31')).aggregate(s=Sum('daily_savings_dollars')).get('s')
        absolute = abs(sum_savings)
        sum_format = "{0:.2f}".format(absolute)

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

