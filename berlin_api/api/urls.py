# api/urls.py

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import Food_View
from django.conf import settings

urlpatterns = {

    url(r'^', Food_View.as_view(), name="food_list_view"),
    
}

urlpatterns = format_suffix_patterns(urlpatterns)
