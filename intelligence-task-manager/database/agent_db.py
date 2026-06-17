from db_connection import get_connection, create_database, create_tables

class AgentDB:
    
    def create_agent(data):
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute(
            """
        INSERT INTO agents(id, name, specialty)
            """
        )