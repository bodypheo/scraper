from sqlalchemy import create_engine
from sqlalchemy import text, insert


#sqlite> pragma table_info('urls');
#0|url_id|INTEGER|1||1
#1|url|VARCHAR|0||0
#2|nombre_app|VARCHAR|0||0
#3|date_db|DATETIME|0||0
#4|date_update|DATE|0||0
#5|date_launch|DATE|0||0
#6|downloads|INTEGER
# description VARCHAR|0||0
#7|num_reviews|INTEGER|0||0
#8|rate|FLOAT|0||0


db_uri = "sqlite:///model/urls.db"
eng = create_engine(db_uri, echo=True)

sql_select = "SELECT * from urls"
sql_insert_completo = "INSERT INTO urls (url, nombre_app, date_db, date_update, date_launch, downloads, description, num_reviews, rate) \
                        VALUES ('https://play.google.com/store/apps/details?id=com.apalon.weatherlive', 'El tiempo', '2023-05-09', '2022-11-01', \
                       '2022-01-10', '100000', 'App para ver el tiempo', '300', '4.4')"


with eng.begin() as conn:
    salida = conn.execute(text(sql_select))
    for i in salida:
        print(i[1])
        
    result = conn.execute(text(sql_insert_completo))
    conn.commit                        

conn.close