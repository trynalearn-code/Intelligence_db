from database.mission_db import MissionDB
from fastapi import APIRouter, HTTPException
from logs.setup_log import log

router=APIRouter()

def validate(field, body):
    if field not in body:
        raise HTTPException("You're missing {field}", status_code=400)


@router.post("", status_code=201)
def create_mission(body:dict):
    log.info("attempting to create a mission")
    validate("title", body)
    validate("description", body)
    validate("location", body)
    validate("difficulty", body)
    validate("importance", body)
    validate("status", body)
    validate("assigned_agent_id", body)
    MissionDB.create_mission(body)
    log.info("successfully created a mission")

@router.get("")
def get_all_missions():
    log.info("attempting to get all missions")
    return MissionDB.get_all_missions()

@router.get("/{id}")
def get_mission_by_id(id):
    log.info("attempting to get a mission by its id")
    return MissionDB.get_mission_by_id(id)

@router.put("/{id}/assign/{agent_id}")
def assign_mission(id, agent_id):
    log.info("attempting to assign mission %s to agent %s", id, agent_id)
    try:
        return MissionDB.assign_mission(id, agent_id)
    except MissionDB.get_open_missions_by_agent(agent_id)==3:
            log.warning("We can't assign this mission to this agent")
            raise HTTPException("Sorry, agent %s already has 3 open missions",agent_id, status_code=400)
    except MissionDB.check_a["is_active"]==False:
            log.warning("We can't assign this mission to this agent")
            raise HTTPException("Sorry, agent %s is inactive"(agent_id), status_code=400)
    except MissionDB.check_m["risk_level"]>=25 and MissionDB.check_a["agent_rank"] != "Commander":
            log.warning("We can't assign this mission to this agent")
            raise HTTPException("Sorry, this mission is too dangerous for agent %s"(agent_id), status_code=400)
@router.put("/{id}/start")
def start_mission(id):
    log.info("attempting to start mission %s", id)
    pass