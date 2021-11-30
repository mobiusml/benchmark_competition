import os
import json
import requests
import traceback
from libs.config import config



class Imagga:
    def __init__(self):
        self.name = 'Imagga'

        self.end_point = config.IMAGGA_END_POINT
        self.api_key = config.IMAGGA_API_KEY
        self.api_secret = config.IMAGGA_API_SECRET

    def predict(self, image_id_list : list, with_url=True):
        total = len(image_id_list)
        counter = 0
        output = {}
        for id in image_id_list:
            counter += 1
            print(f'Predict {counter} from {total}')

            image_url = f'{config.BASE_URL}{id}'
            image_path = f'{config.BASE_FOLDER}{id}'

            try:
                if with_url:
                    response = requests.get(
                        f'{self.end_point}/v2/tags?image_url={image_url}',
                        auth=(self.api_key, self.api_secret))
                else:
                    response = requests.post(
                        f'{self.end_point}/v2/tags',
                        auth=(self.api_key, self.api_secret),
                        files={'image': open(image_path, 'rb')})

                response = response.json()
                if "result" not in response:
                    print("Error", response)

                image_output = []
                for concept in response["result"]["tags"]:
                    name = concept['tag']['en']
                    score = concept['confidence'] / 100.
                    print('%12s: %.2f' % (name, score))
                    image_output.append({
                        'name' : name,
                        'score': score
                    })
                output[id] = image_output
            except KeyboardInterrupt:
                return
            except Exception:
                print('Error', id, traceback.format_exc())

        with open(f'predictions/{self.name}.json', 'w') as f:
            f.write(json.dumps(output))

