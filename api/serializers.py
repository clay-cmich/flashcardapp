from rest_framework import serializers
from .models import CustomUser, FlashcardDeck, Flashcard, Review

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'date_joined', 'days_reviewed', 'unique_cards_reviewed', 'total_cards_reviewed')
        
class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = '__all__'

class FlashcardDeckSerializer(serializers.ModelSerializer):
    flashcard_count = serializers.SerializerMethodField()

    class Meta:
        model = FlashcardDeck
        fields = ('id', 'title', 'user', 'flashcard_count')

    def get_flashcard_count(self, obj):
        return obj.flashcards.count()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
