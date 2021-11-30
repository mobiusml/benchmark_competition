import os
import json
import requests
import traceback
from libs.config import config

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials


class Microsoft:
    def __init__(self):
        self.name = 'Microsoft'

        self.end_point = config.MICROSOFT_END_POINT
        self.api_key = config.MICROSOFT_API_KEY
        self.client = ComputerVisionClient(self.end_point, CognitiveServicesCredentials(self.api_key))

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
                response = self.client.tag_image(image_url) 
                image_output = []
                for tag in response["tags"]:
                    print('%12s: %.2f' % (tag['name'], tag['confidence']))
                    image_output.append({
                        'name' : tag['name'],
                        'score': tag['confidence']
                    })
                output[id] = image_output
            except KeyboardInterrupt:
                return
            except Exception:
                print('Error', id, traceback.format_exc())

        with open(f'predictions/{self.name}.json', 'w') as f:
            f.write(json.dumps(output))

