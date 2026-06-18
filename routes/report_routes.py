from database.agent_db import AgentDB
from database.mission_db import MissionDB
from fastapi import FastAPI, APIRouter, HTTPException

router=APIRouter()

@router.get("/summary")
def get_summary():
    return {
        "active_agents":AgentDB.count_active_agents(),
        "total_missions":MissionDB.count_all_missions(),
        "open_missions":MissionDB.count_open_missions(),
        "completed_missions":MissionDB.count_completed_missions(),
        "failed_missions":MissionDB.count_failed_missions(),
        "critical_missions":MissionDB.count_critical_missions()
    }

@router.get("/missions-by-status")
def get_missions_by_status():
    return {
        "new":MissionDB.count_new_missions(),
        "assigned":MissionDB.count_assigned_missions(),
        "open": MissionDB.count_only_open_missions(),
        "in_progress": MissionDB.count_in_progress_missions(),
        "completed": MissionDB.count_completed_missions(),
        "failed": MissionDB.count_failed_missions(),
        "canceled":MissionDB.count_canceled_missions()
    }

@router.get("/top-agent")
def get_top_agent():
    return {"top agent": MissionDB.get_top_agent()}