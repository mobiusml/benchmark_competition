import os
from dotenv import load_dotenv
load_dotenv(".env")


class AppConfig:
	BASE_FOLDER = os.environ.get('BASE_FOLDER', 'data/unsplash-images/')
	BASE_URL = os.environ.get('BASE_URL', 'https://raw.githubusercontent.com/mobiusml/benchmark_competition/master/data/unsplash-images/')

	# Mobius
	MOBIUS_END_POINT = os.environ.get('MOBIUS_END_POINT')
	MOBIUS_API_KEY = os.environ.get('MOBIUS_API_KEY')

	# Clarifai
	CLARIFAI_END_POINT = os.environ.get('CLARIFAI_END_POINT', 'https://api.clarifai.com')
	CLARIFAI_MODEL_ID = os.environ.get('CLARIFAI_MODEL_ID', 'aaa03c23b3724a16a56b629203edc62c')
	CLARIFAI_API_KEY = os.environ.get('CLARIFAI_API_KEY')

	# Imagga
	IMAGGA_END_POINT = os.environ.get('CLARIFAI_END_POINT', 'https://api.imagga.com')
	IMAGGA_API_KEY = os.environ.get('IMAGGA_API_KEY')
	IMAGGA_API_SECRET = os.environ.get('IMAGGA_API_SECRET')

	# Microsoft
	MICROSOFT_END_POINT = os.environ.get('MICROSOFT_END_POINT')
	MICROSOFT_API_KEY = os.environ.get('MICROSOFT_API_KEY')

	# Google
	GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
	GOOGLE_APPLICATION_CREDENTIALS = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')

config = AppConfig()
