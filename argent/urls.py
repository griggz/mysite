from django.conf.urls import url

from argent.charts import ChartsView, get_data, ChartData

from . import views

# from argent.views import detail

app_name = 'argent'


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'entry/list/(?P<month>\w+)$', views.EntryListView.as_view(), name='entry-list'),

    url(r'entry/detail/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    url(r'entry/add/$', views.EntryCreate.as_view(), name='entry-add'),

    url(r'entry/update/(?P<pk>[0-9]+)/$', views.EntryUpdate.as_view(), name='entry-update'),

    url(r'^charts', ChartsView.as_view(), name='charts'),

    url(r'^api/data/$', get_data, name='api-data'),

    url(r'^api/chart/data/$', ChartData.as_view()),

    # url(r'entry/(?P<pk>[0-9]+)/delete/$', views.EntryDelete.as_view(), name='entry-delete'),

]
