from database.mission_db import MissionDB
from fastapi import APIRouter, HTTPException

router=APIRouter()

def validate(field, body):
    if field not in body:
        raise HTTPException("You're missing {field}", status_code=400)


@router.post("", status_code=201)
def create_mission(body:dict):
    validate("title", body)
    validate("description", body)
    validate("location", body)
    validate("difficulty", body)
    validate("importance", body)
    validate("status", body)
    validate("assigned_agent_id", body)
    MissionDB.create_mission(body)

@router.get("")
def get_all_missions():
    return MissionDB.get_all_missions()

@router.get("/{id}")
def get_mission_by_id(id):
    return MissionDB.get_mission_by_id(id)

@router.put("/{id}/assign/{agent_id}")
def assign_mission(id, agent_id):
    return MissionDB.assign_mission(id, agent_id)

# @router.put("/{id}/start")
# def assign_mission(id, agent_id):
#     return MissionDB.assign_mission(id, agent_id)