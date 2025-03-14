from django.conf import settings
from storages.backends.s3 import S3Storage, S3StaticStorage


class MediaStorage(S3Storage):
    bucket_name = "media"

    def __init__(self, *args, **kwargs):
        if settings.DEBUG:
            self.secure_urls = False
            self.url_protocol = "http:"
            self.custom_domain = f"{settings.AWS_S3_ENDPOINT_LOCAL_DOMAIN}/{self.bucket_name}"
        super(MediaStorage, self).__init__(*args, **kwargs)


class StaticStorage(S3StaticStorage):
    bucket_name = "staticfiles"

    def __init__(self, *args, **kwargs):
        if settings.DEBUG:
            self.secure_urls = False
            self.url_protocol = "http:"
            self.custom_domain = f"{settings.AWS_S3_ENDPOINT_LOCAL_DOMAIN}/{self.bucket_name}"
        super(StaticStorage, self).__init__(*args, **kwargs)
