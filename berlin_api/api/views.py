# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from .serializers import Food_Serializer
from .models import Food
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

# Generic view for get/post Suggestions_From_User
class Food_View(generics.ListCreateAPIView):

    queryset = Food.objects.all().order_by('-date')
    serializer_class = Food_Serializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()
