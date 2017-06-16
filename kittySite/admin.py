import logging

from django.contrib import admin
from .models import *


class GamesAdmin(admin.ModelAdmin):
    list_display = ('teamA', 'teamB', 'datetime', 'catChoice', 'scoreA', 'scoreB', 'betSum', 'finished', 'catWasRight')
    list_filter = ['datetime', 'catChoice', 'finished']
    list_display_links = (['teamA', 'teamB'])

    def teamA(self, obj):
        return self.team_a.title

    def teamB(self, obj):
        return self.team_b.title


admin.site.register(Team)
admin.site.register(Game, GamesAdmin)
