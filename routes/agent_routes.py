from database.agent_db import AgentDB
from fastapi import FastAPI, APIRouter, HTTPException
from logs.setup_log import log

router=APIRouter()


def validate(field, body):
    if field not in body:
        raise HTTPException("You're missing {field}", status_code=400)

@router.post("", status_code=201)
def create_agent(body:dict):
    log.info("attempting to create an agent")
    validate("name", body)
    validate("specialty", body)
    validate("agent_rank", body)
    AgentDB.create_agent(body)
    log.info("successfully created an agent")

@router.get("")
def get_all_agents():
    log.info("attempting to get all the agents")
    return AgentDB.get_all_agents() 
    

@router.get("/{id}")
def get_agent_by_id(id):
    log.info("attempting to get an agent by his id")
    return AgentDB.get_agent_by_id(id)

@router.put("/{id}")
def update_agent(id, data):
    log.info("attempting to update agent %s", id)
    return AgentDB.update_agent(id, data)

@router.put("/{id}/deactivate")
def deactivate_agent(id):
    log.info("attempting to deactivate agent %s", id)
    return AgentDB.deactivate_agent(id)

@router.get("{id}/performance")
def get_agent_performance(id):
    log.info("attempting to get the performance of agent %s", id)
    return AgentDB.get_agent_performance(id)