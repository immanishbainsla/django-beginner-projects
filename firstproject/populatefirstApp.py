import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstproject.settings')

import django
django.setup()

## FAKE POP SCRIPT
import random
from firstApp.models import AccessRecoed,Topic,Webpage
from faker import Faker
fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def addtopic():
    t = Topic.objects.get_or_create(topname=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):

        # get the topic for the entry
        top = addtopic()

        # create the fake data for that entry
        fakeurl = fakegen.url()
        fakedate = fakegen.date()
        fakename = fakegen.company()

        # create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fakeurl,name=fakename)[0]

        # create the fake AccessRecoed for that webpage
        accrd = AccessRecoed.objects.get_or_create(name=webpg,date=fakedate)[0]

if __name__ == '__main__':
    print('populating script.')
    populate(20)
    print('populating complete.')
