from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser, Review, FlashcardDeck, Flashcard
from .serializers import CustomUserSerializer, ReviewSerializer, FlashcardDeckSerializer, FlashcardSerializer
from random import randint
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    if request.method == 'GET':
        user = request.user
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    
from .models import CustomUser

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def flashcard_deck_list_create(request):
    if request.method == 'GET':
        user = CustomUser.objects.get(id=request.user.id)  # Get the CustomUser instance
        flashcard_decks = FlashcardDeck.objects.filter(user=user)  # Use the CustomUser instance
        serializer = FlashcardDeckSerializer(flashcard_decks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        user = CustomUser.objects.get(id=request.user.id)  # Get the CustomUser instance
        serializer = FlashcardDeckSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)  # Use the CustomUser instance
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def flashcard_deck_retrieve_update_destroy(request, pk):
    try:
        flashcard_deck = FlashcardDeck.objects.get(pk=pk)
    except FlashcardDeck.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FlashcardDeckSerializer(flashcard_deck)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FlashcardDeckSerializer(flashcard_deck, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        flashcard_deck.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def flashcard_list_create(request):
    if request.method == 'GET':
        flashcards = Flashcard.objects.all()
        serializer = FlashcardSerializer(flashcards, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FlashcardSerializer(data=request.data)
        if serializer.is_valid():
            deck_id = request.data.get('deck')
            deck = FlashcardDeck.objects.get(pk=deck_id)
            serializer.save(deck=deck)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def flashcard_retrieve_update_destroy(request, pk):
    try:
        flashcard = Flashcard.objects.get(pk=pk)
    except Flashcard.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FlashcardSerializer(flashcard)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FlashcardSerializer(flashcard, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        flashcard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def flashcard_deck_flashcards(request, pk):
    try:
        flashcard_deck = FlashcardDeck.objects.get(pk=pk)
    except FlashcardDeck.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        flashcards = flashcard_deck.flashcards.all()
        serializer = FlashcardSerializer(flashcards, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_random_flashcard_for_review(request, deck_id):
    try:
        flashcard_deck = FlashcardDeck.objects.get(pk=deck_id)
    except FlashcardDeck.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        flashcards = flashcard_deck.flashcards.all()
        if not flashcards:
            return Response({"detail": "No flashcards found in the deck."}, status=status.HTTP_404_NOT_FOUND)

        random_flashcard = flashcards[randint(0, flashcards.count() - 1)]
        serializer = FlashcardSerializer(random_flashcard)
        return Response(serializer.data)
    
@api_view(['POST'])
def submit_flashcard_review(request, flashcard_id):
    try:
        flashcard = Flashcard.objects.get(pk=flashcard_id)
    except Flashcard.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        username = request.user.username
        user = User.objects.get(username=username)
        correct = request.data.get('correct')

        review, _ = Review.objects.get_or_create(user=user, flashcard=flashcard)
        if correct:
            review.correct_attempts += 1
        else:
            review.incorrect_attempts += 1
        review.save()

        user.total_cards_reviewed += 1
        if not flashcard.reviewed:
            user.unique_cards_reviewed += 1
            flashcard.reviewed = True
            flashcard.save()
        user.save()

        serializer = ReviewSerializer(review)
        return Response(serializer.data)