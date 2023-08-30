import streamlit as st
import yfinance as yf
import pandas as pd
import altair as alt

st.set_page_config(layout="wide")

st.title('Stock Returns Dashboard')

tickers = ('TSLA', 'AAPL', 'XAUT-USD', 'CL=F', 'NQ=F')

 # DROPDOWN Menu
dropdown = st.multiselect('Pick your Assets', tickers)
start = st.date_input('Start', value=pd.to_datetime('2023-01-01'))  # Default start date
end = st.date_input('End', value=pd.to_datetime('today'))


def relativeret(df):
     rel = df.pct_change()
     cumret = (1+rel).cumprod() - 1
     cumret = cumret.fillna(0)
     return cumret


if len(dropdown) > 0: # If selected asset from list
     df = yf.download(dropdown, start, end)['Adj Close']
     df1 = relativeret(yf.download(dropdown, start, end)['Adj Close'])
     st.header('Closed Price of {}'.format(dropdown))
     st.title('Close Price')
     st.line_chart(df)  # Chart line
     st.header('Returns of {}'.format(dropdown))
     st.title('Cumulative Returns')
     st.line_chart(df1)
