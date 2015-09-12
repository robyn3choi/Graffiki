from django.contrib import admin
from .models import Comment, Graffiti

admin.site.register(Graffiti)
admin.site.register(Comment)

