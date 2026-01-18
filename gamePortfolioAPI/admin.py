from django.contrib import admin
from gamePortfolioAPI.models import Developer, Contact, Game, GameImage


# Serializers
class GameImageAdminSerialzer(admin.ModelAdmin):
    list_display = ("game",)

    def display_game(self, obj):
        return obj.game.title


# Register your models here.
admin.site.register(Developer)
admin.site.register(Contact)
admin.site.register(Game)
admin.site.register(GameImage, GameImageAdminSerialzer)
