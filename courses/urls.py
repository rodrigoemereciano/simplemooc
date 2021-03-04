from simplemooc.courses.views import details
from simplemooc.courses.views import index
from django.urls import path, re_path


urlpatterns = [
    
    #path('', include(('simplemooc.courses.views', 'simplemooc'), namespace='index')),
    path('', index , name='index'),
    re_path((r'^(?P<pk>\d+)/$'), details , name='details'),

]