from django.contrib import admin
from theme.models import Theme, Place
# Register your models here.

class PlaceInline(admin.StackedInline):
    model = Place

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    inlines = (PlaceInline,)
    list_display = ('id','theme_name' ,'map_img', 'graph_img', 'good','bad')

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id','place_name', 'map_img', 'graph_img', 'wordcloud_img','solutions')