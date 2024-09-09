from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from electricvehicle_charging_control.dependencies import CommonQueryParams, get_db
from electricvehicle_charging_control.services import VehicleService

router = APIRouter()

_service = VehicleService()

@router.get('/vehicles')
def get(
        session: Session = Depends(get_db),
        commons: CommonQueryParams = Depends()
):
    return _service.get(session, offset=commons.offset, limit=commons.limit)


@router.get('/vehicles/{id}')
def get_by_id(
        id: int,
        session: Session = Depends(get_db)
):
    return _service.get_by_id(session, id)
