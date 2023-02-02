from typing import Any, Dict, Optional, Union, List
from app.models.comments import Comments
from app.schemas.comments import CommentCreate, CommentUpdate
from app.crud.base import CRUDBase


class CRUDComment(CRUDBase[Comments, CommentCreate, CommentUpdate]):
    ...


comments = CRUDComment(Comments)
