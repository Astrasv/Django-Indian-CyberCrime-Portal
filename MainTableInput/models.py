from django.db import models

# Create your models here.
from django.db import models

class State(models.Model):
    state_name = models.CharField(max_length=255)

class City(models.Model):
    city_name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.city_name

class Crime(models.Model):
    crime_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.crime_name

class Motive(models.Model):
    motive_description = models.TextField()
    def __str__(self):
        return self.motive_description

class Victim(models.Model):
    victim_name = models.CharField(max_length=255)
    age = models.IntegerField(null=True, blank=True)
    
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    
    contact_info = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):  
        return self.victim_name

class Suspect(models.Model):
    suspect_name = models.CharField(max_length=255)
    age = models.IntegerField(null=True, blank=True)
    
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    
    
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.suspect_name

class InvestigatingAgency(models.Model):
    agency_name = models.CharField(max_length=255)
    headquarters_location = models.CharField(max_length=255)
    
    def __str__(self):
        return self.agency_name

class Investigator(models.Model):
    investigator_name = models.CharField(max_length=255)
    badge_number = models.CharField(max_length=20)
    contact_info = models.CharField(max_length=255, null=True, blank=True)
    agency = models.ForeignKey(InvestigatingAgency, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.investigator_name

class CyberCrime(models.Model):
    description = models.TextField()
    date_reported = models.DateField()
    city = models.ForeignKey(City,on_delete=models.CASCADE, null=True, blank=True)
    crime = models.ForeignKey(Crime, on_delete=models.CASCADE, null=True, blank=True)
    motive = models.ForeignKey(Motive, on_delete=models.CASCADE, null=True, blank=True)
    victim = models.ForeignKey(Victim, on_delete=models.CASCADE, null=True, blank=True)
    suspect = models.ForeignKey(Suspect, on_delete=models.CASCADE, null=True, blank=True)
    investigator = models.ForeignKey(Investigator, on_delete=models.CASCADE, null=True, blank=True)

