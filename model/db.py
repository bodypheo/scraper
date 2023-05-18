from sqlalchemy import create_engine
from sqlalchemy import text, insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#sqlite> pragma table_info('urls');
#0|url_id|INTEGER|1||1
#1|url|VARCHAR|0||0
#2|nombre_app|VARCHAR|0||0
#3|date_db|DATETIME|0||0
#4|date_update|DATE|0||0
#5|date_launch|DATE|0||0
#6|downloads|INTEGER
#7|description VARCHAR|0||0
#8|num_reviews|INTEGER|0||0
#9|rate|FLOAT|0||0

db_uri = "sqlite:///model/apps.sqlite"
eng = create_engine(db_uri, echo=True)
Session = sessionmaker(bind=eng)
session = Session()

Base = declarative_base()

def main():
    pass

if __name__== "__main__" :
    main()