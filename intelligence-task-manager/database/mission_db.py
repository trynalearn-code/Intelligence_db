from db_connection import get_connection, create_database, create_tables

class MissionDB:
    def create_mission(data):
        conn=get_connection()
        cursor=conn.cursor(dictionary=True)
        cursor.execute(
            """
        INSERT INTO missions (%s, %s, %s, %s, %s, %s, %s)
            """,data("title", "description", "location", "difficulty", "importance", "status", "assigned_agent_id")
        )
        cursor.execute(
            """
        INSERT INTO missions (risk_level)
        VALUES("difficulty" * 2 + importance)
            """,
        )
        conn.commit()
        cursor.close()
        conn.close()
        return {"message": "Your mission has successfully been created"}
    
    def get_all_missions():
        conn=get_connection()
        cursor=conn.cursor(dictionary=True)
        cursor.execute(
            """
        SELECT * FROM missions
            """
        )
        row=cursor.fetchone()
        cursor.close()
        conn.close()
        return row 
    
    def get_mission_by_id(id):
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute(
            """
        SELECT * FROM missions
        WHERE id = %s 
            """(id,)
        )
        row=cursor.fetchone()
        cursor.close()
        conn.close()
        return row
    
    def assign_mission(m_id, a_id):
        # if get_open_missions_by_agent(a_id)==3:
        #     return {"message" : "Sorry, agent %s already has 3 open missions"(a_id)}
        conn=get_connection()
        cursor=conn.cursor(dictionary=True)
        cursor.execute(
            """
        UPDATE missions
        SET assigned_agent_id = %s
        WHERE id = %s
            """(a_id, m_id)
        )
        check=cursor.execute(
            """
        SELECT * FROM agents
        WHERE id = %s
            """(a_id)
        )
        if check["is_active"]==False:
            return {"message" : "Sorry, agent %s is inactive"(a_id)}
        cursor.execute(
            """
        UPDATE missions
        SET status = %s
        WHERE id = %s
            """("ASSIGNED",m_id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return {"message" : "Your mission %s has been assigned to agent %s"(m_id,a_id)}
    
    def update_mission_status(id, status):
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute(
            """
        UPDATE missions
        SET mission_status = %s
        WHERE id = %s
            """(status, id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return {"message" : "Your mission status %s has been assigned to agent %s"(status, id)}

    def get_open_missions_by_agent(id):
        conn=get_connection()
        cursor=conn.cursor(dictionary=True)
        cursor.execute(
            """
        SELECT * FROM missions
        WHERE id = %s
        AND status = "ASSIGNED"
        OR status = "IN-PROGRESS"
            """(id,)
        )
        row=cursor.fetchone()
        cursor.close()
        conn.close()
        return row
    
    def count_all_missions():
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute(
            """
        SELECT COUNT (*) FROM missions
            """
        )
        counts=cursor.fetchone()
        cursor.close()
        conn.close()
        return counts
    
    def count_by_status(status):
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute(
            """
        SELECT COUNT (*) FROM missions
        WHERE status = %s
            """(status,)
        )
        counts=cursor.fetchone()
        cursor.close()
        conn.close()
        return counts
    
    def count_open_missions():
        conn=get_connection()
        cursor=conn.cursor()
        assigned=cursor.execute(
            """
        SELECT COUNT (*) FROM missions
        WHERE status = "ASSIGNED"
            """
        )
        progress=cursor.execute(
            """
        SELECT COUNT (*) FROM missions
        WHERE status = "IN-PROGRESS"
            """
        )
        counts=cursor.fetchall(assigned + progress)
        cursor.close()
        conn.close()
        return counts
    
    def count_critical_missions():
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute(
            """
        SELECT * FROM missions
        WHERE  (difficulty * 2) + importance >= 25
            """
        )
        counts=cursor.fetchone()
        cursor.close()
        conn.close()
        return counts
    
    def get_top_agent():
        conn=get_connection()
        cursor=conn.cursor(dictionary=True)
        cursor.execute(
            """
        SELECT * FROM missions
        ORDER BY completed_missions DESC
        LIMIT 1
            """
        )
        winner=cursor.fetchone()
        cursor.close()
        conn.close()
        return winner
    
    