import pydantic
from datetime import datetime


class Note(pydantic.BaseModel):
    client_id: str
    user_id: str
    note: str
    create_at: datetime

