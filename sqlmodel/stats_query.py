from sqlmodel import Field, Session, SQLModel, create_engine, select
from models import Stats
from models import engine


with Session(engine) as session:
    statement = select(Stats)
    results = session.exec(statement)
    for stat in results:
        print(stat)