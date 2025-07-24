from django.urls import path

from . import views

app_name = 'vocabulary'

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('vocabulary-detail/<int:pk>/', views.VocabularyDetailView.as_view(), name="vocabulary_detail"),
    path('vocabulary-create/', views.VocabularyCreateView.as_view(), name="vocabulary_create"),
    path('vocabulary-update/<int:pk>/', views.VocabularyUpdateView.as_view(), name="vocabulary_update"),
    path('vocabulary-delete/<int:pk>/', views.VocabularyDeleteView.as_view(), name="vocabulary_delete"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
]