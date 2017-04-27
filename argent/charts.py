from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import MonthYear, Entry
from django.db.models import Sum


# API Method "RESTFRAMEWORK"


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        qs_November16 = Entry.objects.filter(date__range=('2016-11-1', '2016-11-30')).aggregate(s=Sum('dollars_sum')).get('s')
        qs_December16 = Entry.objects.filter(date__range=('2016-12-1', '2016-12-31')).aggregate(s=Sum('dollars_sum')).get('s')
        qs_January17 = Entry.objects.filter(date__range=('2017-1-1', '2017-1-31')).aggregate(s=Sum('dollars_sum')).get('s')
        qs_February17 = Entry.objects.filter(date__range=('2017-2-1', '2017-2-28')).aggregate(s=Sum('dollars_sum')).get('s')
        qs_March17 = Entry.objects.filter(date__range=('2017-3-1', '2017-3-31')).aggregate(s=Sum('dollars_sum')).get('s')
        qs_April17 = Entry.objects.filter(date__range=('2017-4-1', '2017-4-30')).aggregate(s=Sum('dollars_sum')).get('s')
        labels = ["November16", "December16", "January17", "February17", "March17", "April17"]
        default_items = [qs_November16, qs_December16, qs_January17, qs_February17, qs_March17, qs_April17]
        data = {
            "labels": labels,
            "default": default_items
        }

        return Response(data)

User = get_user_model()


# Alternate method | Works with url(r'^api/data/$', get_data, name='api-data')
class ChartsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'argent/charts.html', {})


def get_data(request, *args, **kwargs):
    data = {
        "sales": MonthYear.objects.filter(month='December'),
        "customers": 10,
    }
    return JsonResponse(data)