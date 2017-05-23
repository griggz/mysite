from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import MonthYear, Entry, Savings
from django.db.models import Sum
import datetime

today = datetime.date.today()
User = get_user_model()

# API Method "RESTFRAMEWORK"


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # SAVINGS
        qs_November16 = Entry.objects.filter(date__range=('2016-11-1', '2016-11-30')).aggregate(s=Sum('dollars_sum')).get('s')
        qs_December16 = Entry.objects.filter(date__range=('2016-12-1', '2016-12-31')).aggregate(s=Sum('dollars_sum')).get('s')
        qs_January17 = Entry.objects.filter(date__range=('2017-1-1', '2017-1-31')).aggregate(s=Sum('dollars_sum')).get('s')
        qs_February17 = Entry.objects.filter(date__range=('2017-2-1', '2017-2-28')).aggregate(s=Sum('dollars_sum')).get('s')
        qs_March17 = Entry.objects.filter(date__range=('2017-3-1', '2017-3-31')).aggregate(s=Sum('dollars_sum')).get('s')
        qs_April17 = Entry.objects.filter(date__range=('2017-4-1', '2017-4-30')).aggregate(s=Sum('dollars_sum')).get('s')
        qs_May17 = Entry.objects.filter(date__range=('2017-5-1', '2017-5-31')).aggregate(s=Sum('dollars_sum')).get('s')

        # SPENDING
        qs2_November16 = Entry.objects.filter(date__range=('2016-11-1', '2016-11-30')).aggregate(s=Sum('daily_savings_display')).get('s')
        qs2_December16 = Entry.objects.filter(date__range=('2016-12-1', '2016-12-31')).aggregate(s=Sum('daily_savings_display')).get('s')
        qs2_January17 = Entry.objects.filter(date__range=('2017-1-1', '2017-1-31')).aggregate(s=Sum('daily_savings_display')).get('s')
        qs2_February17 = Entry.objects.filter(date__range=('2017-2-1', '2017-2-28')).aggregate(s=Sum('daily_savings_display')).get('s')
        qs2_March17 = Entry.objects.filter(date__range=('2017-3-1', '2017-3-31')).aggregate(s=Sum('daily_savings_display')).get('s')
        qs2_April17 = Entry.objects.filter(date__range=('2017-4-1', '2017-4-30')).aggregate(s=Sum('daily_savings_display')).get('s')
        qs2_May17 = Entry.objects.filter(date__range=('2017-5-1', '2017-5-31')).aggregate(s=Sum('daily_savings_display')).get('s')

        labels = ["NOV16", "DEC16", "JAN17", "FEB17", "MAR17", "APR17", "MAY17"]
        spending = [qs_November16, qs_December16, qs_January17, qs_February17, qs_March17, qs_April17, qs_May17]
        savings = [qs2_November16, qs2_December16, qs2_January17, qs2_February17, qs2_March17, qs2_April17, qs2_May17]
        data = {
            "labels": labels,
            "spending": spending,
            "savings": savings
        }

        return Response(data)


class DashData(APIView):  # FOR TESTING WITH argent/dash and argent/api/data
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # SAVINGS
        qs_November16 = Entry.objects.filter(date__range=('2016-11-1', '2016-11-30')).aggregate(s=Sum('dollars_sum')).get('s')
        qs_December16 = Entry.objects.filter(date__range=('2016-12-1', '2016-12-31')).aggregate(s=Sum('dollars_sum')).get('s')
        qs_January17 = Entry.objects.filter(date__range=('2017-1-1', '2017-1-31')).aggregate(s=Sum('dollars_sum')).get('s')
        qs_February17 = Entry.objects.filter(date__range=('2017-2-1', '2017-2-28')).aggregate(s=Sum('dollars_sum')).get('s')
        qs_March17 = Entry.objects.filter(date__range=('2017-3-1', '2017-3-31')).aggregate(s=Sum('dollars_sum')).get('s')
        qs_April17 = Entry.objects.filter(date__range=('2017-4-1', '2017-4-30')).aggregate(s=Sum('dollars_sum')).get('s')
        qs_May17 = Entry.objects.filter(date__range=('2017-5-1', '2017-5-31')).aggregate(s=Sum('dollars_sum')).get('s')

        # SPENDING
        qs2_November16 = Entry.objects.filter(date__range=('2016-11-1', '2016-11-30')).aggregate(s=Sum('daily_savings_display')).get('s')
        qs2_December16 = Entry.objects.filter(date__range=('2016-12-1', '2016-12-31')).aggregate(s=Sum('daily_savings_display')).get('s')
        qs2_January17 = Entry.objects.filter(date__range=('2017-1-1', '2017-1-31')).aggregate(s=Sum('daily_savings_display')).get('s')
        qs2_February17 = Entry.objects.filter(date__range=('2017-2-1', '2017-2-28')).aggregate(s=Sum('daily_savings_display')).get('s')
        qs2_March17 = Entry.objects.filter(date__range=('2017-3-1', '2017-3-31')).aggregate(s=Sum('daily_savings_display')).get('s')
        qs2_April17 = Entry.objects.filter(date__range=('2017-4-1', '2017-4-30')).aggregate(s=Sum('daily_savings_display')).get('s')
        qs2_May17 = Entry.objects.filter(date__range=('2017-5-1', '2017-5-31')).aggregate(s=Sum('daily_savings_display')).get('s')

        labels = ["NOV16", "DEC16", "JAN17", "FEB17", "MAR17", "APR17", "MAY17"]
        spending = [qs_November16, qs_December16, qs_January17, qs_February17, qs_March17, qs_April17, qs_May17]
        savings = [qs2_November16, qs2_December16, qs2_January17, qs2_February17, qs2_March17, qs2_April17, qs2_May17]
        data = {
            "labels": labels,
            "spending": spending,
            "savings": savings
        }

        return Response(data)


# Alternate method | Works with url(r'^api/data/$', get_data, name='api-data')
class ChartsView(View):
    def get(self, request, *args, **kwargs):
        entry_qs = Entry.objects.filter(date=today)
        savings_qs = Savings.objects.filter(id=2)
        context = {
            'entry_qs': entry_qs,
            'savings_qs': savings_qs,
        }
        return render(request, 'argent/dashboard.html', context)


# def get_data(request, *args, **kwargs):
#     data = {
#         "sales": MonthYear.objects.filter(month='December'),
#         "customers": 10,
#     }
#     return JsonResponse(data)
