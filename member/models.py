# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytz
from django.db import models
# from timezone_field import TimeZoneField

# Create your models here.
class time(models.Model):
    """Model definition for time."""

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    class Meta:
        """Meta definition for time."""

        verbose_name = 'time'
        verbose_name_plural = 'times'

    def __str__(self):
        """Unicode representation of time."""
        return '{} {}'.format(self.start_time, self.end_time)

class Member(models.Model):
    """Model definition for Members."""

    id = models.CharField(primary_key=True,max_length=100)
    real_name = models.CharField(max_length=100)
    TIMEZONE = tuple(zip(pytz.all_timezones,pytz.all_timezones))
    tz = models.CharField(max_length=32,choices=TIMEZONE)
    activity_periods = models.ManyToManyField(time)
    

    class Meta:
        """Meta definition for Members."""

        verbose_name = 'Members'
        verbose_name_plural = 'Memberss'

    def __str__(self):
        """Unicode representation of Members."""

        return str(self.id)

    def to_dict(self):
        empty_dict=dict()
        return empty_dict