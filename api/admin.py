from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, FlashcardDeck, Flashcard

admin.site.register(CustomUser, UserAdmin)
admin.site.register(FlashcardDeck)
admin.site.register(Flashcard)

