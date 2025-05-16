import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("YT_KEY")

DOWNLOADS_DIR = 'downloads'
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, 'captions')
VEDIOS_DIR = os.path.join(DOWNLOADS_DIR, 'vedios')
OUTPUTS_DIR = 'outputs'