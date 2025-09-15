import pydantic
from datetime import datetime


class User(pydantic.BaseModel):
    username: str
    email: str
    hashed_password: str
    created_at: datetime
    is_admin: bool = False


# Testeando modelo
def test_drive_user(dataset: dict) -> None:
    """
    Validamos que la implementación del modelo sea la correcta en base al class model creado en Pydantic
    Args:
        dataset: diccinario con los datos del modelo

    Returns:
        None: La función sólo imprime mensaje en pantalla con el modelo validado o con el error generado.
    """
    try:
        user: User = User(**dataset)
        print(user)

    except Exception as e:
        print(e)

data = {
        "username": "mrGoonies",
        "email": "gooniesdev@gmail.com",
        "hashed_password": "test122",
        "created_at": datetime.today().strftime('%Y-%m-%d-%H:%M:%S'),
        "is_admin": True
        }

test_drive_user(data)
