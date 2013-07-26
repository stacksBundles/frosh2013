from django.db import models
from django.contrib.auth.models import User

# Create your models here.



    
class Sponsor(models.Model):

    title = models.CharField(max_length = 500)

    logo = models.ImageField(upload_to ="logos")

    rank = models.IntegerField()

    link = models.URLField(max_length = 500, blank = True, null = True)

    def __unicode__(self):

        slug = self.title[:10]

        return slug
    
class House(models.Model):

    house_name = models.CharField(max_length = 140)

    house_crest = models.ImageField(upload_to = "images", default = "static/images/crest.gif")

    user = models.ForeignKey(User, default=1)

    def __unicode__(self):

        return self.house_name

class Image(models.Model):

    image = models.ImageField(upload_to = "static", default = "cake.png")

    tag = models.CharField(max_length = 140)

    vassal = models.ForeignKey("Vassal", null=True, editable = False)

    page = models.ForeignKey("House", default=1, editable = False)

    def __unicode__(self):
        return self.tag

class Vassal(models.Model):

    SIR = "Sir"
    QUEEN = "Queen"
    KING = "King"
    LORD = "Lord"
    LADY = "Lady"
    PRIEST = "Priest"
    PRIESTESS = "Priestess"
    PRINCE = "Prince"
    PRINCESS = "Princess"
    SEER = "Seer"
    WARLORD = "Warlord"
    WARLADY = "Warlady"
    DRAGON = "Dragon"

    TITLE_CHOICES = (
        (SIR, 'Sir'),
        (QUEEN, 'Queen'),
        (KING, 'King'),
        (LORD, 'Lord'),
        (LADY, 'Lady'),
        (PRIEST, 'Priest'),
        (PRIESTESS, 'Priestess'),
        (PRINCESS, 'Princess'),
        (PRINCE, 'Prince'),
        (SEER, 'Seer'),
        (WARLORD, 'Warlord'),
        (WARLADY, 'Warlady'),
        (DRAGON, 'Dragon'),
        
    )
        
    title = models.CharField(max_length = 9, choices = TITLE_CHOICES)

    name = models.CharField(max_length = 140, default = "undefined")

    horse_name = models.CharField(max_length = 20, default = "undefined")

    favorite_event = models.CharField(max_length = 140, default = "undefined")

    house = models.ForeignKey("House", editable=False)

    def __unicode__(self):

        return self.name

    
    
