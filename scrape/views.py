from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Yelp, Results
from .forms import YelpForm
from django.contrib import messages
from .scripts.scrape_yelp import scrape
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import pandas as pd


class YelpScrape:
    def __init__(self, link, instance_id):
        self.link = link
        self.results = None
        self.instance_id = instance_id
        self.business_name = None
        self.scrape_yelp()

    def scrape_yelp(self):
        results, biz_name = scrape(self.link, 5)
        self.results = pd.DataFrame(results)
        self.business_name = biz_name

    def process_results(self):
        for row in self.results.itertuples():
            # add some custom validation\parsing for some of the fields
            yelp_obj = Yelp.objects.get(id=self.instance_id)
            instance = Results(yelp_id=yelp_obj, author=row.author,
                               date=row.date, rating=row.rating,
                               review=row.reviews)
            try:
                instance.save()
            except:
                pass


def create_scrape(request):
    # if not request.user.is_staff or not request.user.is_superuser:
    #     raise Http404
    yelp_form = YelpForm(request.POST or None, request.FILES or None)
    if yelp_form.is_valid():
        instance = yelp_form.save()
        instance.user = request.user
        scrape = YelpScrape(instance.link, instance.id)
        instance.business_name = scrape.business_name
        instance.yelp_id = instance.id
        instance.save()
        YelpScrape(instance.link, instance.id).process_results()
        messages.success(request, '{}'.format(str(instance.link)), 'has been scraped!')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": "New Scrape",
        "form": yelp_form,
    }
    return render(request, "scrape/scrape_form.html", context)


def scrape_details_list(request, slug=None):
    instance = get_object_or_404(Yelp, slug=slug)
    results = Results.objects.all().filter(yelp_id=instance.id)

    paginator = Paginator(results, 25)  # Show 25 posts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    # export to csv requirements

    context = {
            "object_list": queryset,
            "title": instance.business_name.replace('-', ' ').upper() + ' REVIEWS',
            "page_request_var": page_request_var,
        }

    return render(request, 'scrape/results.html', context)




