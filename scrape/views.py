from .models import Yelp, Results
from rest_framework import generics, permissions, pagination
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
from .serializers import ResultsSerializer, ScrapeSerializer
from .scripts.scrape_run import YelpScrape as Scrape


class ScrapePageNumberPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'size'
    max_page_size = 20

    def get_paginated_response(self, data):
        user = False
        user = self.request.user
        if user.is_authenticated:
            user = True
        context = {
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'user': user,
            'results': data,
        }
        return Response(context)


class ScrapeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset            = Yelp.objects.all()
    serializer_class    = ScrapeSerializer
    lookup_field        = 'slug'
    permission_classes  = [IsOwnerOrReadOnly]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class ScrapeListCreateAPIView(generics.ListCreateAPIView):
    queryset            = Yelp.objects.all()
    serializer_class    = ScrapeSerializer
    permission_classes  = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class    = ScrapePageNumberPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        Scrape(serializer.instance, serializer.instance.id).process_results()
