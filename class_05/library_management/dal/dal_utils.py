from pydantic import BaseModel


import json
from pathlib import Path


def parse_models_from_file(file: Path, model: BaseModel):
    object_dicts = json.loads(file.read_text())
    objects = [model.model_validate(book_dict) for book_dict in object_dicts]

    return objects
