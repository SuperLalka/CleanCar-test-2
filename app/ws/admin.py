from django.contrib import admin
from django.utils.html import mark_safe

from app.utils.admin_forms import ImageForm
from app.ws.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    form = ImageForm
    fieldsets = (
        (
            'Object info',
            {'fields': ('uuid', 'file', 'image_tag')}
        ),
    )
    list_display = ['uuid', 'file', 'image_tag']
    readonly_fields = ['image_tag']
    search_fields = ['uuid']

    def image_tag(self, obj):
        url = obj.file.url
        return mark_safe(
            "<img src='{}' width='auto' height='200px' />".format(url)
        )

    image_tag.short_description = 'Image'
