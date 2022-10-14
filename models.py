from redis_om import (EmbeddedJsonModel, Field, JsonModel)
from pydantic import NonNegativeInt
from typing import Optional, List

# We keep the models simple here
# Index the fields for easy searching
class User(EmbeddedJsonModel):
    name: str = Field(index=True)
    email: str = Field(index=True)

# A video can have  many likes and users
class Video(JsonModel):
    # Indexed for exact text matching
    title: str = Field(index=True)
    description: str = Field(index=True)
    uri: str = Field(index=True)

    likes: NonNegativeInt = Field()
    likedBy: List[User]
