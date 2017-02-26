import os

from configparser import ConfigParser
from api.SkinCancerApi import SkinCancerApi as api
from src.classification.MelanomaClassifier import MelanomaClassifier
from src.conf.ClassifierConfig import ClassifierConfig


# entry point to fire up the app
def main():
    root_dir = os.path.dirname(os.path.realpath(__file__))
    parser = ConfigParser()
    parser.read(root_dir + '/config/application.conf')

    port = parser.getint('application', 'port', fallback=8080)

    config = ClassifierConfig(
        base_model_name=parser.get('classifier', 'base_model_name'),
        img_height=parser.getint('classifier', 'img_height'),
        img_width=parser.getint('classifier', 'img_width'),
        img_channels=parser.getint('classifier', 'img_channels'),
        nb_classes=parser.getint('classifier', 'nb_classes'),
        weights_path=parser.get('classifier', 'weights_path'),
        class_names=parser.get('classifier', 'class_names').split(',')
    )

    classifier = MelanomaClassifier(config)

    app = api(__name__, specification_dir=root_dir + '/swagger/',
              port=port,
              api_file='skin-cancer-api.yaml',
              classifier=classifier)
    app.run()


if __name__ == '__main__':
    main()
