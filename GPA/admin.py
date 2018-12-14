from django.contrib import admin
from .models import Semester, Term, Course

admin.site.register(Semester)
admin.site.register(Term)
admin.site.register(Course)