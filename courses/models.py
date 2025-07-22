from django.db import models
import uuid

class FeaturedImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    altText = models.CharField(max_length=255, blank=True)
    source_url = models.URLField()
    height = models.PositiveIntegerField()
    width = models.PositiveIntegerField()

class InstructorPerson(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, db_index=True)
    role = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    linkedin_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    website_url = models.URLField(blank=True, null=True)

class Instructor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, db_index=True)
    featured_image = models.OneToOneField(FeaturedImage, on_delete=models.CASCADE)
    slug = models.SlugField()
    title = models.CharField(max_length=255)
    person = models.OneToOneField(InstructorPerson, on_delete=models.CASCADE)
    
class InstructorRole(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

class PlatFormEnName(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, db_index=True)
    en_name = models.CharField(max_length=255)

class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, db_index=True)
    featured_image = models.OneToOneField(FeaturedImage, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True)
    modified = models.DateTimeField(auto_now=True)

class ShortCourse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    primary_color = models.CharField(max_length=255)
    isprivate = models.CharField(max_length=255, blank=True)
    enroll_url = models.URLField()
    coming_soon = models.CharField(max_length=255, blank=True)
    hubspot_form_id = models.CharField(max_length=255)


