from database.agent_db import AgentDB
from fastapi import FastAPI, APIRouter, HTTPException


router=APIRouter()


def validate(field, body):
    if field not in body:
        raise HTTPException("You're missing {field}", status_code=400)

@router.post("", status_code=201)
def create_agent(body:dict):
    validate("name", body)
    validate("specialty", body)
    validate("agent_rank", body)
    AgentDB.create_database(body)


