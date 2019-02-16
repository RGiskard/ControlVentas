from sqlalchemy import create_engine
#Conección a mysql 
engine=create_engine("mysql+mysqlconnector://root:sesamo@localhost/test")
engine.connect()
print(engine)

