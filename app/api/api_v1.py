from fastapi import APIRouter

from app.api.v1.endpoints import (
    user,
    card,
    list,
    comment,
    workspace,
    workspace_user,
    card_user,
    login
)

router = APIRouter()


router.include_router(user.router, prefix="/user",  tags=["Users"])
router.include_router(workspace.router, prefix="/workspace", tags=["Workspace"])
router.include_router(card.router, prefix="/card",  tags=["Cards"])
router.include_router(list.router, prefix="/list", tags=["Lists"])
router.include_router(comment.router, prefix="/comment", tags=["Comments"])
router.include_router(workspace_user.router, prefix="/workspace_user", tags=["Workspace-User"])
router.include_router(card_user.router, prefix="/card_ser", tags=["Card-User"])
router.include_router(login.router, prefix="/login", tags=["Login"])