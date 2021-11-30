import os
import json
import requests
import traceback
from libs.config import config
from google.cloud import vision


class GoogleCloudVision:
    def __init__(self):
        self.name = 'Google-Cloud-Vision'

        self.end_point = config.GOOGLE_API_KEY
        self.client = vision.ImageAnnotatorClient()

    def predict(self, image_id_list : list):
        total = len(image_id_list)
        counter = 0
        output = {}

        for id in image_id_list:
            counter += 1
            print(f'Predict {counter} from {total}')

            image_url = f'{config.BASE_URL}{id}'
            image_path = f'{config.BASE_FOLDER}{id}'

            try:
                image = vision.Image()
                image.source.image_uri = image_url

                response = self.client.label_detection(image=image)
                labels = response.label_annotations

                image_output = []
                for label in labels:
                    print('%12s: %.2f' % (label['description'], label['score']))
                    image_output.append({
                        'name' : label['description'],
                        'score': label['score']
                    })
                output[id] = image_output
            except KeyboardInterrupt:
                return
            except Exception:
                print('Error', id, traceback.format_exc())

        with open(f'predictions/{self.name}.json', 'w') as f:
            f.write(json.dumps(output))

