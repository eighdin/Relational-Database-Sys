from sqlmodel import Session
from model import Faculty, engine

f1 = Faculty(firstname= "Christopher", lastname="Mansour")

with Session(engine) as session:
    session.add(f1)
    session.commit()