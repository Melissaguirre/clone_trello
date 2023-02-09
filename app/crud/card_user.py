from app.models.card_user import CardUsers
from app.schemas.card_users import CardUserCreate, CardUserUpdate
from app.crud.base import CRUDBase

class CRUDCardUser(CRUDBase[CardUsers, CardUserCreate, CardUserUpdate]):
    ...


card_users = CRUDCardUser(CardUsers)
