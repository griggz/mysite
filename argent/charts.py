from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import MonthYear, Entry, Savings
from django.db.models import Sum
import datetime
import pandas as pd

today = datetime.date.today()
User = get_user_model()


# API Method "RESTFRAMEWORK"


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # SPENDING/SAVINGS BY MONTH
        June17_spending = Entry.objects.filter(
            date__range=('2017-6-1', '2017-6-30')).values_list('dollars_sum')

        # SPENDING BY COUNTRY
        lyon = Entry.objects.filter(city=1).aggregate(
            s=Sum('dollars_sum')).get('s')
        avignon = Entry.objects.filter(city=2).aggregate(
            s=Sum('dollars_sum')).get('s')
        arles = Entry.objects.filter(city=3).aggregate(
            s=Sum('dollars_sum')).get('s')
        paris = Entry.objects.filter(city=4).aggregate(
            s=Sum('dollars_sum')).get('s')
        aix = Entry.objects.filter(city=5).aggregate(
            s=Sum('dollars_sum')).get('s')
        london = Entry.objects.filter(city=6).aggregate(
            s=Sum('dollars_sum')).get('s')
        dublin = Entry.objects.filter(city=7).aggregate(
            s=Sum('dollars_sum')).get('s')
        prague = Entry.objects.filter(city=8).aggregate(
            s=Sum('dollars_sum')).get('s')
        budapest = Entry.objects.filter(city=9).aggregate(
            s=Sum('dollars_sum')).get('s')
        rome = Entry.objects.filter(city=10).aggregate(
            s=Sum('dollars_sum')).get('s')
        florence = Entry.objects.filter(city=11).aggregate(
            s=Sum('dollars_sum')).get('s')
        naples = Entry.objects.filter(city=12).aggregate(
            s=Sum('dollars_sum')).get('s')
        albufera = Entry.objects.filter(city=13).aggregate(
            s=Sum('dollars_sum')).get('s')
        vienna = Entry.objects.filter(city=14).aggregate(
            s=Sum('dollars_sum')).get('s')
        barcelona = Entry.objects.filter(city=15).aggregate(
            s=Sum('dollars_sum')).get('s')
        geneva = Entry.objects.filter(city=16).aggregate(
            s=Sum('dollars_sum')).get('s')
        brussels = Entry.objects.filter(city=17).aggregate(
            s=Sum('dollars_sum')).get('s')
        bruges = Entry.objects.filter(city=18).aggregate(
            s=Sum('dollars_sum')).get('s')
        vienne = Entry.objects.filter(city=19).aggregate(
            s=Sum('dollars_sum')).get('s')
        perouges = Entry.objects.filter(city=20).aggregate(
            s=Sum('dollars_sum')).get('s')
        annecy = Entry.objects.filter(city=22).aggregate(
            s=Sum('dollars_sum')).get('s')
        # for i in Entry.objects.filter(city=2)

        # LAST 6 MONTHS SPENDING/SAVINGS
        # SAVINGS
        # qs_November16 = Entry.objects.filter(date__range=('2016-11-1', '2016-11-30')).aggregate(s=Sum('dollars_sum')).get('s')
        qs_December16 = Entry.objects.filter(
            date__range=('2016-12-1', '2016-12-31')).aggregate(
            s=Sum('dollars_sum')).get('s')
        qs_January17 = Entry.objects.filter(
            date__range=('2017-1-1', '2017-1-31')).aggregate(
            s=Sum('dollars_sum')).get('s')
        qs_February17 = Entry.objects.filter(
            date__range=('2017-2-1', '2017-2-28')).aggregate(
            s=Sum('dollars_sum')).get('s')
        qs_March17 = Entry.objects.filter(
            date__range=('2017-3-1', '2017-3-31')).aggregate(
            s=Sum('dollars_sum')).get('s')
        qs_April17 = Entry.objects.filter(
            date__range=('2017-4-1', '2017-4-30')).aggregate(
            s=Sum('dollars_sum')).get('s')
        qs_May17 = Entry.objects.filter(
            date__range=('2017-5-1', '2017-5-31')).aggregate(
            s=Sum('dollars_sum')).get('s')
        qs_June17 = Entry.objects.filter(
            date__range=('2017-6-1', '2017-6-30')).aggregate(
            s=Sum('dollars_sum')).get('s')

        # SPENDING
        # qs2_November16 = Entry.objects.filter(date__range=('2016-11-1', '2016-11-30')).aggregate(s=Sum('daily_savings_display')).get('s')
        qs2_December16 = Entry.objects.filter(
            date__range=('2016-12-1', '2016-12-31')).aggregate(
            s=Sum('daily_savings_display')).get('s')
        qs2_January17 = Entry.objects.filter(
            date__range=('2017-1-1', '2017-1-31')).aggregate(
            s=Sum('daily_savings_display')).get('s')
        qs2_February17 = Entry.objects.filter(
            date__range=('2017-2-1', '2017-2-28')).aggregate(
            s=Sum('daily_savings_display')).get('s')
        qs2_March17 = Entry.objects.filter(
            date__range=('2017-3-1', '2017-3-31')).aggregate(
            s=Sum('daily_savings_display')).get('s')
        qs2_April17 = Entry.objects.filter(
            date__range=('2017-4-1', '2017-4-30')).aggregate(
            s=Sum('daily_savings_display')).get('s')
        qs2_May17 = Entry.objects.filter(
            date__range=('2017-5-1', '2017-5-31')).aggregate(
            s=Sum('daily_savings_display')).get('s')
        qs2_June17 = Entry.objects.filter(
            date__range=('2017-6-1', '2017-6-30')).aggregate(
            s=Sum('daily_savings_display')).get('s')

        labels = ["DEC16", "JAN17", "FEB17", "MAR17", "APR17", "MAY17",
                  "JUNE17"]
        spending = [qs_December16, qs_January17, qs_February17, qs_March17,
                    qs_April17, qs_May17, qs_June17]
        savings = [qs2_December16, qs2_January17, qs2_February17, qs2_March17,
                   qs2_April17, qs2_May17, qs2_June17]
        country_labels = [lyon, avignon, arles, paris, aix, london, dublin, prague,
                   budapest, rome, florence, naples, albufera, vienna,
                   barcelona, geneva, brussels, bruges, vienne, perouges,
                   annecy]

        # GRAND TOTAL SPENDING/SAVINGS
        sav_object = Savings.objects.get(id=2)
        qs_spending = sav_object.total_spent_dollars
        qs_savings = sav_object.total_savings_display

        spent_labels = ["Spent"]
        saved_labels = ["Saved"]
        total_spending = [qs_spending]
        total_saving = [qs_savings]

        # ANNUAL SAVINGS
        # 2017
        year17spent = Entry.objects.filter(
            date__range=('2017-1-1', '2017-12-31')).aggregate(
            s=Sum('dollars_sum')).get('s')
        year17saved = Entry.objects.filter(
            date__range=('2017-1-1', '2017-12-31')).aggregate(
            s=Sum('daily_savings_display')).get('s')

        spent_labels17 = ["Spent"]
        saved_labels17 = ["Saved"]
        spending17 = [year17spent]
        savings17 = [year17saved]

        data = {
            # LAST 6 MONTH
            "labels": labels,
            "spending": spending,
            "savings": savings,

            # GRAND TOTALS
            "spent_label": spent_labels,
            "saved_label": saved_labels,
            "total_spending": total_spending,
            "total_saving": total_saving,
            # ANNUAL TOTALS
            "spent_labels17": spent_labels17,
            "saved_labels17": saved_labels17,
            "spending17": spending17,
            "savings17": savings17,
            # TOTALS BY COUNTRY w/ LOCATION DATA
            "country_labels": country_labels,
            "france": {"lyon": {"sum": lyon,
                                "lat": 45.74846,
                                "lon": 4.84671},
                       "avignon": {"sum": avignon,
                                   "lat": 43.94834,
                                   "lon": 4.80892},
                       "arles": {"sum": arles,
                                 "lat": 43.67681,
                                 "lon": 4.63031},
                       "vienne": {"sum": vienne,
                                  "lat": 45.51667,
                                  "lon": 4.86667},
                       "perouges": {"sum": perouges,
                                    "lat": 46.202789,
                                    "lon": 5.219246},
                       "annecy": {"sum": annecy,
                                  "lat": 45.9,
                                  "lon": 6.11667},

                       "paris": {"sum": paris,
                                 "lat": 48.864716,
                                 "lon": 2.349014},
                       "aix-en-provence": {"sum": aix,
                                           "lat": 43.5283,
                                           "lon": 5.44973}},
            "United Kingdon": {"london": {"sum": london,
                                          "lat": 51.509865,
                                          "lon": -0.118092}},
            "Ireland": {"dublin": {"sum": dublin,
                                   "lat": 53.350140,
                                   "lon": -6.266155}},
            "Hungary": {"budapest": {"sum": budapest,
                                     "lat": 47.497913,
                                     "lon": 19.040236}},
            "Czech Republic": {"prague": {"sum": prague,
                                          "lat": 50.073658,
                                          "lon": 4.418540}},
            "Italy": {"rome": {"sum": rome,
                               "lat": 41.902782,
                               "lon": 12.496366},
                      "florence": {"sum": florence,
                                   "lat": 43.769562,
                                   "lon": 11.255814},
                      "naples": {"sum": naples,
                                 "lat": 40.853294,
                                 "lon": 14.305573}},
            "Austria": {"vienna": {"sum": vienna,
                                   "lat": 48.210033,
                                   "lon": 16.363449}},
            "Portugal": {"albufera": {"sum": albufera,
                                      "lat": 37.08819,
                                      "lon": -8.2503}},
            "Spain": {"barcelona": {"sum": barcelona,
                                    "lat": 41.390205,
                                    "lon": 2.154007}},
            "Switzerland": {"geneva": {"sum": geneva,
                                       "lat": 46.204391,
                                       "lon": 6.143158}},
            "Belgium": {"brussels": {"sum": brussels,
                                     "lat": 50.85045,
                                     "lon": 4.34878},
                        "bruges": {"sum": bruges,
                                   "lat": 51.20892,
                                   "lon": 3.22424}}
        }

        return Response(data)


class DashData(APIView):  # FOR TESTING WITH argent/dash and argent/api/data
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        sav_object = Savings.objects.get(id=2)

        # Total Savings/Spent
        qs_spending = sav_object.total_savings_display
        qs_savings = sav_object.total_spent_dollars

        labels = ["Total Spent", "Total Saved", ]
        totals = [qs_spending, qs_savings]
        data = {
            "labels": labels,
            "totals": totals,
        }

        return Response(data)


# # Alternate method | Works with url(r'^api/data/$', get_data, name='api-data')
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
