from pydantic import BaseModel
from typing import Optional, Dict

class OrganizationBase(BaseModel):
    name: str
    address: str
    phone_number: str
    email: str
    meta_data: Optional[Dict] = None

class OrganizationCreate(OrganizationBase):
    pass

class Organization(OrganizationBase):
    id: int

class OrganizationUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    meta_data: Optional[Dict] = None