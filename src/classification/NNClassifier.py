from abc import ABC, abstractmethod
from src.classification.ClassifierResult import ClassifierResult
from src.conf.ClassifierConfig import ClassifierConfig
from src.common.Image import Image
from keras import layers
from keras import applications
from keras.models import Model
from keras.layers import Input, Layer


class NNClassifier(ABC):
    def __init__(self, config: ClassifierConfig) -> None:
        self._config = config
        self._model = self.create_model()

    @abstractmethod
    def predict(self, image: Image) -> ClassifierResult:
        pass

    @abstractmethod
    def get_model(self, top_model_input_tensor: Layer, model_input_tensor: Input) -> Model:
        pass

    def create_model(self) -> Model:
        config = self._config

        base_model_input_tensor = layers.Input(shape=(config.img_height, config.img_width, config.img_channels))
        base_model = self.get_base_model(base_model_input_tensor, config.base_model_name)

        model_input_tensor = base_model_input_tensor
        top_model_input_tensor = base_model.output

        model = self.get_model(top_model_input_tensor, model_input_tensor=model_input_tensor)

        model.load_weights(config.weights_path)

        return model

    @staticmethod
    def get_base_model(input_tensor: Input, base_model_name: str) -> Model:
        if base_model_name == 'inception_v3':
            base_model = applications.inception_v3.InceptionV3(
                weights='imagenet',
                include_top=False,
                input_tensor=input_tensor)
        elif base_model_name == 'resnet50':
            base_model = applications.resnet50.ResNet50(
                weights='imagenet',
                include_top=False,
                input_tensor=input_tensor)
        elif base_model_name == 'xception':
            base_model = applications.xception.Xception(
                weights='imagenet',
                include_top=False,
                input_tensor=input_tensor)
        else:
            assert False, 'Invalid base model name: {}.'.format(base_model_name)

        return base_model
