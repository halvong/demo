import random
from datetime import datetime
from demo_app.models import Publisher, Source, RevenueRecord

publishers = [ 'micha', 'mark', 'melanie', 'logan']
sources = ['yahoo', 'google']

print('date,pub_name,source,clicks,revenue')
idx = 0
for i in range(1,32):
    d = datetime(2019,10,i).date()
    for pub, _ in enumerate(publishers):
        pub += 1
        source = random.randint(0,1)
        source += 1
        clicks = random.randint(20,500)
        revenue = '{:0.2f}'.format(clicks*(random.randint(0,150)/150) )
        print('{}. {},{},{},{},{}'.format(idx, d, pub, source, clicks, revenue))
        RevenueRecord.objects.create(date=d, clicks=clicks, revenue=revenue, publisher_id=pub, source_id=source)
        idx += 1