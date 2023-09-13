from django.urls import path
from . import views

urlpatterns=[
    path('',views.ListView.as_view(),name='home'),
    path('votes',views.VoteView.as_view(),name='votes'),
    path('results',views.Collective.as_view(),name='final')
]