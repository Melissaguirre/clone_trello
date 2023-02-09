from app.models.cards import Cards
from app.schemas.cards import CardCreate, CardUpdate
from app.crud.base import CRUDBase


class CRUDCard(CRUDBase[Cards, CardCreate, CardUpdate]):
    ...
    

cards = CRUDCard(Cards)