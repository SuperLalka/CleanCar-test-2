
from factory import Faker
from factory.django import DjangoModelFactory

from app.ws.models import Image


class ImageFactory(DjangoModelFactory):
    class Meta:
        model = Image

    uuid = Faker("uuid4")
    file = Faker("image_url")
