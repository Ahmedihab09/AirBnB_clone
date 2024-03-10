#!/user/bin/python3
from base_model import BaseModel

class Review(BaseModel):
    """
    Review class that inherits from BaseModel.
    """
    place_id = ""
    user_id = ""
    text = ""