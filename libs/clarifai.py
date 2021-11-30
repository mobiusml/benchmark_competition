import os
import json
from libs.config import config

from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import service_pb2_grpc
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2


class Clarfia:
    def __init__(self):
        self.name = 'Clarifai'
        self.metadata = (('authorization', f'Key {config.CLARIFAI_API_KEY}'),)
        self.stub = service_pb2_grpc.V2Stub(ClarifaiChannel.get_grpc_channel())
        self.model_id = config.CLARIFAI_MODEL_ID

    def predict(self, image_id_list : list):
        total = len(image_id_list)
        counter = 0
        output = {}
        for id in image_id_list:
            counter += 1
            print(f'Predict {counter} from {total}')
            
            image_url = f'{config.BASE_URL}{id}'
            request = service_pb2.PostModelOutputsRequest(
                model_id=self.model_id,
                inputs=[
                    resources_pb2.Input(data=resources_pb2.Data(image=resources_pb2.Image(url=image_url)))
                ])
            
            try:
                response = self.stub.PostModelOutputs(request, metadata=self.metadata)

                if response.status.code != status_code_pb2.SUCCESS:
                    print("There was an error with your request!")
                    print("\tCode: {}".format(response.outputs[0].status.code))
                    print("\tDescription: {}".format(response.outputs[0].status.description))
                    print("\tDetails: {}".format(response.outputs[0].status.details))
                    raise Exception("Request failed, status code: " + str(response.status.code))

                image_output = []
                for concept in response.outputs[0].data.concepts:
                    print('%12s: %.2f' % (concept.name, concept.value))
                    image_output.append({
                        'name' : concept.name,
                        'score': concept.value
                    })
                output[id] = image_output
            except:
                print('Error', id)
        
        with open(f'predictions/{self.name}.json', 'w') as f:
            f.write(json.dumps(output))

