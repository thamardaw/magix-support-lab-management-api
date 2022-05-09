from fastapi import APIRouter
from .routes import user,authentication,patient,test_category

router = APIRouter(prefix="/api")

router.include_router(user.router)
router.include_router(authentication.router)
router.include_router(patient.router)
router.include_router(test_category.router)
