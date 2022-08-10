from typing import List, Any
from sqlalchemy import create_engine, insert
from sqlalchemy import Column, Integer, DateTime, String, Date, Text, Time
from sqlalchemy.orm import declarative_base
from loguru import logger

engine = create_engine(
    'postgresql+psycopg2:'
    '//postgres:1234@127.0.0.1:5432/test'
    )


Base = declarative_base()


class Crimes(Base):

    __tablename__ = "crimes"
    id = Column(Integer, primary_key=True)
    crime_id = Column(Integer)
    original_crime_type_name = Column(String,nullable=True)
    report_date = Column(Date,nullable=True)
    call_date = Column(Date,nullable=True)
    offense_date = Column(Date,nullable=True)
    call_time = Column(Time,nullable=True)
    call_date_time = Column(DateTime,nullable=True)
    disposition = Column(String,nullable=True)
    address = Column(Text,nullable=True)
    city = Column(String,nullable=True)
    state = Column(String,nullable=True)
    agency_id = Column(Integer,nullable=True)
    address_type = Column(String,nullable=True)
    common_location = Column(Text,nullable=True)


@logger.catch
def write_to_database(row: List[Any]) -> None:
    """ write data to database """

    ins = insert(Crimes).values(
        crime_id=int(row[0]),
        original_crime_type_name=row[1],
        report_date=row[2],
        call_date=row[3],
        offense_date=row[4],
        call_time=row[5],
        call_date_time=row[6],
        disposition = row[7],
        address=row[8],
        city=row[9],
        state=row[10],
        agency_id=row[11],
        address_type=row[12],
        common_location=row[13]
        )


    engine.execute(ins)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
