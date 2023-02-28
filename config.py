import os
from dotenv import load_dotenv

if not load_dotenv():
    print(".env is not created!!!")

class Configure(object):
    SERVER_DOMAIN: str          = os.getenv("SERVER_DOMAIN", "localhost")
    SERVER_PORT: int            = int(os.getenv("SERVER_PORT", 5000))
    DEBUG: bool                 = os.getenv("DEBUG", False) == True or os.getenv("DEBUG", False) == "true"




