from iu_proj.survey.models import Choices
from iu_proj.survey.models import Questions
from iu_proj.survey.models import Modules
from iu_proj.survey.models import ChoiceCategories
from iu_proj.survey.models import Surveys
from iu_proj.survey.models import Branches

from django.contrib import admin

class SurveysAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Info', {'fields': ['name']}),
        ('Other Info', {'fields' : ['description', 'branches', 'modules']}),
        ]
    
class ModulesAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Info', {'fields': ['name']}),
        ('Other Info', {'fields' : ['description', 'questions']}),
        ]    

class ChoicesInline(admin.TabularInline):
    model = Choices
    extra = 4

class QuestionsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Info', {'fields': ['content']}),
    ]
    inlines = [ChoicesInline]
    
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Modules, ModulesAdmin)
admin.site.register(Surveys, SurveysAdmin)

