import os

from dotenv import load_dotenv
# 默认加载cwd下的.env
load_dotenv()
ENV = os.getenv('ENV', 'development')
env_path = f'.env.{ENV}'
if os.path.exists(env_path):
    # 加载对应环境的环境变量
    load_dotenv(env_path, override=True)