import numpy as np

from io import BytesIO
from keras import applications
from keras import layers
from keras import models
from keras.preprocessing import image as image_utils
from keras.models import Model
from keras.layers import Input, Layer
from src.classification.ClassifierResult import ClassifierResult
from src.classification.NNClassifier import NNClassifier
from src.common.Image import Image


class MelanomaClassifier(NNClassifier):
    def predict(self, image: Image) -> ClassifierResult:
        # preprocessing
        img = image_utils.load_img(BytesIO(image.content),
                                   target_size=(self._config.img_width, self._config.img_height))
        img = image_utils.img_to_array(img)
        img = np.expand_dims(img, axis=0)

        # prediction
        probability = self._model.predict(applications.xception.preprocess_input(img)).flatten()
        predicted_class = np.argmax(probability)

        clf_result = ClassifierResult(
            self._config.class_names[predicted_class],
            float("{0:.2f}".format(probability[predicted_class]))
        )

        return clf_result

    def get_model(self, top_model_input_tensor: Layer, model_input_tensor: Input) -> Model:
        base_model_name = self._config.base_model_name

        if base_model_name == 'resnet50':
            x = layers.Flatten()(top_model_input_tensor)
        elif base_model_name == 'xception':
            x = layers.GlobalAveragePooling2D()(top_model_input_tensor)
        else:
            assert False, 'Classifier network not implemented for base model: {}.'.format(base_model_name)

        x = layers.Dense(1024)(x)
        x = layers.BatchNormalization()(x)
        x = layers.advanced_activations.LeakyReLU()(x)
        x = layers.Dropout(0.25)(x)

        if model_input_tensor is None:
            model_input_tensor = top_model_input_tensor

        x = layers.Dense(self._config.nb_classes, activation='softmax')(x)
        return models.Model(input=model_input_tensor, output=x)
