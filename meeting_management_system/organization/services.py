from database.db import Session
from loguru import logger
from fastapi import HTTPException
from organization.models import Organization
from organization.schemas import OrganizationCreate


def filter_organizations(id: int = None, name: str = None, email: str = None, address: str = None, phone_number: str = None):
    logger.info(f"Filtering organizations with id: {id}, name: {name}, email: {email}, address: {address}, phone_number: {phone_number}")

    try:
        with Session() as session:
            query = session.query(Organization)
            if id:
                query = query.filter(Organization.id == id)
            if name:
                query = query.filter(Organization.name == name)
            if email:
                query = query.filter(Organization.email == email)
            if address:
                query = query.filter(Organization.address == address)
            if phone_number:
                query = query.filter(Organization.phone_number == phone_number)
            return query.all()
    except Exception as e:
        logger.error(f"Error filtering organizations: {e}")
        raise HTTPException(status_code=500, detail=str(e))


def create_organization(organizationCreate: OrganizationCreate):
    logger.info(f"Creating organization with data: {organizationCreate}")

    try:
        with Session() as session:
            organization_exists = session.query(Organization).filter(Organization.name == organizationCreate.name).first()
            print("🐍 File: organization/services.py | Line: 36 | create_organization ~ organization_exists",organization_exists)

            if organization_exists:
                print("🐍 File: organization/services.py | Line: 39 | create_organization ~ organization_exists",organization_exists)
                logger.error(f"Organization already exists: {organizationCreate.name}")
                raise HTTPException(
                    status_code=400,
                    detail=f"Organization already exists"
                )

            new_organization = Organization(**organizationCreate.model_dump())
            print("🐍 File: organization/services.py | Line: 47 | create_organization ~ organization",new_organization)

            session.add(new_organization)
            session.commit()
            session.refresh(new_organization)
            return new_organization
    except Exception as e:
        logger.error(f"Error creating organization: {e}")
        raise HTTPException(status_code=500, detail=str(e))
