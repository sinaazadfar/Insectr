from django.contrib import admin
from .models import Child, LayerOne, LayerTwo, LayerThree, Category, Arthropod


class ChildAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class LayerThreeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class LayerTwoAdmin(admin.ModelAdmin):
    list_display = ('name',)


class LayerOneAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ArthropodAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Child, ChildAdmin)
admin.site.register(LayerThree, LayerThreeAdmin)
admin.site.register(LayerTwo, LayerTwoAdmin)
admin.site.register(LayerOne, LayerOneAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Arthropod, ArthropodAdmin)
