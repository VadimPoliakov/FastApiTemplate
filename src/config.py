import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)

basedir = Path(__file__).resolve().parent.parent

from environs import Env

env = Env()
env.read_env(f"{basedir}/vault/env")

tags_metadata = [
    {
        "name": "inquire",
    },
    {
        "name": "execution",
    },
]

info_app = {
    "title": "Project Title",
    "description": """Project Description 🚀""",
    "version": "0.1",
    "openapi_tags": tags_metadata,
}