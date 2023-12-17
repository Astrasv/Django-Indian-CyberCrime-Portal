from django.contrib import admin
from .models import State, City, Crime, Motive, Victim, Suspect, InvestigatingAgency, Investigator, CyberCrime

# Register your models
admin.site.register(State)
admin.site.register(City)
admin.site.register(Crime)
admin.site.register(Motive)
admin.site.register(Victim)
admin.site.register(Suspect)
admin.site.register(InvestigatingAgency)
admin.site.register(Investigator)
admin.site.register(CyberCrime)
