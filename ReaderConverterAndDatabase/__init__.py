__author__ = 'Hans'


import psycopg2
import csv
import time
from sqlalchemy import Column, Integer, String, DateTime, BIGINT, REAL, TIMESTAMP, TEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from multiprocessing import Process




Base = declarative_base()



class Position(Base):
    __tablename__ = 'Positions'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    DateTime = Column(DateTime)
    UnitId = Column(BIGINT)
    Rdy = Column(REAL)
    Rdx = Column(REAL)
    Speed = Column(Integer)
    Course = Column(Integer)
    NumSatellites = Column(Integer)
    HDOP = Column(Integer)
    Quality = Column(TEXT)

class Connection(Base):
    __tablename__ = 'Connections'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    DateTime = Column(DateTime)
    UnitId = Column(BIGINT)
    Value = Column(Integer)
    Port = Column(TEXT)

class Events(Base):
    __tablename__ = 'Events'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    DateTime = Column(DateTime)
    UnitId = Column(BIGINT)
    Value = Column(Integer)
    Port = Column(TEXT)

class Monotoring(Base):
    __tablename__ = 'Monitoring'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    UnitId = Column(BIGINT)
    Type = Column(TEXT)
    Min = Column(REAL)
    Max = Column(REAL)
    Sum = Column(TEXT)
    BeginTime = Column(TIMESTAMP)
    EndTime = Column(TIMESTAMP)

print("creating engine!!!")
engine = create_engine("postgresql://postgres:test123@localhost/project")
engine.connect()
sessionmaker = sessionmaker()
sessionmaker.configure(bind=engine)
Base.metadata.create_all(engine)



def splitConnectionsData():
    with open('Connections.csv') as csvfile:

        readCSV = csv.reader(csvfile, delimiter=';')

        next(readCSV) #skips first row
        print("Reading Connections...")
        count = 0
        session = sessionmaker()
        for row in readCSV:

            count = count +1
            c = Connection(DateTime = row[0], UnitId = row[1],Port = row[2], Value = row[3])
            session.add(c)
            session.commit()


        print("connection counted: ", count)
        return count



def splitEventsData():
    with open('Events.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        next(readCSV) #skips first row
        print("Reading Events...")
        count = 0
        session = sessionmaker()
        for row in readCSV:
            e = Events(DateTime = row[0], UnitId = row[1],Port = row[2], Value = row[3])
            session.add(e)

            count = count +1
            session.commit()
        print("events counted: ", count)


def splitMonitoringData():
    with open('Monitoring.csv') as csvfile:

        readCSV = csv.reader(csvfile, delimiter=';')
        count = 0

        next(readCSV) #skips first row
        print("Reading Monitoring...")
        session = sessionmaker()
        for row in readCSV:
            m = Monotoring(UnitId = row[0], BeginTime = row[1], EndTime = row[2], Type = row[3], Min = row[4], Max = row[5], Sum = row[6]);
            session.add(m)
            count = count +1
            session.commit()



        print("Monitoring counted: ", count)



def splitPositionsData():
    #websocket = yield from websockets.connect('ws://localhost:8760/')
    with open('Positions.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        next(readCSV) #skips first row
        print("Reading Positions...")
        count = 0
        session = sessionmaker()
        for row in readCSV:
            p = Position(DateTime = row[0], UnitId = row[1], Rdx = row[2], Rdy = row[3], Speed = row[4], Course = row[5], NumSatellites = row[6], HDOP = row[7], Quality = row[8]);
            session.add(p)
            count = count +1
            session.commit()

        print("positions counted: ", count)

if __name__ == '__main__':

        starttime = time.time()
       #todo async
        print("start")



        ConnectionsDataParserThread = Process(splitConnectionsData(), args=())
        EventsDataParserThread = Process(splitEventsData(), args=())
        MonitoringDataParserThread = Process(splitMonitoringData(), args=())
        #PositionsDataParserThread = Process(splitPositionsData(), args=())

        ConnectionsDataParserThread.start()
        EventsDataParserThread.start()
        MonitoringDataParserThread.start()
        #PositionsDataParserThread.start()

        # ConnectionsDataParserThread.join()
        # EventsDataParserThread.join()
        # MonitoringDataParserThread.join()
        # PositionsDataParserThread.join()
        endtime = time.time()

        total_time = endtime - starttime
        print("total_time = ", total_time)

        # endtime = time.time()
        # print(endtime - starttime)

        """
        splitConnectionsData()
        splitEventsData()
        splitMonitoringData()
        splitPositionsData()
        """




    #else:

