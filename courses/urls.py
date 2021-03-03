from simplemooc.courses.views import index
from django.urls import include, path
urlpatterns = [
    
    #path('', include(('simplemooc.courses.views', 'simplemooc'), namespace='index')),
    path(r'^$', index , name='index'),

]