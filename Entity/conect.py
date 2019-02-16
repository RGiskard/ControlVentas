from sqlalchemy import create_engine
#Conección a mysql 
engine=create_engine("mysql+mysqlconnector://root:sesamo@localhost/test")
engine.connect()#establece la conección
#print(engine)
##Creación de metadata
from sqlalchemy import MetaData
metadata=MetaData()

##Creación de una tabla
from sqlalchemy import Table,Column, Integer, Numeric, String, ForeignKey

#importacion de datatypes
from datetime import datetime
from sqlalchemy import DateTime
##Creacion de tablas usando SqlAlchemy-ORM
users=Table("customers",metadata,Column("customer_id",Integer,primary_key=True),Column("name",String(64),nullable=False))
metadata.create_all(engine)

