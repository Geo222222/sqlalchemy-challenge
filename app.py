from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import datetime as dt
import numpy as np  

#################################################
# Database Setup
#################################################
# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# Reflect the existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session
session = Session(engine)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


def get_session():
    session = Session(engine)
    return session

# Home route
@app.route("/")
def home():
    return (
        f"Welcome to the Climate API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

# Precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = get_session()
    most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    most_recent_date = dt.datetime.strptime(most_recent_date, "%Y-%m-%d")
    one_year_ago = most_recent_date - dt.timedelta(days=365)

    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).all()
    session.close()

    precip_data = {date: prcp for date, prcp in results}
    return jsonify(precip_data)

# Stations route
@app.route("/api/v1.0/stations")
def stations():
    session = get_session()
    results = session.query(Station.station, Station.name).all()
    session.close()

    station_list = []
    for station, name in results:
        station_dict = {}
        station_dict["station"] = station
        station_dict["name"] = name
        station_list.append(station_dict)

    return jsonify(station_list)


# TOBS route
@app.route("/api/v1.0/tobs")
def tobs():
    session = get_session()
    most_active_station = session.query(Measurement.station, func.count(Measurement.station))\
                                 .group_by(Measurement.station)\
                                 .order_by(func.count(Measurement.station).desc())\
                                 .first()[0]
    most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    most_recent_date = dt.datetime.strptime(most_recent_date, "%Y-%m-%d")
    one_year_ago = most_recent_date - dt.timedelta(days=365)

    results = session.query(Measurement.date, Measurement.tobs)\
                     .filter(Measurement.station == most_active_station)\
                     .filter(Measurement.date >= one_year_ago).all()
    session.close()

    tobs_data = {date: tobs for date, tobs in results}
    return jsonify(tobs_data)

# Start-end date route
@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    session = get_session()
    start_date = dt.datetime.strptime(start, "%Y-%m-%d")
    end_date = dt.datetime.strptime(end, "%Y-%m-%d")
    
    results = session.query(
        func.min(Measurement.tobs),
        func.avg(Measurement.tobs),
        func.max(Measurement.tobs)
    ).filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    session.close()
    
    temps = list(np.ravel(results))
    return jsonify(temps)


#################################################
# Flask Routes
#################################################
if __name__ == "__main__":
    app.run(debug=True)