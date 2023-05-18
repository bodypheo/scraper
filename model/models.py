import db
from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime, Float
from datetime import date, datetime

#TODO
# * Probar el insert y el appInDb en spider
# * Crear el updateapp
# ! Limpiar el código de los otros scripts donde pueda haber código BD que no sea de alchemy

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

class App(db.Base):
    __tablename__ = "app"
    url_id = Column(Integer, primary_key=True)
    url = Column(String)
    nombre_app = Column(String)
    date_db = Column(DateTime)
    date_update = Column(DateTime)
    date_launch = Column(DateTime)
    downloads = Column(String)
    description = Column(String)
    num_reviews = Column(Integer)
    rate = Column(Float)
    
    def __init__(self, url, nombre_app, date_db, date_update, date_launch, downloads, description, num_reviews, rate):
        self.url = url
        self.nombre_app = nombre_app
        self.date_db = date_db
        self.date_update = date_update
        self.date_launch = date_launch
        self.downloads = downloads
        self.description = description
        self.num_reviews = num_reviews
        self.rate = rate

def insertAppIntoDb(app):
    db.session.add(app)
    db.session.commit()
    if app.url_id != None:
        return app.url_id
    
def appInDb(url_app):
    res = db.session.query(App).filter_by(url=url_app).first()
    if res:
        return 1
    else:
        return 0

def updateApp(app):
    pass
    #TODO Crear update

def create():
    db.Base.metadata.create_all(db.eng)

def main():    
    app = App("https://play.google.com/store/apps",
        "Prueba de app",
        date.today(),
        datetime.strptime("2022-10-05", '%Y-%m-%d'),
        datetime.strptime("2022-12-05", '%Y-%m-%d'),
        "11K",
        "Descripción",
        220,
        3.4)
    db.session.add(app)
    db.session.commit()
    if app.url_id != None:
        print(app.url_id)
if __name__== "__main__" :
    url = "https://play.google.com/store/apps"
    url2 = "kkkkkkk"
    if appInDb(url2):
        print("existe")
    else:
        print("No existe")
