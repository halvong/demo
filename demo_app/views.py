from django.shortcuts import render
from django.db.models import Sum
from django.views import View
from .models import RevenueRecord, Publisher, Source
from django.shortcuts import render, get_object_or_404
import datetime

# Create your views here.

class IndexView(View):
    def get(self, request):
        revenue = RevenueRecord.objects.values('date').annotate(revenue_sum=Sum('revenue'), clicks_sum=Sum('clicks')).order_by('-date')
        return render(request, 'index_template.html', {'dates': revenue})

class DateView(View):
    def get(self, request, q_date):
        ddate = datetime.datetime.strptime(q_date,"%Y-%m-%d").strftime("%B %d, %Y")
        #records = RevenueRecord.objects.filter(date=q_date).annotate(revenue_sum=Sum('revenue'), clicks_sum=Sum('clicks')).order_by('publisher')
        records = RevenueRecord.objects.filter(date=q_date).values('date', 'publisher','publisher__name').annotate(revenue_sum=Sum('revenue'), clicks_sum=Sum('clicks')).order_by('publisher__name')
        return render(request, 'date_template.html', {'publishers': records, 'q_date': ddate})

class PublisherView(View):
    def get(self, request, q_date, q_publisher):

        publisher = get_object_or_404(Publisher, id=q_publisher)

        ddate = datetime.datetime.strptime(q_date,"%Y-%m-%d").strftime("%B %d, %Y")
        publishers = RevenueRecord.objects.filter(date=q_date,publisher=q_publisher).values("source__name").annotate(revenue_sum=Sum('revenue'), clicks_sum=Sum('clicks')).order_by('source__name')
        return render(request, 'publisher_template.html', {'publishers': publishers, 'q_date': ddate, 'publisher': publisher})
