import os
import django
from django.utils import timezone
from datetime import datetime
from faker import Faker
from django.db.utils import IntegrityError

# Initialize Django environment/ Set the settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jobs.settings")

#Set up Django
django.setup()

# Initialize Faker instance
fake = Faker()

# Import necessary models
from accounts.models import User
from jobsapp.models import Job, Applicant, Favorite
from tags.models import Tag

# Create a new User
def create_user():
    email = fake.email()

    # Check if a user with this email already exists
    if User.objects.filter(email=email).exists():
        print(f"User with email {email} already exists.")
        return None  # Or return the existing user, if preferred

    try:
        # Create a new user if the email doesn't exist
        user = User.objects.create_user(
            email=email,
            password="testpassword123",
            role="Employer",  # Example role
            gender="male"
        )
        print(f"User created: {user.email}")
        return user
    except IntegrityError:
        print(f"Error: User with email {email} already exists.")
        return None

# Create a few Tags
def create_tags():
    tag_names = ["Python", "Django", "Remote"]
    tags = []
    for name in tag_names:
        tag, created = Tag.objects.get_or_create(name=name)
        if created:
            print(f"Tag created: {tag.name}")
        tags.append(tag)
    return tags

# Create a new Job
def create_job(user, tags):
    if user is None:
        print("Error: Cannot create job without a valid user.")
        return None

    # Use timezone-aware datetime
    last_date = timezone.make_aware(datetime(2024, 12, 31), timezone.get_current_timezone())
    

    job = Job.objects.create(
        user=user,
        title="Senior Python Developer",
        description="We are looking for a senior Python developer...",
        location="New York",
        type="1",  # Full-time
        category="IT",
        last_date=last_date,
        company_name="Tech Corp",
        company_description="Leading tech company in the AI industry.",
        website="https://techcorp.com",
        salary=120000,
    )
    job.tags.set(tags)  # Set many-to-many relationship with tags
    print(f"Job created: {job.title}")
    return job

# Create an Applicant for a Job
def create_applicant(user, job):
    if user is None or job is None:
        print("Error: Cannot create applicant without valid user and job.")
        return None

    try:
        applicant = Applicant.objects.create(
            user=user,
            job=job,
            comment="I have over 5 years of experience with Python and Django.",
            status=1  # Pending
        )
        print(f"Applicant created for job: {job.title} by user: {user.email}")
        return applicant
    except IntegrityError:
        print(f"Error: Failed to create applicant for job: {job.title} due to user or job issue.")
        return None

# Create a Favorite job for a user
def create_favorite(user, job):
    if user is None or job is None:
        print("Error: Cannot create favorite without valid user and job.")
        return None

    try:
        favorite = Favorite.objects.create(
            user=user,
            job=job,
        )
        print(f"Favorite job added: {job.title} for user: {user.email}")
        return favorite
    except IntegrityError:
        print(f"Error: Failed to create favorite for job: {job.title} due to user or job issue.")
        return None

# from django.contrib.sites.models import Site
# Site.objects.create(domain='localhost', name='Localhost')

# Main function to call the insertion functions
if __name__ == "__main__":
    # Step 1: Create a User
    user = create_user()

    if user is None:
        print("Error: User creation failed. Exiting.")
        exit()

    # Step 2: Create Tags
    tags = create_tags()

    # Step 3: Create a Job and assign tags
    job = create_job(user, tags)

    if job is None:
        print("Error: Job creation failed. Exiting.")
        exit()

    # Step 4: Create an Applicant for the Job
    applicant_user = create_user()  # Create a different user to apply for the job

    if applicant_user is None:
        print("Error: Applicant creation failed. Exiting.")
        exit()

    create_applicant(applicant_user, job)

    # Step 5: Add the job to the user's favorites
    create_favorite(applicant_user, job)
