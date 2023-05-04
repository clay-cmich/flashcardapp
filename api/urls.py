from django.urls import path
from . import views

urlpatterns = [
    path('current-user/', views.current_user, name='current-user'),
    path('flashcard-decks/', views.flashcard_deck_list_create, name='flashcard-deck-list-create'),
    path('flashcard-decks/<int:pk>/', views.flashcard_deck_retrieve_update_destroy, name='flashcard-deck-retrieve-update-destroy'),
    path('flashcards/', views.flashcard_list_create, name='flashcard-list-create'),
    path('api/flashcard-decks/<int:pk>/flashcards/', views.flashcard_deck_flashcards, name='flashcard_deck_flashcards'),
    path('flashcards/<int:pk>/', views.flashcard_retrieve_update_destroy, name='flashcard-retrieve-update-destroy'),
    path('flashcard_deck/<int:deck_id>/random_review/', views.get_random_flashcard_for_review, name='get_random_flashcard_for_review'),
    path('flashcard/<int:flashcard_id>/submit_review/', views.submit_flashcard_review, name='submit_flashcard_review'),
]
