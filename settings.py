import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

PAGE_LINK = os.environ.get("PAGE_LINK")
MAIL_ADDRESSES = os.environ.get("MAIL_ADDRESSES")
PASSWORDS = os.environ.get("PASSWORDS")