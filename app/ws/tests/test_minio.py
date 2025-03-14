from urllib.parse import urlparse

import pytest
from django.conf import settings
from minio import Minio


@pytest.mark.parametrize(
    'bucket',
    ['media', 'staticfiles']
)
def test_minio_required_buckets_exists(bucket):
    client = Minio(
        urlparse(settings.AWS_S3_ENDPOINT_URL).netloc,
        access_key=settings.AWS_ACCESS_KEY_ID,
        secret_key=settings.AWS_SECRET_ACCESS_KEY,
        region=settings.AWS_S3_REGION_NAME,
        secure=False
    )

    assert client.bucket_exists(bucket)
