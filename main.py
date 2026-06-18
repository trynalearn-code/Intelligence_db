from database.db_connection import create_tables, create_database
from fastapi import FastAPI, HTTPException, APIRouter
import uvicorn
from routes import agent_routes, mission_routes, report_routes


app=FastAPI()
app.include_router(agent_routes.router, prefix="/agents")
app.include_router(mission_routes.router, prefix="/missions")
app.include_router(report_routes.router, prefix="/reports")





if __name__ == "__main__":
    create_database()
    create_tables()
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)