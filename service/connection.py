from sqlalchemy import create_engine, true

def connect():

        engine = create_engine("mysql://root:root@localhost/pmt", echo = True)
        connection = engine.connect()
        return connection