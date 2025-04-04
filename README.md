# 🌡️ SQLAlchemy Challenge – Climate Analysis in Hawaii

## 🏝️ Overview

This project uses **SQLAlchemy**, **Python**, and **Flask** to analyze and serve climate data for the Hawaiian Islands. The data originates from NOAA and is stored in a SQLite database. Using a combination of data modeling and API development, the project enables interactive access to temperature and precipitation trends.

---

## 🧰 Technologies Used

- Python
- SQLite
- SQLAlchemy ORM
- Flask (for API routes)
- Pandas
- Matplotlib

---

## 📁 Project Structure

```
sqlalchemy-challenge/
├── hawaii.sqlite               # SQLite database with NOAA climate data
├── climate_starter.ipynb       # Jupyter notebook for climate analysis
├── app.py                      # Flask API serving climate data endpoints
└── README.md                   # Project documentation
```

---

## 🔍 Climate Analysis (in `climate_starter.ipynb`)

- Connected to SQLite using SQLAlchemy ORM
- Reflected existing database schema to generate classes
- Retrieved last 12 months of precipitation and temperature data
- Identified most active weather station and analyzed:
  - Temperature distribution
  - Min, max, average temps over specific date ranges
- Created visualizations using Pandas and Matplotlib

---

## 🌐 Flask API (in `app.py`)

### Available Routes:

- `/` : Welcome page with available API routes
- `/api/v1.0/precipitation` : Precipitation data for the last year
- `/api/v1.0/stations` : List of weather stations
- `/api/v1.0/tobs` : Temperature observations of the most active station
- `/api/v1.0/<start>` : Temp min/avg/max from start date to end of data
- `/api/v1.0/<start>/<end>` : Temp min/avg/max between start and end dates

---

## 🚀 How to Run

1. Clone the repo:
```bash
git clone https://github.com/Geo222222/sqlalchemy-challenge.git
cd sqlalchemy-challenge
```

2. Launch the Jupyter notebook:
```bash
jupyter notebook climate_starter.ipynb
```

3. Run the Flask app:
```bash
python app.py
```

> Make sure Python and Flask are installed.

---

## 📌 Future Enhancements

- Deploy API to cloud using Heroku or AWS
- Build a frontend dashboard using Dash or Streamlit
- Add real-time weather scraping for current conditions

---

**Author:** [Geo222222](https://github.com/Geo222222)  
**Focus:** Data Engineering • APIs • Climate Data

