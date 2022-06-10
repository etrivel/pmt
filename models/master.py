from tokenize import String
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import BIGINT, VARCHAR, Table, Column, MetaData, Integer,Date, column
from sqlalchemy import create_engine, true
from sqlalchemy.ext.declarative import declarative_base

base=declarative_base()

class User(base):
        __tablename__="bankdetails"
        id=Column('id',BIGINT, primary_key=True)
        employee_id=Column('employee_id',BIGINT)
        bank_name=Column('bank_name',VARCHAR(255))
        bank_branch=Column('bank_branch',VARCHAR(255))
        accacc_noNo=Column('acc_no',VARCHAR(255))
        ifsc_code=Column('ifsc_code',VARCHAR(255))
        micr_code=Column('micr_code',VARCHAR(255))
        is_active=Column('is_active',VARCHAR(255))
        created_at=Column('created_at',Date)
        updated_at=Column('updated_at',Date)   

engine = create_engine("mysql://root:root@localhost/pmt", echo = True)
base.metadata.create_all(bind=engine)     