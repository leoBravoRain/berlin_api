# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import django

# Foods of Berlin
class Food(models.Model):

	# date
    date = models.DateTimeField(default=django.utils.timezone.now)
