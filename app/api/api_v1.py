from fastapi import APIRouter
from app.api.v1.endpoints import (
    user, 
    card, 
    lists, 
    workspace, 
    comment, 
    card_user,
    workspace_user,
    login
)


router = APIRouter()


router.include_router(user, tags="Users")
router.include_router(workspace)
router.include_router(card.router, prefix="/card")
router.include_router(lists.router)
router.include_router(comment)
router.include_router(workspace_user)
router.include_router(card_user)
router.include_router(route)