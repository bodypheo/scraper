from sqlalchemy import create_engine
from sqlalchemy import text

db_uri = "sqlite:///model/urls.db"
eng = create_engine(db_uri, echo=True)
sql = "SELECT * from urls"

with eng.begin() as conn:
    salida = conn.execute(text(sql))
    for i in salida:
        print(i[1])


# multiple *args no longer accepted, pass a list
#result = connection.execute(
#
#Construir una lista con los resultados a insentar
#     table.insert(), {"x": 10, "y": 5}, {"x": 15, "y": 12}, {"x": 9, "y": 8}
#)