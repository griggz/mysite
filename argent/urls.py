from django.urls import path, re_path, include

from argent.charts import ChartsView, ChartData, DashData

from . import views

# from argent.views import detail

app_name = 'argent'


urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    re_path(r'^entry/list/(?P<month>\w+)$', views.EntryListView.as_view(), name='entry-list'),
    re_path(r'^entry/detail/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    re_path(r'^entry/add/$', views.EntryCreate.as_view(), name='entry-add'),
    re_path(r'^entry/update/(?P<pk>[0-9]+)/$', views.EntryUpdate.as_view(), name='entry-update'),
    re_path(r'^api/chart/data/$', ChartData.as_view()),

    # url(r'dash', ChartsView.as_view(), name='dash'),
    #
    # url(r'api/data/$', DashData.as_view()),
    #
    # url(r'^charts', ChartsView.as_view(), name='charts'),
    #
    # url(r'^api/data/$', get_data, name='api-data'),
    #
    # url(r'entry/(?P<pk>[0-9]+)/delete/$', views.EntryDelete.as_view(), name='entry-delete'),

]
