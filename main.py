from important_functions import *

print(f"Your answer is {adding_2_numbers(2,3)}")

import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Access them using os.getenv
secret_key = os.getenv("api_key")
print(secret_key)