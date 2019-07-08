from django.contrib import admin
from django.db import models
from .models import Yelp, Results
from .forms import YelpForm
from pagedown.widgets import AdminPagedownWidget


class YelpAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }
    list_display = ['id', 'business_name', "scrape_date", "id"]
    list_filter = ["scrape_date"]
    search_fields = ["business_name"]
    form = YelpForm

    class Meta:
        model = Yelp


admin.site.register(Yelp, YelpAdmin)


class ResultsAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }
    list_display = ['yelp_id', "author", "date", 'rating', 'review']
    list_filter = ["yelp_id"]
    search_fields = ["yelp_id"]

    class Meta:
        model = Results


admin.site.register(Results, ResultsAdmin)