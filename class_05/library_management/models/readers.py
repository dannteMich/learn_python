from pydantic import BaseModel


class Reader(BaseModel):
    name: str
    identifier: str
