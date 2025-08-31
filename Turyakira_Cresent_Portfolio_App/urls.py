from django.urls import path 
from.views import HomePage,AboutMePage,ProjectsPage,ServicesPage,ContactMe

urlpatterns=[
    path('',HomePage.as_view(),name='home'),
    path('aboutMe/',AboutMePage.as_view(),name='aboutMe'),
    path('projects/',ProjectsPage.as_view(),name='projects'),
    path('services/',ServicesPage.as_view(),name='services'),
    path('contactMe/',ContactMe.as_view(),name='contactMe'),
]