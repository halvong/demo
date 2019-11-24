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
5. from django.db.models import Sum
RevenueRecord.objects.values('date').annotate(revenue=Sum('revenue'), clicks=Sum('clicks')).order_by('-date')


 {% for rec in publishers %}
                <li><a href="">{{rec.publisher}}</a>, {{rec.revenue}}, {{rec.clicks}}</li>
            {% endfor %}