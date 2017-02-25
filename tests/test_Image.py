import pytest
import base64
import os

from src.common.Image import Image

test_image_filename = os.path.dirname(__file__) + '/resources/test_image.jpg'


def test_create_image_from_content():
    with open(test_image_filename, 'rb') as image_file:
        test_image = image_file.read()

    image_b64 = base64.b64encode(test_image).decode('UTF-8')

    image = Image(content=image_b64)

    assert image.content == base64.b64decode(image_b64)
    assert image.content_b64 == image_b64


def test_create_image_from_source():
    image = Image(source='some link')

    assert image.content == ""


def test_create_image_from_content_source():
    with open(test_image_filename, 'rb') as image_file:
        test_image = image_file.read()

    image_b64 = base64.b64encode(test_image).decode('UTF-8')

    image = Image(content=image_b64,
                  source="some link")

    assert image.content == base64.b64decode(image_b64)
    assert image.content_b64 == image_b64


def test_from_dict():
    with open(test_image_filename, 'rb') as image_file:
        test_image = image_file.read()

    image_b64 = base64.b64encode(test_image).decode('UTF-8')

    test_dict = {
        'content': image_b64,
        'source': "some link"
    }

    image = Image.from_dict(test_dict)

    assert image.content == base64.b64decode(image_b64)
    assert image.content_b64 == image_b64


def test_invalid_content():
    with pytest.raises(ValueError) as exception:
        Image(content='')

    assert 'image content is empty' == str(exception.value)
