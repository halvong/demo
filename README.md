#Setting up database
0. starts web and database:      docker-compose up -d
1. login to postgresql database: docker-compose run --rm database psql -U mike -h database
2. creates demo_app:             docker-compose exec web python manage.py startapp demo_app
3.                               docker-compose exec web python manage.py makemigrations demo_app
4.                               docker-compose exec web python manage.py migrate

#Django console to import data to database
0. starts web and database:  docker-compose up -d 
1.                           docker-compose exec web python manage.py shell
2. from demo_app.models import Publisher, Source, RevenueRecord
   from django.db.models import Sum 
3. Source.objects.bulk_create([Source(name="yahoo"),Source(name="google")])
4. Publisher.objects.bulk_create([Publisher(name="micha"),Publisher(name="mark"),Publisher(name="melanie"),Publisher(name="logan")])
execfile('generate_data.py')
5. RevenueRecord.objects.values('date').annotate(revenue=Sum('revenue'), clicks=Sum('clicks')).order_by('-date')
   dates = RevenueRecord.objects.filter(date="2019-10-31").annotate(revenue_sum=Sum('revenue'), clicks_sum=Sum('clicks')).order_by('publisher')
   publishers = RevenueRecord.objects.filter(date="2019-10-31",publisher=2).values('source').annotate(revenue_sum=Sum('revenue'), clicks_sum=Sum('clicks')).order_by('source')
