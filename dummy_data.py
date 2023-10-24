import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

django.setup()

from faker import Faker
import random
from job.models import Job, Company, Category


def create_category(n):
    fake = Faker()
    for x in range(n):
        Category.objects.create(
            name = fake.name()
        )
    print(f"{n} category was added successfully")



def create_company(n):
    fake = Faker() 
    images = [ 'job-list1.png','job-list2.png', 'job-list3.png','job-list4.png' ]
    for x in range(n):
        Company.objects.create(
            name = fake.name(),
            subtitle = fake.text(),
            website = fake.url(),
            email = fake.email(),
            logo = f"company/{ images[random.randint(0,3)] }"
        )
    print(f"{n} company was added successfully")



def create_job(n):
    fake = Faker()
    job_type = [ 'FullTime', 'PartTime', 'Remote', 'Freelance' ]
    for x in range(n):
        Job.objects.create(
            title = fake.name(),
            company = Company.objects.all().order_by('?')[0], 
            salary_start = random.randint(2000,2500), 
            salary_end = random.randint(2300,2800), 
            description = fake.sentence(), 
            vacancy = random.randint(1,5), 
            job_type = job_type[random.randint(0,3)], 
            experience = random.randint(1,10), 
            category = Category.objects.all().order_by('?')[0]
        )
    print(f"{n} job was added successfully")

create_category(5)
create_company(100)
create_job(2000)