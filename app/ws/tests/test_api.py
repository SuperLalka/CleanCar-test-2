import uuid

import pytest
import tempfile

from app.ws.models import Image
from app.ws.tests.conftest import TEST_HOST


class TestApiClass:

    @pytest.mark.parametrize(
        'url, method',
        [(
                f'{TEST_HOST}/api/images/',
                'get',
        )]
    )
    def test_api_list_images(self, client, url, method):
        r = getattr(client, method)(url)
        assert r.status_code == 200
        assert 'results' in r.json()
        assert r.json()['results'] == {}

    @pytest.mark.parametrize(
        'url, method',
        [(
                f'{TEST_HOST}/api/images/',
                'get',
        )]
    )
    def test_api_list_images(self, client, image, url, method):
        r = getattr(client, method)(url)
        assert r.status_code == 200
        assert 'results' in r.json()

        assert len(r.json()['results']) == 1
        assert r.json()['results'][0].get('uuid') == image.uuid
        assert r.json()['results'][0].get('file') == image.file.url

    @pytest.mark.parametrize(
        'url, method',
        [(
                f'{TEST_HOST}/api/images/{{uuid}}/',
                'get',
        )]
    )
    def test_api_retrieve_images(self, client, url, method):
        r = getattr(client, method)(url.format(uuid=str(uuid.uuid4())))
        assert r.status_code == 404

    @pytest.mark.parametrize(
        'url, method',
        [(
                f'{TEST_HOST}/api/images/{{uuid}}/',
                'get',
        )]
    )
    def test_api_retrieve_images(self, client, image, url, method):
        r = getattr(client, method)(url.format(uuid=image.uuid))
        assert r.status_code == 200
        assert r.json().get('uuid') == image.uuid
        assert r.json().get('file') == image.file.url

    @pytest.mark.parametrize(
        'url, method',
        [(
                f'{TEST_HOST}/api/images/',
                'post',
        )]
    )
    def test_api_create_images(self, client, url, method):
        r = getattr(client, method)(url)
        assert r.status_code == 400

    @pytest.mark.parametrize(
        'url, method',
        [(
                f'{TEST_HOST}/api/images/',
                'post',
        )]
    )
    def test_api_create_images(self, db, client, url, method):
        fp = tempfile.TemporaryFile()
        fp.write(b'Hello world!')

        r = getattr(client, method)(
            url,
            data={
                'file': fp
            }
        )

        fp.close()

        assert r.status_code == 201

    @pytest.mark.parametrize(
        'url, method',
        [(
                f'{TEST_HOST}/api/images/{{uuid}}/',
                'delete',
        )]
    )
    def test_api_destroy_images(self, client, url, method):
        r = getattr(client, method)(url.format(uuid=str(uuid.uuid4())))
        assert r.status_code == 404

    @pytest.mark.parametrize(
        'url, method',
        [(
                f'{TEST_HOST}/api/images/{{uuid}}/',
                'delete',
        )]
    )
    def test_api_destroy_images(self, db, client, image, url, method):
        image_obj_uuid = image.uuid
        r = getattr(client, method)(url.format(uuid=image.uuid))
        assert r.status_code == 204
        assert not r.data

        assert Image.objects.filter(uuid=image_obj_uuid).exists() is False
