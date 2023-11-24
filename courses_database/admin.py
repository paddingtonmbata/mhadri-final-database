from django.contrib import admin
from .models import CourseData

class CourseDataAdmin(admin.ModelAdmin):
    search_fields = ['institution_location__country_name', 'institution_name', 'type_of_course', 'thematic_focus']

admin.site.register(CourseData, CourseDataAdmin)

