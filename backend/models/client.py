from pydantic import BaseModel
from datetime import datetime

class Client(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    address: str
    created_at: datetime
    updated_at: datetime
    is_active: bool = True


