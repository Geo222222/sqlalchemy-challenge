# Import the dependencies.
%matplotlib inline
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

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

# View all of the classes that automap found
print(Base.classes.keys())

most_recent = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
print(f"Most recent date: {most_recent}")


# Calculate the date 12 months ago from the most recent date
most_recent_date = dt.datetime.strptime(most_recent, "%Y-%m-%d")
one_year_ago = most_recent_date - dt.timedelta(days=365)

# Query for the last 12 months of precipitation data
precipitation_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).all()

# Load the query results into a DataFrame
precip_df = pd.DataFrame(precipitation_data, columns=['date', 'prcp'])


# Plot the results
precip_df.plot(x='date', y='prcp', rot=45)
plt.xlabel('Date')
plt.ylabel('Precipitation')
plt.title('Precipitation Over Last 12 Months')
plt.show()

# Print summary statistics
print(precip_df.describe())

# Query to find the most active stations
active_stations = session.query(Measurement.station, func.count(Measurement.station)).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()
print(active_stations)

# Most active station
most_active_station = active_stations[0][0]
print(f"Most active station: {most_active_station}")

# Close Session
session.close()

#################################################
# Flask Setup
#################################################




#################################################
# Flask Routes
#################################################
