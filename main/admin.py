from django.contrib import admin
from .models import Tutorial, TutorialSeries, TutorialCategory
from django.db import models
from tinymce.widgets import TinyMCE

# Register your models here.

class TutorialAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["tutorial_title", "tutorial_publish"]}),
        ("URL", {'fields': ["tutorial_slug"]}),
        ("Series", {'fields': ["tutorial_series"]}),
        ("Content", {"fields": ["tutorial_content"]})
    ]


    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
        }
        


admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)
admin.site.register(Tutorial,TutorialAdmin)