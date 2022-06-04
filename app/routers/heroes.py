from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from starlette.status import HTTP_201_CREATED, HTTP_401_UNAUTHORIZED, \
    HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_422_UNPROCESSABLE_ENTITY
from starlette.responses import StreamingResponse, Response


from app.db.database import create_connection
from sqlalchemy.orm import Session, aliased
from sqlalchemy import func, union, select, or_, alias, text, and_
from typing import List, Optional
from app.models import *
from ..schemas import heroes as schema
import io

router = APIRouter(
    prefix="/heroes",
    tags=["Heroes"],
)


@router.get("/all/", response_model=List[schema.GetHeroes], status_code=HTTP_200_OK,
            summary="Retrieves all heroes.",
            responses={404: {"description": "Heroes were not found."}})
def get_all_heroes(db: Session = Depends(create_connection)):
    result = db.query(
        Heroes.hero_id,
        Heroes.hero_name,
        Heroes.image_name,
        Heroes.primary_attr
    ).all()

    if len(result) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Heroes were not found."
        )

    return result


@router.get("/synergies/", response_model=List[schema.GetSynergies], status_code=HTTP_200_OK,
            summary="Retrieves all synergies.",
            responses={404: {"description": "Synergies were not found."}})
def get_all_synergies(db: Session = Depends(create_connection)):
    result = db.query(
        Synergies.hero_id_1,
        Synergies.hero_id_2,
        Synergies.s_value,
    ).all()

    if len(result) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Synergies were not found."
        )

    return result


@router.get("/counters/", response_model=List[schema.GetCounters], status_code=HTTP_200_OK,
            summary="Retrieves all counters.",
            responses={404: {"description": "Counters were not found."}})
def get_all_synergies(db: Session = Depends(create_connection)):
    result = db.query(
        Counters.hero_id_1,
        Counters.hero_id_2,
        Counters.c_value,
    ).all()

    if len(result) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Counters were not found."
        )

    return result
