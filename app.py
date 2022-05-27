import yfinance as yf
import streamlit as st
import pandas as pd
import datetime

st.write("""

# Simple Stock Price App

""")

col1, col2 = st.columns(2)

# with col1:
with st.form("stock_price_form"):
    st.subheader("Set Ticker and Period")
    
    tickerSymbol = st.text_input("Ticker Symbol")
    startDate = st.date_input(
        "Start Period",
        min_value=datetime.date(2000, 1, 1),
        max_value=datetime.date(2022, 1, 1),
        value=datetime.date(2010, 1, 1)
    )
    endDate = st.date_input(
        "End Period",
        min_value=datetime.date(2000, 1, 1),
        max_value=datetime.date(2022, 1, 1),
        value=datetime.date(2010, 1, 2)
    )

    submitted = st.form_submit_button("Submit")
    
    if submitted:
        st.write("tickerSymbol", tickerSymbol, "startDate", startDate, "endDate", endDate)
        st.write(f"### Shown are the stock **closing price** and ***volume*** of {tickerSymbol}")

        tickerData = yf.Ticker(tickerSymbol)

        tickerDf = tickerData.history(period='1d', start=startDate, end=endDate)

        st.write("### Closing Price")
        st.line_chart(tickerDf.Close)

        st.write("### Volume")
        st.line_chart(tickerDf.Volume)