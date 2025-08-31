from datetime import datetime
from sqlalchemy import(
    Table,Column,Integer,String,DateTime,Boolean
)
from database import meta,engine

tasks = Table(
    'tasks',
    meta,
    Column('id',Integer , primary_key = True),
    Column('title' , String(length=64) , primary_key = True , nullable = False),
    Column("description" , String),
    Column("completed" , Boolean , default = False,nullable=False),
    Column("created_at" , DateTime , default = datetime.now),
    Column("due_date" , DateTime , default = datetime.now)

)

meta.create_all(engine)