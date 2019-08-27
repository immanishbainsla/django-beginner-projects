import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','protwo.settings')

import django
django.setup()

from apptwo.models import users
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fakename = fakegen.name().split()
        fakefirstname = fakename[0]
        fakelastname = fakename[1]
        fakeemail = fakegen.email()

        # new entry
        user = users.objects.get_or_create(firstname = fakefirstname, lastname = fakelastname, email = fakeemail)[0]

if __name__ == '__main__':
    print('Populating Databases')
    populate(20)
    print('Populating Complete')
