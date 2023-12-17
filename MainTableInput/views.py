from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)


# For maps
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from .models import CyberCrime, State , Victim, Suspect, Investigator # Import your CyberCrime model
from .forms import CyberCrimeForm , VictimForm, SuspectForm, InvestigatorForm # Import the CyberCrimeForm


class CyberCreateView(LoginRequiredMixin,CreateView):
    model = CyberCrime
    form_class = CyberCrimeForm # Fields are already present in the forms created
    
    template_name = 'MainTableInput/main.html'
    success_url = '/'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class VictimCreateView(LoginRequiredMixin , CreateView):
    model = Victim
    form_class = VictimForm
    
    template_name = 'MainTableInput/AddVictim.html'
    success_url = '/'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class SuspectCreateView(LoginRequiredMixin , CreateView):
    model = Suspect
    form_class = SuspectForm
    
    template_name = 'MainTableInput/AddSuspect.html'
    success_url = '/'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class InvestigatorCreateView(LoginRequiredMixin, CreateView):
    model = Investigator
    form_class = InvestigatorForm
    
    template_name = 'MainTableInput/AddInvestigator.html'
    success_url = '/'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)




class CyberListView(LoginRequiredMixin, ListView):
    model = CyberCrime
    template_name = "MainTableInput/ListRecords.html"
    context_object_name = "records"
    ordering = ['-date_reported']

class VictimListView(LoginRequiredMixin, ListView):
    model = Victim
    template_name = "MainTableInput/ListVictims.html"
    context_object_name = "records"
    

class SuspectListView(LoginRequiredMixin, ListView):
    model = Suspect
    template_name = "MainTableInput/ListSuspects.html"
    context_object_name = "records"

class InvestigatorListView(LoginRequiredMixin, ListView):
    model = Investigator
    template_name = "MainTableInput/ListInvestigators.html"
    context_object_name = "records"





  
class CyberUpdateView(LoginRequiredMixin, UpdateView):
    model = CyberCrime
    template_name = "MainTableInput/UpdateRecord.html"
    form_class = CyberCrimeForm
    success_url = '/records/listrecords'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    
    
class VictimUpdateView(LoginRequiredMixin, UpdateView):
    model = Victim
    template_name = "MainTableInput/UpdateVictim.html"
    form_class = VictimForm
    success_url = '/records/listvictims'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class SuspectUpdateView(LoginRequiredMixin, UpdateView):
    model = Suspect
    template_name = "MainTableInput/UpdateSuspect.html"
    form_class = SuspectForm
    success_url = '/records/listsuspects'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class InvestigatorUpdateView(LoginRequiredMixin, UpdateView):
    model = Investigator
    template_name = "MainTableInput/UpdateInvestigator.html"
    form_class = InvestigatorForm
    success_url = '/records/listinvestigators'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    

class CyberDeleteView(LoginRequiredMixin,DeleteView):
    model = CyberCrime
    template_name = "MainTableInput/ConfirmDeletion.html"
    success_url = "/records/listrecords"

class VictimDeleteView(LoginRequiredMixin,DeleteView):
    model = Victim
    template_name = "MainTableInput/ConfirmDeletion.html"
    success_url = "/records/listvictims"

class SuspectDeleteView(LoginRequiredMixin,DeleteView):
    model = Suspect
    template_name = "MainTableInput/ConfirmDeletion.html"
    success_url = "/records/listsuspects"

class InvestigatorDeleteView(LoginRequiredMixin,DeleteView):
    model = Investigator
    template_name = "MainTableInput/ConfirmDeletion.html"
    success_url = "/records/listinvestigators"






# maps

@login_required
def crime_map(request):
    state_cybercrime_counts = (
        CyberCrime.objects
        .values('city__state__state_name')
        .annotate(total_count=Count('id'))
    )
    
    state_cybercrime_dict = {data['city__state__state_name']: data['total_count'] for data in state_cybercrime_counts}
    
    all_states = State.objects.values_list('state_name', flat=True)
    
    state_cybercrime_dict_template = {state.replace(' ', '_'): state_cybercrime_dict.get(state, 0) for state in all_states}
    
    return render(request, 'MainTableInput/crime_map.html', {'state_cybercrime_dict': state_cybercrime_dict_template})

