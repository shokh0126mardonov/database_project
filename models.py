from datetime import datetime
from sqlalchemy import(
    Table,Column,Integer,String,DateTime,Boolean
)
from database import meta

tasks = Table(
    'tasks',
    meta,
    Column('id',Integer , primary_key = True,autoincrement=True),
    Column('title' , String(length=64) , nullable = False),
    Column("description" , String),
    Column("completed" , Boolean , default = False,nullable=False),
    Column("created_at" , DateTime , default = datetime.now),
    Column("due_date" , DateTime , default = datetime.now)

)

