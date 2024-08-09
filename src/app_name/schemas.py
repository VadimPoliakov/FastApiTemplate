from pydantic import BaseModel
from datetime import datetime


class Videos(BaseModel):
    """Validate request data"""

    id: int
    uid: str
    path: str
    name_video: str
    date_creation: datetime
    status: str


