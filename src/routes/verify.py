from fastapi import APIRouter,Depends
import models.database,controllers.verify
from sqlalchemy.orm import Session

router=APIRouter(prefix='/verify', tags=["Verification"])

@router.get('/{uniqueId}')
def veryfy_email(uniqueId,db:Session=Depends(models.database.get_db)):
    return controllers.verify.verify_email(uniqueId,db)
    