from django.contrib import admin
from polls.models import Question,Choice



class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldset = [
                    (None,                    {'fields' : ['question_text'] }),
                    ('date information',      {'fields' : ['pub_date'], 'classes': ['collapse'] })
            ]
    inlines = [ChoiceInline]

admin.site.register(Question,QuestionAdmin)
