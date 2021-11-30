import os
from libs.serve_request import ServerRequest
from libs.clarifai import Clarfia
from libs.imagga import Imagga
from libs.microsoft import Microsoft
from libs.google_cload_vision import GoogleCloudVision
from libs.aws_rekognition import AwsRekognition
from libs.mobius_labs import MobiusLabs

# Params
imageListPath = 'data/unsplash-images.txt'

image_id_list = []
with open(imageListPath) as f:
    image_id_list = f.read().splitlines()

# clarifai = Clarfia()
# clarifai.predict(image_id_list)

# microsift = Microsift()
# microsift.predict(image_id_list)

# googleCloudVision = GoogleCloudVision()
# googleCloudVision.predict(image_id_list)

# awsRekognition = AwsRekognition()
# awsRekognition.predict(image_id_list)

# mobiusLabs = MobiusLabs('MobiusLabs', 0.50)
# mobiusLabs.predict(image_id_list)

# mobiusLabs = MobiusLabs('MobiusLabs-Mobile-High-Threshold', 0.7)
# mobiusLabs.predict(image_id_list)

# mobiusLabs = MobiusLabs('MobiusLabs-Mobile-Mid-Threshold', 0.5)
# mobiusLabs.predict(image_id_list)

# mobiusLabs = MobiusLabs('MobiusLabs-Mobile-Low-Threshold', 0.3)
# mobiusLabs.predict(image_id_list)



