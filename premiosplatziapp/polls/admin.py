from django.contrib import admin

#mymodels
from .models import Question, Choice

admin.site.register(Question)
