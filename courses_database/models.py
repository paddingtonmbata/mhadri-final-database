from django.db import models

class Country(models.Model):
    country_name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=2)

    def __str__(self):
        return self.country_name
    
    

class TeachingMechanisms(models.TextChoices):
    ONLINE = 'Online', 'Online'
    FACETOFACE = "Face to Face", 'Face to Face'
    BOTH = 'Both', 'Both'

class CourseData(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    source = models.URLField(max_length=200)
    institution_name = models.CharField(max_length=100)
    institution_location = models.ForeignKey(Country, on_delete=models.CASCADE)
    type_of_course = models.CharField(max_length=200)
    thematic_focus = models.TextField()
    population_focus = models.CharField(max_length=100)#changed to population focus
    scope = models.TextField()
    objective_of_training = models.CharField(max_length=100)
    #faculty out
    teaching_mechanism = models.CharField(choices=TeachingMechanisms.choices, default=TeachingMechanisms.ONLINE, max_length=20)#changed to course medium
    methods_of_teaching = models.CharField(max_length=100)#changed to methods of teaching
    frequency_of_running_of_course = models.CharField(max_length=100)#changed to frequency of running of course/training
    funding_availability = models.TextField()#changed to Funding/Grants availability
    additional_details = models.TextField()#changed to additional details
    #out
    #out

    def __str__(self):
        return f"[{self.created_at}] {self.institution_name}, {self.institution_location} focusing on {self.thematic_focus}"