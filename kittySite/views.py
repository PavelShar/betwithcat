from __future__ import division
from django.shortcuts import render
from models import *

def index(request):
    # context = {
    #     'base_info': BaseInfo.objects.first(),
    #     'menus' : Menu.objects.all(),
    #     'areas' : Areas.objects.all(),
    #     'news' : News.objects.filter(published=True).order_by('-date'),
    #     'speakers' : Speakers.objects.all(),
    #     'topics' : TopicAreas.objects.all(),
    #     'dates' : ImportantDates.objects.all(),
    #     'footer' : Footer.objects.first(),
    #     'prog_com' : Organizers.objects.filter(Q(committee__contains='prog')),
    #     'org_com': Organizers.objects.filter(Q(committee__contains='org')),
    #     'publications' : Publications.objects.all(),
    #     'fees' : Fees.objects.all(),
    # }


    context = {
        'finishedGamesNum' : Game.objects.filter(finished=1).count(),
        'totalWinSum' : totalWinSum(),
        'winRate' : totalWinRate(),
        'looseRate' : 100 - totalWinRate(),
        'games' : Game.objects.all().order_by('datetime'),
    }
    return render(request, 'index.html', context)


def totalWinSum():
    games_objects = Game.objects.filter(finished=1)
    win_sum = 0
    for game in games_objects:
        win_sum = win_sum + game.getWinSum()
    return win_sum


def totalWinRate():
    games_total = Game.objects.filter(finished=1).count()
    if games_total == 0:
        return 0
    games_objects = Game.objects.filter(finished=1)
    games_wins = 0
    for game in games_objects:
        if game.catWasRight():
            games_wins = games_wins + 1
    return float("{0:.2f}".format(games_wins / games_total * 100))
