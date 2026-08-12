import os

from dotenv import load_dotenv

# Load .env first, then override with .env.{ENV} when present.
load_dotenv()

ENV = os.getenv('ENV', 'development')
env_path = f'.env.{ENV}'

if os.path.exists(env_path):
    load_dotenv(env_path, override=True)
