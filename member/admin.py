# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from django.contrib.auth.models import User, Group, GroupManager
from django.contrib.auth.admin import UserAdmin

from .models import Member,time


admin.site.register(Member)
admin.site.register(time)
admin.site.unregister(Group)