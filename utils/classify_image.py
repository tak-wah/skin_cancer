import sys
sys.path.append('./../')

import requests
import argparse
import base64

from typing import List

parser = argparse.ArgumentParser(description='Send an image for melanoma classification to host:port')
parser.add_argument('imagePath', type=str)
parser.add_argument('-host', type=str, default='localhost')
parser.add_argument('-port', type=int, default=8080)


class PredictApi:
    def __init__(self, host: str, port: int):
        self._predict_endpoint = 'http://{0}:{1}/melanoma/predict'.format(
            host, port)

    def predict(self, filenames: List[str]) -> None:
        images = []
        for filename in filenames:
            with open(filename, 'rb') as image_file:
                image = image_file.read()
                images.append(
                    {'content': base64.b64encode(image).decode('UTF-8')})

        r = requests.post(self._predict_endpoint, json=images)
        clf_results = r.json()

        print(clf_results)


def main(args):
    api = PredictApi(args.host, args.port)
    api.predict([args.imagePath])

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
