from datetime import datetime
from database import engine,meta,get_connect
import models
from crud import create_task,get_task,delete_task
meta.create_all(engine)

def add_task():
    title = input("title: ")
    descreption = input("descreption: ")
    due_date_text = input("due date (yyyy-mm-dd | hh:mm): ")
    due_date = datetime.strptime(due_date_text,"%Y-%m-%d | %H:%M")
    create_task(get_connect(),title,due_date=due_date,description=descreption)

def show_task():
    result = get_task(get_connect())
    for i in result:
        print(i)

def remove_task():
    task_id = int(input("task_id ni kiriting: "))
    delete_task(get_connect(),task_id)
    print("task o'chirildi")
    
    