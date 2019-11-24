from django.urls import path, re_path

from . import views

app_name = 'demo'

urlpatterns = [
    path('', views.IndexView.as_view(), name='get_index'),
    #path('<int:year>-<int:month>-<int:day>', views.DateView.as_view(), name='get_date'),
    re_path('(?P<q_date>\d{4}-\d{2}-\d{2})', views.DateView.as_view(), name='get_date'),
    #path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.PublisherView.as_view(), name='get_publisher'),
]