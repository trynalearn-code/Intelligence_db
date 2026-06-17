import mysql.connector

def get_connection():
    mysql.connector.connect(
        host = "127.0.0.1",
        port = 3306,
        username = "root", # intelligence-mysql
        password = "root", #1234
        database = "Intelligence_db"
    )

def create_database():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute(
        "CREATE DATABASE Intelligence_db"
    )
    conn.commit()
    cursor.close()
    conn.close()

def create_tables():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute(
        """
CREATE TABLE agents IF NOT EXIST (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  specialty VARCHAR(255),
  is_active BOOLEAN DEFAULT TRUE,
  completed_missions INT,
  failed_missions INT,
  agent_rank ENUM(Junior, Senior, Commander)
        """
);
    cursor.execute(
        """
CREATE TABLE missions IF NOT EXIST (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  locaton VARCHAR(255),
  difficulty INT CHECK (1<= difficulty <=10),
  importance INT CHECK (1<= importance <=10),
  status VARCHAR(255) DEFAULT NEW,
  risk_level VARCHAR(255),
  assigned_agent_id INT NULL,
        """
);
    conn.commmit()
    cursor.close()
    conn.close()
    
    