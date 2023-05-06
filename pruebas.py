from sqlalchemy import create_engine
from sqlalchemy import text

db_uri = "sqlite:///model/urls.db"
eng = create_engine(db_uri, echo=True)
sql = "SELECT * from urls"

with eng.begin() as conn:
    salida = conn.execute(text(sql))
    for i in salida:
        print(i[1])