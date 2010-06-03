from django.db import models

# Create your models here.
class Choices(models.Model):
    #qforeign = ManyToManyField('Questions',related_name="member choice",db_table="choices_to_questions")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Questions(models.Model):
    #mforeign = models.ManyToManyField('SModules',related_name="member question",db_table="questions_to_modules")
    choices = models.TextField(blank=True,null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Modules(models.Model):
    #sforeign = models.ManyToManyField('Surveys',related_name="member module",db_table="modules_to_surveys")
    questions = models.TextField()
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Surveys(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    modules = models.TextField()
    branches = models.TextField(blank=True,null=True)

class Branches(models.Model):
    #brach_to_survey = models.ManyToManyField('Surveys',related_name="member branch",db_table="branches_to_surveys")
    msource = models.PositiveIntegerField()
    qsource = models.PositiveIntegerField()
    csource = models.PositiveIntegerField()
    qsink = models.PositiveIntegerField()
    msink = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ChoiceCategories(models.Model):
    name = models.CharField(max_length=150)
    choices = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#To be created: surveys, question branching, choice categories.
#Unsure about: how the Django many-to-many relationship works, and whether it's worthwhile to include. It makes another table for each relationship, but I don't know what purpose that table serves, how to access it, what to use it for, etc.
