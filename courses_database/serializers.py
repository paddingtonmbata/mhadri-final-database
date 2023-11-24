from rest_framework import serializers

from .models import *

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('country_name',)

class CourseDataSerializer(serializers.ModelSerializer):
    institution_location = serializers.CharField(source='institution_location.country_name')

    class Meta:
        model = CourseData
        fields = '__all__'

class CountryCourseCountSerializer(serializers.Serializer):
    country_name = serializers.CharField()
    course_count = serializers.IntegerField()
