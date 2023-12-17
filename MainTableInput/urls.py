from django.urls import path
from .views import (
    CyberCreateView, 
    CyberDeleteView,
    VictimCreateView ,
    SuspectCreateView,
    InvestigatorCreateView,
    CyberListView ,
    VictimListView,
    SuspectListView,
    InvestigatorListView,
    CyberUpdateView,
    VictimUpdateView,
    SuspectUpdateView,
    InvestigatorUpdateView,
    VictimDeleteView,
    SuspectDeleteView,
    InvestigatorDeleteView,
    
    crime_map
)

urlpatterns = [
    path('', CyberCreateView.as_view(), name='create-cybercrime'),
    path('listrecords', CyberListView.as_view(), name = 'list-cybercrime'),
    path('record/<int:pk>/update',CyberUpdateView.as_view(), name = 'update-cybercrime'),
    path('record/<int:pk>/delete',CyberDeleteView.as_view(), name = 'delete-cybercrime'),
    path('crimemap/',crime_map, name= "visualise-cybercrime"),
    path('victimrecord/',VictimCreateView.as_view() , name = 'create-victim'),
    path('suspectrecord/',SuspectCreateView.as_view() , name = 'create-suspect'),
    path('investigatorrecord/',InvestigatorCreateView.as_view() , name = 'create-investigator'),
    path('listvictims/',VictimListView.as_view() , name = 'list-victims'),
    path('listsuspects/',SuspectListView.as_view() , name = 'list-suspects'),
    path('listinvestigators/',InvestigatorListView.as_view() , name = 'list-investigators'),
    path('updatevictims/<int:pk>/update',VictimUpdateView.as_view() , name = 'update-victims'),
    path('updatesuspects/<int:pk>/update',SuspectUpdateView.as_view() , name = 'update-suspects'),
    path('updateinvestigators/<int:pk>/update',InvestigatorUpdateView.as_view() , name = 'update-investigators'),
    
    path('deletevictims/<int:pk>/delete',VictimDeleteView.as_view(), name = 'delete-victims'),
    path('deletesuspects/<int:pk>/delete',SuspectDeleteView.as_view(), name = 'delete-suspects'),
    path('deleteinvestigators/<int:pk>/delete',InvestigatorDeleteView.as_view(), name = 'delete-investigators'),
    
]
