# import dependencies for python
import datetime as dt
import numpy as np
import pandas as pd
# import dependencies for sql 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import creat_engine, func
#import flask dependency 
from flask import Flask, jsonify
# set up database engine 
engine = create_engine("sqlite:///hawaii.sqlite")
# reflect database
Base = automap_base()
Base.prepare(engine, reflect=True)
#set references
Measurement = Base.classes.measurement
Station = Base.classes.station
# create session link 
session = Session(engine)
#define the app 
app = Flask(__name__)
@app.route('/')
def welcome():
    return(
        '''
        Welcome to the Hawaii Climate Analysis API!
        Available Routes:
        /api/v1.0/precipitation
        /api/v1.0/stations
        /api/v1.0/tobs
        /api/v1.0/temp/start/end
    ''')
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)
