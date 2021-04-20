import re

from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Album, Artist, Song, UserSongs


class SongAdmin(admin.ModelAdmin):
    list_display = ("name", "artist", "album", "pub_year")


class AlbumAdmin(admin.ModelAdmin):
    list_display = ("name", "artist", "pub_year")


class ArtistAdmin(admin.ModelAdmin):
    list_display = ("name", "genre", "create_year", "picture", "get_image")

    def get_image(self, obj):
        img_src = re.sub(r"settings.MEDIA_ROOT/", "", f"{obj.picture.url}")
        return mark_safe(f'<img src={img_src} height="100px"')

    get_image.short_description = "Artist Picture"


admin.site.register(Song, SongAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(UserSongs)
