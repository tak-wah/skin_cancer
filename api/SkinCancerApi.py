import connexion

from src.classification.NNClassifier import NNClassifier
from src.classification.ClassifierResult import ClassifierResult
from src.common.Image import Image
from pathlib import Path

from typing import List, Dict, Any


# extends connexion.App
class SkinCancerApi(connexion.App):
    def __init__(self, import_name: str, specification_dir: str,
                 api_file: str, port: int,
                 classifier: NNClassifier) -> None:

        # call parent constructor
        connexion.App.__init__(self, import_name,
                               specification_dir=specification_dir,
                               port=port)

        self.__classifier = classifier
        self._api_file = Path(api_file)
        self.add_api(self._api_file,
                     resolver=self.function_resolver,
                     validate_responses=False)

    def function_resolver(self, operation_id: str):
        """
        Map the swagger operation_id to the function in this class.
        :param operation_id: operation id from swagger spec file
        :return: the corresponding function of the class
        """

        function_name = operation_id
        function = getattr(self, function_name)
        return function

    # our API endpoint
    def image_predict(self, images: List[Dict[str, Any]]) -> List[ClassifierResult]:
        images_to_process = [Image.from_dict(image) for image in images]
        return [self.__classifier.predict(image).to_dict for image in images_to_process]
