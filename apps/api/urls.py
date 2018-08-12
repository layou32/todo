from django.conf.urls import url
from .views import TodosViewSet
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^todos/$', TodosViewSet),
]

urlpatterns = format_suffix_patterns(urlpatterns)