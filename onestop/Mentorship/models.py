from datetime import datetime
from django.db import models
from Networking.models import Alumni_Profile,Student_Profile #Imported profiles from Networking 
from django.utils import timezone

class MentorshipModel(models.Model):
    # Fields specific to the Mentorship app
    MENTORSHIP_CHOICES = (
        ('Career', 'Career'),
        ('Course', 'Course'),
    )
    mentorship_type = models.CharField(
        max_length=10,
        choices=MENTORSHIP_CHOICES,
        default='Career',
    )

    # Now you can use NetworkingModel in your MentorshipModel
    networking_alumni_info = models.ForeignKey(Alumni_Profile, on_delete=models.CASCADE)
    networking_student_info = models.ForeignKey(Student_Profile, on_delete=models.CASCADE)
    # DateTimeField to store the date and time of the mentorship session
    mentorship_datetime = models.DateTimeField()




# Rating field for mentors, on a scale of 1-5
class MentorRating(models.Model):
    mentor_rating = models.DecimalField(
        max_digits=2,  # Total number of digits
        decimal_places=1,  # Number of decimal places
        default=1.0,  # Set a default value if needed
        )
    
# Custom method to set the date and time of the mentorship session
    def set_mentorship_datetime(self, year, month, day, hour, minute):
        
        self.mentorship_datetime = timezone.make_aware(
            datetime(year, month, day, hour, minute)
        )

#Function for the type of Mentorship
def set_mentorship_type(self, mentorship_type):
        if mentorship_type in dict(self.MENTORSHIP_CHOICES).keys():
            self.mentorship_type = mentorship_type
