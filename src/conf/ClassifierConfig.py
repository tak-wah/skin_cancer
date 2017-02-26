from typing import List


class ClassifierConfig:
    def __init__(self, base_model_name: str,
                 img_height: int, img_width: int, img_channels: int,
                 nb_classes: int, class_names: List[str],
                 weights_path: str) -> None:
        self.__base_model_name = base_model_name
        self.__img_height = img_height
        self.__img_width = img_width
        self.__img_channels = img_channels
        self.__nb_classes = nb_classes
        self.__class_names = class_names
        self.__weights_path = weights_path

    @property
    def base_model_name(self) -> str:
        return self.__base_model_name

    @property
    def img_height(self) -> int:
        return self.__img_height

    @property
    def img_width(self) -> int:
        return self.__img_width

    @property
    def img_channels(self) -> int:
        return self.__img_channels

    @property
    def nb_classes(self) -> int:
        return self.__nb_classes

    @property
    def class_names(self) -> List[str]:
        return self.__class_names

    @property
    def weights_path(self) -> str:
        return self.__weights_path
