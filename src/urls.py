from django.urls import path

from . import views

urlpatterns = [
    path('phrasal_verbs/', views.PhrasalVerbsView.as_view(), name='phrasalverbs_list'),
]