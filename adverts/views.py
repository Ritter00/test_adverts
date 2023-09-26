from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.response import Response


from adverts.serializers import *
from adverts.models import *


class AdvertViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
   
    def list(self, request):
        queryset = Advert.objects.all()
        serializer = AdvertSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Advert.objects.all()
        ad = get_object_or_404(queryset, pk=pk)
        try:
            ad.views += 1
            ad.save()
        except Exception as e:
            print(e)
        serializer = AdvertSerializer(ad)
        return Response(serializer.data)
   
snippet_list = AdvertViewset.as_view({
    'get': 'list',
})

snippet_detail = AdvertViewset.as_view({
    'get': 'retrieve',
})

class HomeView(TemplateView):
    template_name = 'main.html'
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        queryset = Advert.objects.all()
        ctx['objects'] = queryset.order_by('id')
        return ctx