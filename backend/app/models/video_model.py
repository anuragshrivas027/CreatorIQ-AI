from pydantic import BaseModel
from pydantic import Field


class VideoRequest(BaseModel):

    url: str = Field(
        ...,
        min_length=5
    )