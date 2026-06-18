from database import db_connection
from fastapi import FastAPI, HTTPException, APIRouter
import uvicorn
from routes import agent_routes, mission_routes, report_routes

app=FastAPI()
app.include_router(agent_routes.router, prefix="/agents")
app.include_router(mission_routes.router, prefix="/missions")
app.include_router(report_routes.router, prefix="/reports")





if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)