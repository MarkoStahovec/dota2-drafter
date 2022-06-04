from pydantic import BaseModel


class GetHeroes(BaseModel):
    hero_id: int
    hero_name: str
    image_name: str
    primary_attr: str


class GetSynergies(BaseModel):
    hero_id_1: int
    hero_id_2: int
    s_value: int


class GetCounters(BaseModel):
    hero_id_1: int
    hero_id_2: int
    c_value: int
