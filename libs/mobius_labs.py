import os
import json
import requests
import traceback
from libs.config import config



class MobiusLabs:
    def __init__(self, name, threshold):
        self.name = name
        self.threshold = threshold
        self.end_point = config.MOBIUS_END_POINT
        self.api_key = config.MOBIUS_API_KEY

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
                params = {
                    "modules": ["tags/standard_concepts"],
                    "tags": {
                        "standard_concepts": {
                            'confidence_threshold': self.threshold,
                            "categories_enabled": False,
                            "config_name": "default"
                        }
                    }
                }

                response = requests.post(f'{self.end_point}/image/predict',
                                         files={'data': open(image_path, 'rb')},
                                         data={'params': json.dumps(params)})

                response = response.json()

                image_output = []
                for concept in response['tags']['standard_concepts']:
                    print('%12s: %.2f' % (concept['name'], concept['score']))
                    image_output.append({
                        'name' : concept['name'],
                        'score': concept['score']
                    })
                output[id] = image_output
            except KeyboardInterrupt:
                return
            except Exception:
                print('Error', id, traceback.format_exc())

        with open(f'predictions/{self.name}.json', 'w') as f:
            f.write(json.dumps(output))

