import base64
import logging

from typing import Dict, Any

#contains the actual payload
class Image:
    def __init__(self, content: str = None, source: str = None) -> None:
        if content is not None:
            if content == '':
                msg = 'image content is empty'
                logging.error(msg)
                raise ValueError(msg)
            self._content = base64.b64decode(content)

        if content is None and source is not None:
            # TODO: retrieve from source (AWS S3, Google Cloud Storage)
            if self._validate_source(source):
                self._content = self._get_from_source(source)
            else:
                msg = "source '{0}' is invalid".format(source)
                logging.error(msg)
                raise ValueError(msg)

    @classmethod
    def from_dict(cls, dct: Dict[str, Any]) -> 'Image':
        content = dct['content'] if 'content' in dct else None
        source = dct['source'] if 'source' in dct else None
        return cls(content, source)

    @property
    def content(self) -> str:
        return self._content

    @property
    def content_b64(self) -> str:
        return base64.b64encode(self._content).decode('UTF-8')

    @staticmethod
    def _get_from_source(source: str) -> str:
        return ""

    @staticmethod
    def _validate_source(source: str) -> bool:
        return True
