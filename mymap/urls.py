
from django.urls import path

from mymap.views import MymapIndexView

app_name = 'mymap'

urlpatterns = [
    path('', MymapIndexView.as_view(), name='mymap_index'),
]
