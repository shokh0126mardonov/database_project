from datetime import datetime
from sqlalchemy import Connection,select
from sqlalchemy import Insert
from models import tasks

def create_task(
        conn: Connection ,
        title: str,
        description: str | None = None,
        due_date :datetime|None = None
    ):
    
    try:
        query = Insert(tasks).values(
            title = title,
            description = description,
            due_date = due_date
        )
        
        conn.execute(query)
        conn.commit()
        

    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()

def get_task(conn: Connection):
    result = []
    
    try:
        cuery = select(tasks)
        result = conn.execute(cuery)
        conn.commit
    except Exception as e:
        print(e)
    finally:
        conn.close()
        
    return result 