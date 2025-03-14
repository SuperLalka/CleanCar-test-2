from django.db import models

from app.utils.storages import MediaStorage
from app.utils.utils import get_str_uuid


class Image(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        auto_created=True,
        default=get_str_uuid
    )
    file = models.FileField(
        upload_to='files/images/',
        storage=MediaStorage(),
        blank=True,
        null=True,
    )

    class Meta:
        db_table = 'images'
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return str(self.uuid)

    @property
    def file_url(self):
        return str(self.image_file.url)
