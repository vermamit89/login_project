from fastapi import APIRouter


router=APIRouter(tags=['Server'])

@router.get('/')
def start():
    return "server is live now"