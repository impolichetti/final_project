import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float

# Database setup
Base = declarative_base()

class DivorceData(Base):
    __tablename__ = 'divorce_data'
    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    all_3544 = Column(Float)
    HS_3544 = Column(Float)
    SC_3544 = Column(Float)
    BAp_3544 = Column(Float)
    BAo_3544 = Column(Float)
    GD_3544 = Column(Float)
    poor_3544 = Column(Float)
    mid_3544 = Column(Float)
    rich_3544 = Column(Float)
    all_4554 = Column(Float)
    HS_4554 = Column(Float)
    SC_4554 = Column(Float)
    BAp_4554 = Column(Float)
    BAo_4554 = Column(Float)
    GD_4554 = Column(Float)
    poor_4554 = Column(Float)
    mid_4554 = Column(Float)
    rich_4554 = Column(Float)
    poor_all = Column(Float)
    mid_all = Column(Float)
    rich_all = Column(Float)
    HS_all = Column(Float)
    SC_all = Column(Float)
    BAp_all = Column(Float)
    BAo_all = Column(Float)
    GD_all = Column(Float)

engine = create_engine('sqlite:///data.db')
Session = sessionmaker(bind=engine)
session = Session()

# Streamlit interface
st.title("Divorce Data Visualization")

# Load data from database
records = session.query(DivorceData).all()

# Convert to DataFrame
data = [{
    'Year': r.year,
    'Poor_all': r.poor_all,
    'Mid_all': r.mid_all,
    'Rich_all': r.rich_all,
    'HS_3544': r.HS_3544
} for r in records]

df = pd.DataFrame(data)
st.write("All Years Summary", df)


