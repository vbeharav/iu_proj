from iu_proj.survey.models import Choices
from iu_proj.survey.models import Questions
from iu_proj.survey.models import Modules
from iu_proj.survey.models import ChoiceCategories
from iu_proj.survey.models import Surveys
from iu_proj.survey.models import Branches

from django.contrib import admin

admin.site.register(Choices)
admin.site.register(Questions)
admin.site.register(Modules)
admin.site.register(Surveys)
admin.site.register(Branches)
admin.site.register(ChoiceCategories)
