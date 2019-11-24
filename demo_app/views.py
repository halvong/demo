from django.shortcuts import render
from django.db.models import Sum
from django.views import View
from .models import RevenueRecord
from django.shortcuts import render, get_object_or_404

# Create your views here.

class IndexView(View):
    def get(self, request):
        revenue = RevenueRecord.objects.values('date').annotate(revenue_sum=Sum('revenue'), clicks_sum=Sum('clicks')).order_by('-date')
        #revenue = RevenueRecord.objects.annotate(revenue_sum=Sum('revenue'), clicks_sum=Sum('clicks')).order_by('-date')
        return render(request, 'index_template.html', {'dates': revenue})

class DateView(View):
    def get(self, request, q_date):
        print ("17date:",q_date)
        dates = RevenueRecord.objects.filter(date=q_date).values('publisher').annotate(revenue_sum=Sum('revenue'), clicks_sum=Sum('clicks')).order_by('publisher')
        return render(request, 'date_template.html', {'publishers': dates})

#class PublisherView(View):
#    def get(self, request):
#record = get_object_or_404(RevenueRecord, date__year=year, date__month=month, date__day=day)
#        queryset = RevenueRecord.objects.values('date').annotate(revenue=Sum('revenue'), clicks=Sum('clicks')).order_by('-date')
#        return render(request, 'publisher_template.html', {'dates': queryset})
