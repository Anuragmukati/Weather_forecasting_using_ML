import pandas as pd
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport

df = pd.read_csv('bengaluru.csv', parse_dates=['date_time'], index_col='date_time')

profile = ProfileReport(df,

                        title="Climate Report",

        dataset={

        "description": "This profiling report was generated for Ananlysing the Weather of the Bengaluru City",

        "copyright_holder": "Anurag Mukati & Chinmay Pathak",

        "copyright_year": "2023",

    },

)


st.title("Data Profiling in Streamlit!")

st.write(df)

st_profile_report(profile)
