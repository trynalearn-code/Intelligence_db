from database.db_connection import get_connection, create_database, create_tables

class AgentDB:
    
    def create_agent(data):
        conn=get_connection()
        cursor=conn.cursor(dictionary=True)
        cursor.execute(
            """
        INSERT INTO agents (name, specialty, agent_rank)
        VALUES (%s, %s, %s) 
        SELECT * FROM agents
            """, data["name"], data["specialty"], data["agent_rank"]
        )
        conn.commit()
        rows=cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    
    def get_all_agents():
        conn=get_connection()
        cursor=conn.cursor(dictionary=True)
        cursor.execute(
            """
        SELECT * FROM agents
            """
        )
        row=cursor.fetchone()
        cursor.close()
        conn.close()
        return row
    
    def get_agent_by_id(id):
        conn=get_connection()
        cursor=conn.cursor(dictionary=True)
        cursor.execute(
            """
        SELECT * FROM agents
        WHERE id = %s 
            """(id,)
        )
        row=cursor.fetchone()
        cursor.close()
        conn.close()
        return row

    def update_agent(id, data):
        conn=get_connection()
        cursor=conn.cursor(dictionary=True)
        cursor.execute(
            """
        UPDATE agents where id=%s 
        SET name = %s 
        SET specialty = %s
        SET is_active = %s 
        SET completed_missions = %s
        SET failed_missions = %s 
        SET agent_rank = %s
            """(id, data("name", "specialty", "is_active", "completed_missions", "failed_missions", "agent_rank"))
        )
        conn.commit()
        cursor.close()
        conn.close()
        return {"message":"Your agent has been updated successfully"}
    
    def deactivate_agent(id):
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute(
            """
        UPDATE agents where id=%s 
        SET is_active = %s 
            """(id, "FALSE")
        )
        conn.commit()
        cursor.close()
        conn.close()
        return {"message":"Your agent %s has been deactivated successfully"(id)}
    
    def increment_completed(id):
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute(
            """
        UPDATE agents where id=%s 
        SET completed_missions = completed_missions + 1
            """(id,)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return {"message":"Your agent's stats have successfully been updated!"}
    
    def increment_failed(id):
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute(
            """
        UPDATE agents where id=%s 
        SET failed_missions = failed_missions + 1
            """(id,)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return {"message":"Your agent's stats have successfully been updated. Better luck next time"}
    
    def get_agent_performance(id):
        conn=get_connection()
        cursor=conn.cursor()
        complete=cursor.execute(
            """
        SELECT completed_missions FROM agents WHERE id=%s 
            """(id)
        )
        failed=cursor.execute(
            """
        SELECT completed_missions FROM agents WHERE id=%s 
            """(id)
        )
        total= complete + failed
        conn.commit()
        cursor.close()
        conn.close()
        return {"completed missions" : complete, 
                "failed missions" : failed,
                "total missions": total,
                "success rate": complete/total}
    
    def count_active_agents():
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute(
            """
        SELECT COUNT (*) FROM agents
            """
        )
        counts=cursor.fetchone()
        cursor.close()
        conn.close()
        return counts