from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from .forms import EntryForm
from django.db.models import Sum
from datetime import datetime
from .models import Entry, Savings, MonthYear

"""DAILY SPENDING TRACKER 1.0: This function accepts your daily financial
spending, adds it together, converts it from spending to Dollars, and uploads it
in to its corresponding database."""


class IndexView(generic.ListView):

    template_name = 'argent/index.html'

    def get_queryset(self):
        return Entry.objects.all()

    def get_context_data(self, **kwargs):

        today_date = datetime.now()

        ctx = super(IndexView, self).get_context_data(**kwargs)

        # TODAY'S ENTRY
        # ctx['entry_qs'] = Entry.objects.filter(date=today_date) --> This displays today's entry
        ctx['entry_qs'] = Entry.objects.filter(date='2017-06-16')

        # CURRENT SAVINGS TOTALS
        ctx['savings_qs'] = Savings.objects.filter(id=2)

        # MONTHLY TOTALS

        # November
        ctx['November16_qs'] = MonthYear.objects.filter(month='November')
        # December
        ctx['December16_qs'] = MonthYear.objects.filter(month='December')
        # January
        ctx['January17_qs'] = MonthYear.objects.filter(month='January')
        # February
        ctx['February17_qs'] = MonthYear.objects.filter(month='February')
        # March
        ctx['March17_qs'] = MonthYear.objects.filter(month='March')
        # April
        ctx['April17_qs'] = MonthYear.objects.filter(month='April')
        # # May
        ctx['May17_qs'] = MonthYear.objects.filter(month='May')
        # # June
        ctx['June17_qs'] = MonthYear.objects.filter(month='June')

        return ctx


class DetailView(generic.DetailView):
    model = Entry
    template_name = 'argent/detail.html'

    def get_context_data(self, **kwargs):
        ctx = super(DetailView, self).get_context_data(**kwargs)
        ctx['current_month'] = self.get_object().date.strftime("%B")
        return ctx
    #
    # def get_context_data(self, **kwargs):
    #     ctx = super(DetailView, self).get_context_data(**kwargs)
    #     ctx['savings_qs'] = Savings.objects.filter(id=1)
    #     return ctx


class EntryCreate(CreateView):
    form_class = EntryForm
    template_name = 'argent/entry_form.html'

    def form_valid(self, form):
        item = form.save()
        item_date = item.date
        e_month_d = item_date.strftime('%m')
        e_month = item_date.strftime('%B')
        e_year = item_date.year
        qs = MonthYear.objects.filter(month=e_month, year=e_year)
        qsv = qs.values('id')
        qsm = e_month
        qsy = e_year
        """FIELDS BELOW RELATED TO THE MONTH/YEAR MODEL AND AGGREGATE MONTHLY TOTALS"""
        if qs.exists():
            qsm_list = []
            if qsm == 'January':
                qsm_list.append('1')
            elif qsm == 'February':
                qsm_list.append('2')
            elif qsm == 'March':
                qsm_list.append('3')
            elif qsm == 'April':
                qsm_list.append('4')
            elif qsm == 'May':
                qsm_list.append('5')
            elif qsm == 'June':
                qsm_list.append('6')
            elif qsm == 'July':
                qsm_list.append('7')
            elif qsm == 'August':
                qsm_list.append('8')
            elif qsm == 'September':
                qsm_list.append('9')
            elif qsm == 'October':
                qsm_list.append('10')
            elif qsm == 'November':
                qsm_list.append('11')
            elif qsm == 'December':
                qsm_list.append('12')

            q_month = qsm_list.pop()

            sum_spending = Entry.objects.filter(date__month=q_month).filter(date__year=qsy).aggregate(s=Sum('spending_sum')).get('s')
            sum_spending_f = "{0:.2f}".format(sum_spending)

            sum_dollars = Entry.objects.filter(date__month=q_month).filter(date__year=qsy).aggregate(s=Sum('dollars_sum')).get('s')
            sum_dollars_f = "{0:.2f}".format(sum_dollars)

            sum_savings = Entry.objects.filter(date__month=q_month).filter(date__year=qsy).aggregate(s=Sum('daily_savings_dollars')).get('s')
            sum_savings_f = "{0:.2f}".format(sum_savings)

            sum_savings = Entry.objects.filter(date__month=q_month).filter(date__year=qsy).aggregate(s=Sum('daily_savings_dollars')).get('s')
            absolute = abs(sum_savings)
            sum_abs_savings = "{0:.2f}".format(absolute)

            MonthYear.objects.filter(id=qsv).update(total_spent=sum_spending_f, total_spent_dollars=sum_dollars_f, total_savings=sum_savings_f, total_savings_display=sum_abs_savings)

            """FIELDS BELOW RELATED TO 'SAVINGS' MODEL AND AGGREGATE GRAND TOTALS"""
            # total_spending_spent
            sum_spending = Entry.objects.aggregate(s=Sum('spending_sum')).get('s')
            sum_spending_f = "{0:.2f}".format(sum_spending)

            # total_dollars_spent
            sum_dollars = Entry.objects.aggregate(s=Sum('dollars_sum')).get('s')
            sum_dollars_f = "{0:.2f}".format(sum_dollars)

            # total_sum
            sum_savings = Entry.objects.aggregate(s=Sum('daily_savings_dollars')).get('s')
            sum_format = "{0:.2f}".format(sum_savings)

            # total_sum_format
            sum_abs_savings = Entry.objects.aggregate(s=Sum('daily_savings_dollars')).get('s')
            absolute = abs(sum_abs_savings)
            sum_abs = "{0:.2f}".format(absolute)

            Savings.objects.filter(id=2).update(total_savings=sum_format, total_savings_display=sum_abs,
                                                total_spent_dollars=sum_dollars_f, total_spent=sum_spending_f)

            return super(EntryCreate, self).form_valid(form)

        else:

            sum_spending = Entry.objects.filter(date__month=e_month_d).filter(date__year=qsy).aggregate(
                s=Sum('spending_sum')).get('s')
            sum_spending_f = "{0:.2f}".format(sum_spending)

            sum_dollars = Entry.objects.filter(date__month=e_month_d).filter(date__year=qsy).aggregate(
                s=Sum('dollars_sum')).get('s')
            sum_dollars_f = "{0:.2f}".format(sum_dollars)

            sum_savings = Entry.objects.filter(date__month=e_month_d).filter(date__year=qsy).aggregate(
                s=Sum('daily_savings_dollars')).get('s')
            sum_savings_f = "{0:.2f}".format(sum_savings)

            sum_savings = Entry.objects.filter(date__month=e_month_d).filter(date__year=qsy).aggregate(
                s=Sum('daily_savings_dollars')).get('s')
            absolute = abs(sum_savings)
            sum_abs_savings = "{0:.2f}".format(absolute)

            MonthYear.objects.create(month=qsm, year=qsy, total_spent=sum_spending_f, total_spent_dollars=sum_dollars_f,
                                     total_savings=sum_savings_f, total_savings_display=sum_abs_savings)

            """FIELDS BELOW RELATED TO 'SAVINGS' MODEL AND AGGREGATE GRAND TOTALS"""
            # total_spending_spent
            sum_spending = Entry.objects.aggregate(s=Sum('spending_sum')).get('s')
            sum_spending_f = "{0:.2f}".format(sum_spending)

            # total_dollars_spent
            sum_dollars = Entry.objects.aggregate(s=Sum('dollars_sum')).get('s')
            sum_dollars_f = "{0:.2f}".format(sum_dollars)

            # total_sum
            sum_savings = Entry.objects.aggregate(s=Sum('daily_savings_dollars')).get('s')
            sum_format = "{0:.2f}".format(sum_savings)

            # total_sum_format
            sum_abs_savings = Entry.objects.aggregate(s=Sum('daily_savings_dollars')).get('s')
            absolute = abs(sum_abs_savings)
            sum_abs = "{0:.2f}".format(absolute)

            Savings.objects.filter(id=2).update(total_savings=sum_format, total_savings_display=sum_abs,
                                                total_spent_dollars=sum_dollars_f, total_spent=sum_spending_f)

            return super(EntryCreate, self).form_valid(form)


class EntryUpdate(UpdateView):
    model = Entry
    form_class = EntryForm
    template_name = 'argent/entry_form.html'

    def form_valid(self, form):
        item = form.save()
        item_date = item.date
        e_month_d = item_date.strftime('%m')
        e_month = item_date.strftime('%B')
        e_year = item_date.year
        qs = MonthYear.objects.filter(month=e_month, year=e_year)
        qsv = qs.values('id')
        qsm = e_month
        qsy = e_year
        """FIELDS BELOW RELATED TO THE MONTH/YEAR MODEL AND AGGREGATE MONTHLY TOTALS"""
        if qs.exists():
            qsm_list = []
            if qsm == 'January':
                qsm_list.append('1')
            elif qsm == 'February':
                qsm_list.append('2')
            elif qsm == 'March':
                qsm_list.append('3')
            elif qsm == 'April':
                qsm_list.append('4')
            elif qsm == 'May':
                qsm_list.append('5')
            elif qsm == 'June':
                qsm_list.append('6')
            elif qsm == 'July':
                qsm_list.append('7')
            elif qsm == 'August':
                qsm_list.append('8')
            elif qsm == 'September':
                qsm_list.append('9')
            elif qsm == 'October':
                qsm_list.append('10')
            elif qsm == 'November':
                qsm_list.append('11')
            elif qsm == 'December':
                qsm_list.append('12')

            q_month = qsm_list.pop()

            sum_spending = Entry.objects.filter(date__month=q_month).filter(date__year=qsy).aggregate(s=Sum('spending_sum')).get('s')
            sum_spending_f = "{0:.2f}".format(sum_spending)

            sum_dollars = Entry.objects.filter(date__month=q_month).filter(date__year=qsy).aggregate(s=Sum('dollars_sum')).get('s')
            sum_dollars_f = "{0:.2f}".format(sum_dollars)

            sum_savings = Entry.objects.filter(date__month=q_month).filter(date__year=qsy).aggregate(s=Sum('daily_savings_dollars')).get('s')
            sum_savings_f = "{0:.2f}".format(sum_savings)

            sum_savings = Entry.objects.filter(date__month=q_month).filter(date__year=qsy).aggregate(s=Sum('daily_savings_dollars')).get('s')
            absolute = abs(sum_savings)
            sum_abs_savings = "{0:.2f}".format(absolute)

            MonthYear.objects.filter(id=qsv).update(total_spent=sum_spending_f, total_spent_dollars=sum_dollars_f, total_savings=sum_savings_f, total_savings_display=sum_abs_savings)

            """FIELDS BELOW RELATED TO 'SAVINGS' MODEL AND AGGREGATE GRAND TOTALS"""
            # total_spending
            sum_spending = Entry.objects.aggregate(s=Sum('spending_sum')).get('s')
            sum_spending_f = "{0:.2f}".format(sum_spending)

            # total_dollars_spent
            sum_dollars = Entry.objects.aggregate(s=Sum('dollars_sum')).get('s')
            sum_dollars_f = "{0:.2f}".format(sum_dollars)

            # total_sum
            sum_savings = Entry.objects.aggregate(s=Sum('daily_savings_dollars')).get('s')
            sum_format = "{0:.2f}".format(sum_savings)

            # total_sum_format
            sum_abs_savings = Entry.objects.aggregate(s=Sum('daily_savings_dollars')).get('s')
            absolute = abs(sum_abs_savings)
            sum_abs = "{0:.2f}".format(absolute)

            Savings.objects.filter(id=2).update(total_savings=sum_format, total_savings_display=sum_abs,
                                                total_spent_dollars=sum_dollars_f, total_spent=sum_spending_f)

            return super(EntryUpdate, self).form_valid(form)

        else:
            """FIELDS BELOW RELATED TO THE MONTH/YEAR MODEL AND AGGREGATE MONTHLY TOTALS"""
            sum_spending = Entry.objects.filter(date__month=e_month_d).filter(date__year=qsy).aggregate(
                s=Sum('spending_sum')).get('s')
            sum_spending_f = "{0:.2f}".format(sum_spending)

            sum_dollars = Entry.objects.filter(date__month=e_month_d).filter(date__year=qsy).aggregate(
                s=Sum('dollars_sum')).get('s')
            sum_dollars_f = "{0:.2f}".format(sum_dollars)

            sum_savings = Entry.objects.filter(date__month=e_month_d).filter(date__year=qsy).aggregate(
                s=Sum('daily_savings_dollars')).get('s')
            sum_savings_f = "{0:.2f}".format(sum_savings)

            sum_savings = Entry.objects.filter(date__month=e_month_d).filter(date__year=qsy).aggregate(
                s=Sum('daily_savings_dollars')).get('s')
            absolute = abs(sum_savings)
            sum_abs_savings = "{0:.2f}".format(absolute)

            MonthYear.objects.create(month=qsm, year=qsy, total_spent=sum_spending_f, total_spent_dollars=sum_dollars_f,
                                     total_savings=sum_savings_f, total_savings_display=sum_abs_savings)

            """FIELDS BELOW RELATED TO 'SAVINGS' MODEL AND AGGREGATE GRAND TOTALS"""
            # total_spending
            sum_spending = Entry.objects.aggregate(s=Sum('spending_sum')).get('s')
            sum_spending_f = "{0:.2f}".format(sum_spending)

            # total_dollars_spent
            sum_dollars = Entry.objects.aggregate(s=Sum('dollars_sum')).get('s')
            sum_dollars_f = "{0:.2f}".format(sum_dollars)

            # total_sum
            sum_savings = Entry.objects.aggregate(s=Sum('daily_savings_dollars')).get('s')
            sum_format = "{0:.2f}".format(sum_savings)

            # total_sum_format
            sum_abs_savings = Entry.objects.aggregate(s=Sum('daily_savings_dollars')).get('s')
            absolute = abs(sum_abs_savings)
            sum_abs = "{0:.2f}".format(absolute)

            Savings.objects.filter(id=2).update(total_savings=sum_format, total_savings_display=sum_abs,
                                                total_spent_dollars=sum_dollars_f, total_spent=sum_spending_f)

            return super(EntryUpdate, self).form_valid(form)


# class EntryDelete(DeleteView):
#     model = Entry
#     success_url = reverse_lazy('argent:index')

class EntryListView(generic.ListView):
    template_name = 'argent/index_list.html'
    queryset = Entry.objects.all()

    def get_context_data(self, **kwargs):
        month = self.kwargs.get('month')
        ctx = super(EntryListView, self).get_context_data(**kwargs)

        # January
        if month == 'January':
            ctx['January17_qs'] = Entry.objects.filter(date__range=('2017-1-1', '2017-1-31'))

        # February17
        elif month == 'February':
            ctx['February17_qs'] = Entry.objects.filter(date__range=('2017-2-1', '2017-2-28'))

        # March
        elif month == 'March':
            ctx['March17_qs'] = Entry.objects.filter(date__range=('2017-3-1', '2017-3-31'))

        # April
        elif month == 'April':
            ctx['April17_qs'] = Entry.objects.filter(date__range=('2017-4-1', '2017-4-30'))

        # May
        elif month == 'May':
            ctx['May17_qs'] = Entry.objects.filter(date__range=('2017-5-1', '2017-5-31'))

        # June
        elif month == 'June':
            ctx['June17_qs'] = Entry.objects.filter(date__range=('2017-6-1', '2017-6-30'))

        # July
        elif month == 'July':
            ctx['July17_qs'] = Entry.objects.filter(date__range=('2017-7-1', '2017-7-31'))

        # August
        elif month == 'August':
            ctx['August17_qs'] = Entry.objects.filter(date__range=('2017-8-1', '2017-8-31'))

        # September
        elif month == 'September':
            ctx['September17_qs'] = Entry.objects.filter(date__range=('2017-9-1', '2017-9-30'))

        # October
        elif month == 'October':
            ctx['October17_qs'] = Entry.objects.filter(date__range=('2017-10-1', '2017-10-31'))

        # November
        elif month == 'November':
            ctx['November16_qs'] = Entry.objects.filter(date__range=('2016-11-1', '2016-11-30'))

        # December
        elif month == 'December':
            ctx['December16_qs'] = Entry.objects.filter(date__range=('2016-12-1', '2016-12-31'))

        else:

            return self

        return ctx

    # def get_context_data(self, **kwargs):
    #     context = super(ArticleListView, self).get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context
