# import random
# import django
# import datetime
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure
# from matplotlib.dates import DateFormatter
# import matplotlib.pyplot
# import matplotlib.pyplot as plt
# import numpy as np
# from .models import Entry, Savings, MonthYear
# from django.db.models import Sum
#
#
# def november16(request):
#     sum_euros = Entry.objects.filter(date__month=11).filter(date__year=2016).aggregate(s=Sum('euros_sum')).get('s')
#     sum_euros_f = "{0:.2f}".format(sum_euros)
#     fig = Figure()
#     ax = fig.add_subplot(111)
#     x = []
#     y = []
#     for i in range(10):
#         x.append(sum_euros_f)
#         y.append(random.randint(0, 1000))
#     ax.plot_date(x, y, '-')
#     ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
#     fig.autofmt_xdate()
#     canvas = FigureCanvas(fig)
#     response = django.http.HttpResponse(content_type='image/png')
#     canvas.print_png(response)
#     return response



# ORIGINAL CODE
#
# def simple(request):
#     import random
#     import django
#     import datetime
#
#     from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
#     from matplotlib.figure import Figure
#     from matplotlib.dates import DateFormatter
#
#     fig = Figure()
#     ax = fig.add_subplot(111)
#     x = []
#     y = []
#     now = datetime.datetime.now()
#     delta = datetime.timedelta(days=1)
#     for i in range(10):
#         x.append(now)
#         now += delta
#         y.append(random.randint(0, 1000))
#     ax.plot_date(x, y, '-')
#     ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
#     fig.autofmt_xdate()
#     canvas = FigureCanvas(fig)
#     response = django.http.HttpResponse(content_type='image/png')
#     canvas.print_png(response)
#     return response