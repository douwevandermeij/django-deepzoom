'''django-deepzoom admin'''
from django.contrib import admin
from . import models


#===============================================================================


def delete_selected(self, request, queryset):
    '''
    Admin action that provides custom bulk delete for tricky classes.
    '''
    for obj in queryset:
        obj.delete()
#end delete_selected


class DeepZoomAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'slug', 'deepzoom_image', 'created',)
    actions = [delete_selected]
#end DeepZoomAdmin


#EOF django-deepzoom admin