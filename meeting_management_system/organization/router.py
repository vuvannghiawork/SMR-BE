from fastapi import APIRouter, Depends, HTTPException, Request
from utils.BaseResponse import BaseResponse
from loguru import logger
from organization.schemas import (
    OrganizationCreate,
)
from organization.services import (
    filter_organizations,
    create_organization,
)
# from sqlalchemy.orm import Session
# from typing import List
# import services
# from schema import OrganizationCreate, Organization, OrganizationUpdate
# from database.session import get_db

prefix = "/organization"
tags = "organization"
router = APIRouter(prefix=prefix, tags=[tags])


@router.get("")
def get_organizations(
    request_: Request,
    id: int = None,
    name: str = None,
    email: str = None,
    address: str = None,
    phone_number: str = None,
):
    logger.info(f"Getting organizations with id: {id}, name: {name}, email: {email}, address: {address}, phone_number: {phone_number}")

    organizations = filter_organizations(id=id, name=name, email=email, address=address, phone_number=phone_number)

    return BaseResponse(
        success=True,
        message="Organizations fetched successfully",
        data=organizations
    )




 

@router.post("")
def post_organization(organizationCreate: OrganizationCreate):
    logger.info(f"Creating organization with data: {organizationCreate}")

    organization = create_organization(organizationCreate)
    
    return BaseResponse(
        success=True,
        message="Organization created successfully",
        data=organization
    )

# @router.put("/{org_id}",  
# def update_organization(org_id: int, org: OrganizationUpdate):
#     updated_org = services.update_organization(db, org_id, org)
#     if not updated_org:
#         raise HTTPException(status_code=404, detail="Organization not found")
#     return updated_org

# @router.delete("/{org_id}",  
# def delete_organization(org_id: int):
#     deleted_org = services.delete_organization(db, org_id)
#     if not deleted_org:
#         raise HTTPException(status_code=404, detail="Organization not found")
#     return deleted_org

