import boto3
import base64
import json
import requests
import traceback
from libs.config import config


class AwsRekognition:
    def __init__(self):
        self.name = 'AWS-Rekognition'

        self.min_confidence = 7
        self.max_labels = 30

        self.aws_access_key_id = config.AWS_ACCESS_KEY
        self.aws_secret_access_key = config.AWS_SECRET_KEY
        
        self.client = boto3.client('rekognition')

    def predict(self, image_id_list : list):
        total = len(image_id_list)
        counter = 0
        output = {}

        for id in image_id_list:
            counter += 1
            print(f'Predict {counter} from {total}')

            image_url = f'{config.BASE_URL}{id}'
            image_path = f'{config.BASE_FOLDER}{id}'
            
            with open(image_path, "rb") as image_file:
                base64_image=base64.b64encode(image_file.read())
                base_64_binary = base64.decodebytes(base64_image)

            try:
                response = self.client.detect_labels(
                    Image={
                        'Bytes': base_64_binary
                    },
                    MaxLabels= self.max_labels,
                    MinConfidence= self.min_confidence,
                    )
                labels = response['Labels']
                print(labels)
                image_output = []
                for label in labels:
                    print('%12s: %.2f' % (label['Name'], label['Confidence']))
                    image_output.append({
                        'name' : label['Name'],
                        'score': label['Confidence'] / 100.
                    })
                output[id] = image_output
            except KeyboardInterrupt:
                return
            except Exception:
                print('Error', id, traceback.format_exc())

        with open(f'predictions/{self.name}.json', 'w') as f:
            f.write(json.dumps(output))
