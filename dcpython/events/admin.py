from django.contrib import admin
from dcpython.events.models import Presentation
from tinymce.widgets import TinyMCE
from django.db import models

class PresentationAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE},
    }
admin.site.register(Presentation, PresentationAdmin)