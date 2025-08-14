# models.py
from typing import List, Optional
from pydantic import BaseModel

class Salary(BaseModel):
    program: str
    departments: List[str]
    specializations: List[str]
    amount: Optional[float]
    ctc: Optional[float]
    category: Optional[str]

class JobEnriched(BaseModel):
    companyName: str
    sector: Optional[str]
    aboutCompany: Optional[str]
    year: int
    season: str
    service: str
    jobDescription: str
    currency: str
    cpiCuttoff: float
    opensAt: Optional[str]
    closesAt: Optional[str]
    expectedOffers: int
    additionalInfo: Optional[str]
    title: str
    allowBonusApplications: bool
    location: str
    accommodaition: Optional[str]
    process: Optional[str]
    day: str
    slot: str
    startsAt: Optional[str]
    endsAt: Optional[str]
    salaries: List[Salary]
