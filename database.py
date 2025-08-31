from sqlalchemy import (
    create_engine,URL,MetaData
    )
from config import HOST,PASSWORD,USER,PORT,NAME

url_object = URL.create(
    drivername="postgresql+psycopg2",
    password=PASSWORD,
    host=HOST,
    port=PORT,
    username=USER,
    database=NAME   
)

engine = create_engine(url_object)
meta = MetaData()