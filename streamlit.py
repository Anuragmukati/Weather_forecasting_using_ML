import streamlit as st
from plotly import graph_objects as go
import streamlit as st
import time
import pandas as pd


df = pd.read_csv('bengaluru.csv')
df['date_time'] = pd.to_datetime(df['date_time'])
header = st.container()
select_param = st.container()
plot_spot = st.empty()

with header:
    st.title("Bengaluru Daily Weather Dashboard")
#select parmeter drop down
with select_param:
    param_lst = list(df.columns)
    param_lst.remove('date_time')
    select_param = st.selectbox('Select a Weather Parameter',   param_lst)

#function to make chart
def make_chart(df, y_col, ymin, ymax):
    fig = go.Figure(layout_yaxis_range=[ymin, ymax])
    fig.add_trace(go.Scatter(x=df['date_time'], y=df[y_col], mode='lines+markers'))
    
    fig.update_layout(width=900, height=570, xaxis_title='time',
    yaxis_title=y_col)
    st.write(fig)


n = len(df)
ymax = max(df[select_param])+5
ymin = min(df[select_param])-5
for i in range(0, n-30, 1):
    df_tmp = df.iloc[i:i+30, :]
    with plot_spot:
        make_chart(df_tmp, select_param, ymin, ymax)
    time.sleep(0.5)

