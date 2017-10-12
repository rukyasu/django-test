import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'summary-project.settings')

import django
django.setup()

from myApp.models import User
from faker import Faker

fakegen = Faker()

def populate(count=5):


    for entry in range(count):
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        # New entry
        user = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]


if __name__ == '__main__':
    print("Populating database...")
    populate(20)
    print("Population completed!")
