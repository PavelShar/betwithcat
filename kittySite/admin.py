import logging

from django.contrib import admin
from .models import *

admin.site.register(Team)
admin.site.register(Game)
