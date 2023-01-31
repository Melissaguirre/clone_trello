from typing import Any, Dict, Optional, Union, List
from app.models.users import Users
from app.schemas.users import UserCreate, UserUpdate
from app.crud.base import CRUDBase


class CRUDUser(CRUDBase[Users, UserCreate, UserUpdate]):
    ...

users = CRUDUser(Users)