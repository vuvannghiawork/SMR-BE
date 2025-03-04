from fastapi import APIRouter
from organization.router import router as organization_router

index_router = APIRouter()
index_router.include_router(organization_router)
