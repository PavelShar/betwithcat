# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from .helpers import *

@python_2_unicode_compatible
class Team(models.Model):
    title = models.CharField(max_length=255)
    photo = models.CharField(max_length=255)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Game(models.Model):
    teamA = models.ForeignKey(Team, related_name='teamA')
    teamB = models.ForeignKey(Team, related_name='teamB')
    datetime = models.DateTimeField()
    kA = models.FloatField('Team A Coefficient', default=0, blank=True)
    kB = models.FloatField('Team B Coefficient', default=0, blank=True)
    catChoice = models.CharField('Cat choice', max_length=255, blank=True, choices=(('', ''), ('A', 'Team A'), ('B', 'Team B')))
    scoreA = models.IntegerField('Score A', default=0, blank=True)
    scoreB = models.IntegerField('Score B', default=0, blank=True)
    betSum = models.IntegerField('Bet summ', default = 0, blank = True)
    link = models.URLField('Bet link', default = '', blank = True)
    finished = models.BooleanField(blank=True, default=False)


    def getWinSum(self):
        if self.scoreA > self.scoreB and self.catChoice == 'A' :
            return (self.betSum * self.kA) - self.betSum
        elif self.scoreB > self.scoreA and self.catChoice == 'B':
            return (self.betSum * self.kB) - self.betSum
        return -self.betSum


    def catWasRight(self):
        if self.scoreA > self.scoreB and self.catChoice == 'A':
            return True
        elif self.scoreB > self.scoreA and self.catChoice == 'B':
            return True
        return False

    def catWasRightAboutA(self):
        if self.scoreA > self.scoreB and self.catChoice == 'A':
            return True
        return False

    def catWasRightAboutB(self):
        if self.scoreB > self.scoreA and self.catChoice == 'B':
            return True
        return False


    def __str__(self):
        return self.teamA.title + ' - ' + self.teamB.title
