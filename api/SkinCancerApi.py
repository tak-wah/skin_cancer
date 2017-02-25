import connexion

from pathlib import Path


class SkinCancerApi(connexion.App):

    def __init__(self, import_name, specification_dir, api_file, port: int) -> None:
        connexion.App.__init__(self, import_name,
                               specification_dir=specification_dir,
                               port=port)

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

    def image_predict(self):
        return 'OK'
