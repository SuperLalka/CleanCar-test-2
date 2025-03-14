import sys
import xml.etree.cElementTree as et
from io import BytesIO

from django.core.exceptions import ValidationError
from django.core.validators import (
    FileExtensionValidator,
    get_available_image_extensions,
)
from django.forms import ImageField as DjangoImageField
from PIL import Image


def validate_image_and_svg_file_extension(value):
    allowed_extensions = get_available_image_extensions() + ["svg"]
    return FileExtensionValidator(allowed_extensions=allowed_extensions)(value)


class SVGAndImageFormField(DjangoImageField):
    default_validators = [validate_image_and_svg_file_extension]

    def to_python(self, data):
        test_file = super(DjangoImageField, self).to_python(data)
        if test_file is None:
            return None

        if hasattr(data, "temporary_file_path"):
            ifile = data.temporary_file_path()
        else:
            if hasattr(data, "read"):
                ifile = BytesIO(data.read())
            else:
                ifile = BytesIO(data["content"])

        try:
            image = Image.open(ifile)
            image.verify()

            test_file.image = image
            test_file.content_type = Image.MIME[image.format]
        except Exception:
            if not self.is_svg(ifile):
                raise ValidationError(
                    self.error_messages["invalid_image"], code="invalid_image",
                ).with_traceback(sys.exc_info()[2])
        if hasattr(test_file, "seek") and callable(test_file.seek):
            test_file.seek(0)
        return test_file

    def is_svg(self, f):
        f.seek(0)
        tag = None
        try:
            for event, el in et.iterparse(f, ("start",)):
                tag = el.tag
                break
        except et.ParseError:
            pass
        return tag == "{http://www.w3.org/2000/svg}svg"
