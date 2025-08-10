from fastapi import UploadFile, File
from pydantic import BaseModel


class ImageSchema(BaseModel):
    image: UploadFile = File(...)

    movie_id: int


class Image(ImageSchema):
    id: int


class ImageCreate(ImageSchema):
    pass
