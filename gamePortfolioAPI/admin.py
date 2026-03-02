from django.contrib import admin
from gamePortfolioAPI.models import (
    Developer,
    Contact,
    Game,
    GameImage,
    Website,
    WebsiteImage,
)


# Serializers
class GameImageAdminSerializer(admin.ModelAdmin):
    list_display = ("game",)

    def display_game(self, obj):
        return obj.game.title


class WebsiteImageAdminSerializer(admin.ModelAdmin):
    list_display = ("website",)

    def display_website(self, obj):
        return obj.website.title


# Register your models here.
admin.site.register(Developer)
admin.site.register(Contact)
admin.site.register(Game)
admin.site.register(GameImage, GameImageAdminSerializer)
admin.site.register(Website)
admin.site.register(WebsiteImage, WebsiteImageAdminSerializer)
