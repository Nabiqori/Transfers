from django.contrib import admin
from .models import *
from django.utils.html import format_html

class SeasonAdmin(admin.ModelAdmin):
    search_fields = ["name"]

class CountryAdmin(admin.ModelAdmin):
    search_fields = ["name"]

class ClubAdmin(admin.ModelAdmin):
    list_display = ["name","image_tag","president", "coach", "found_date", "country"]
    list_filter = ["country"]
    search_fields = ["name","president", "coach",]
    ordering = ["name",]
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 32px; height: 32px;" />', obj.image.url)
        return "Rasm yo'q"

    image_tag.short_description = 'Rasm'

class PlayerAdmin(admin.ModelAdmin):
    list_display = ["name","age", "position",  "country","price", "club"]
    list_filter = ["country","club","position","age"]
    search_fields = ["name"]
    ordering = ["name","price"]

class TransferAdmin(admin.ModelAdmin):
    list_display = ["player","club_from", "club_to", "season", "price","datetime"]
    list_filter = ["player","club_from","club_to","season","datetime"]
    ordering = ["datetime",]
    search_fields = ["player__name"]


admin.site.register(Season, SeasonAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Transfer, TransferAdmin)