from datetime import datetime
from database import engine,meta,get_connect
import models
from crud import create_task
meta.create_all(engine)


title = input("title: ")
descreption = input("descreption: ")
due_date_text = input("due date (yyyy-mm-dd | hh:mm): ")
due_date = datetime.strptime(due_date_text,"%Y-%m-%d | %H:%M")


create_task(get_connect(),title,due_date=due_date,description=descreption)