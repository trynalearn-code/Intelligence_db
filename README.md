# Description

Intelligence_db is a RESTful project that incorporates mysql, docker and fastapi. The project is written in Clean Code as well.

Agents can be created, and data can be found about them. Agents are sent on missions of various difficulties and importance. Their risk level is measured and status is updated. Furthermore, logging is present throughout in order to ensure easy debugging.

Routes -> database -> mysql

# Background

An intelligence unit called ShadowNet needs an agent and task management system. The goal of the project is to build the complete data layer — connecting to MySQL, creating tables, and OOP classes to manage the data


## Project Structure
```
intelligence-task-manager/
├── database/
│ ├── db_connection.py
│ ├── agent_db.py
│ └── mission_db.py
├── README.md
├── requirements.txt
└── .gitignore
```

# Tables

## agents

| Field       | Type      | Notes |
| :--------- | :-------- | :------ |
| id   | INT, AUTO_INCREMENT, PK | identification     |
| name  | VARCHAR | agent name    |
| specialty | VARCHAR  | agent's specialty     |
| is_active  | BOOLEAN | is active: TRUE     |
| completed_missions  | INT | is active: 0     |
| failed_missions | INT  | is active: 0       |
| agent_rank  | ENUM/VARCHAR |  Junior/Senior/Commander only    |

## missions

| Field       | Type      | Notes |
| :--------- | :-------- | :------ |
| id   | INT, AUTO_INCREMENT, PK | identification     |
| title   | VARCHAR | mission title     |
| description | TEXT  | mission description      |
| location   | VARCHAR | mission location     |
| difficulty  | INT | 1-10 only     |
| importance | INT  | 1-10 only      |
| status | VARCHAR  | default: NEW      |
| risk_level   | VARCHAR | Automatically calculated — not from the user     |
| assigned_agent_id   | INT | NULL until assigned     |

# Methods

## db_connection
| Method       | Role     
| :--------- | :-------- 
| get_connection()   | Returns an active connection to MySQL()
| create_database() | Creates intelligence_db if it doesn't exist  
| create_tables()   | Creates the 2 tables if they don't exist 


## AgentDB
### Responsible for all SQL operations against the agents table.
| Method       | Role     
| :--------- | :-------- 
| create_agent(data)   | Creates a new agent and returns the agent object
| get_all_agents() | Returns a list of all the agents 
| get_agent_by_id(id)   | Returns one agent by his id, or None
| update_agent(id, data)   | UPDATE each line (can't change id)
| deactivate_agent(id) | Sets agent to inactive state
| increment_completed(id)   | Updates the number of completed tasks
| increment_failed(id)   | Updates the number of failed tasks
| get_agent_performance(id) | Returns a dictionary with the following keys: completed, failed, total, success_rate
| count_active_agents()   | Returns the number of active agents


## MissionDB
### Responsible for all SQL operations against the missions table.
| Method       | Role     
| :--------- | :-------- 
| create_mission(data)   | Creates a new mission and returns the entire object
| get_all_missions() | Returns all the missions
| get_mission_by_id(id)   | Returns one mission by id, or None
| assign_mission(m_id, a_id)   | Assigns a mission to an agent
| update_mission_status(id, status)   | Updates the status of the mission
| get_open_missions_by_agent(id) |Returns agent's ASSIGNED/IN_PROGRESS missions
| count_all_missions()   | Total missions
| count_by_status(status)   | Counts by specified status
| count_open_missions() | Counts open missions
| count_critical_missions()   | Counts critical missions
| get_top_agent()   | Returns the agent with the most completed_missions


| ### Rules that must be implemented in the data layer                                                           |
| :------------------------------------------------------------------------------------------------------------- |
|                                                                                                                |
\| 1 Rank must be Commander / Senior / Junior — any other value throws an error.\|                            
\| 2 Difficulty and importance must be between 1 and 10 - otherwise an error.\|                                
\| 3 level_risk is calculated automatically when a task is created — the user does not submit it.           \| 
\| 4 An agent with False=active_is cannot accept tasks.                           \|                           
\| 5 An agent cannot have more than 3 open tasks (PROGRESS_IN / ASSIGNED) at the same time. \|                 
\| 6 If CRITICAL=level_risk — only a Commander level agent can accept the mission.\|                           
\| 7 Only a task with a status of NEW can be assigned. After assignment: ASSIGNED=status.               \|     
\| 8 Only a task with the status ASSIGNED can be started. After: PROGRESS_IN=status.           \|              
\| 9 Only a task can be completed. PROGRESS_IN and changed to completed or failed status.      \|              
\| 10 Only a task with a status of NEW or ASSIGNED can be canceled — otherwise an error.    \|                

### Running the Docker
docker run -d --name intelligence-mysql -e MYSQL_ROOT_PASSWORD=1234 \
 -e MY

### Run on a virtual environment
python -m venv Intelligence-proj
Intelligence-proj\Scripts\activate

## Required programs
- python
- uvicorn
- fastapi
- routers
- mysql
- docker
- logging

