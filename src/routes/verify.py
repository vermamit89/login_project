from fastapi import APIRouter,Depends
from ..models import database
from ..controllers import verify
from sqlalchemy.orm import Session

router=APIRouter(prefix='/verify', tags=["Verification"])

@router.get('/{uniqueId}')
def veryfy_email(uniqueId,db:Session=Depends(database.get_db)):
    return verify.verify_email(uniqueId,db)
    