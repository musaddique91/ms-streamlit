import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
import plotly.graph_objects as go


def line_chart(df):
    fig1 = px.line(df, x='Date', y='Amount', title="Amount Over Time (Line Chart)")
    st.plotly_chart(fig1)

def monthly_bar_chart(df):
    fig = px.bar(df, x='Date', y='Amount', title="Monthly Sales Amount (Bar Chart)", labels={'Date': 'Month', 'Amount': 'Sales Amount'})
    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Sales Amount",
        xaxis_tickformat="%b %Y"  # Show month and year on x-axis
    )
    st.plotly_chart(fig)
def yearly_bar_chart(df):
    fig = px.bar(df, x='Date', y='Amount', title="Yearly Sales Amount (Bar Chart)", labels={'Date': 'Year', 'Amount': 'Sales Amount'})
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Sales Amount",
        xaxis_tickformat="%Y"  # Show year on x-axis
    )
    st.plotly_chart(fig)
def predict_future_value(df,value):
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=value)
    st.write(future)
    forcast_df = model.predict(future)
    show_future_df = forcast_df[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
    show_future_df.rename(columns={"ds": "Date", "yhat": "Predicted Amount", "yhat_lower": "Lower Bound", "yhat_upper": "Upper Bound"}, inplace=True)
    st.write(show_future_df)
    st.title("Predicted Future Values:")
    st.write(show_future_df.tail(value))
    
    st.title("Sales Prediction")
    fc_fig = plot_plotly(model, forcast_df)
    fc_fig.update_layout(width=1500, height=600)  # Set custom width and height
    st.plotly_chart(fc_fig)

    plot_components_fig = plot_components_plotly(model, forcast_df)
    st.title("Components of Forecast")
    st.write(plot_components_fig)
    
def sales_analysis():
    sales_file = st.file_uploader("Upload your CSV file", type="csv")
    if sales_file is not None:
        # Read the Excel file
        df = pd.read_csv(sales_file)
        df['Date'] = pd.to_datetime(df['Date'])
        df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')        
        st.dataframe(df)
        col1, col2= st.columns(2)
        with col1:
            st.write("Data Top 10 Rows:", df.head(10))
        with col2:
            st.write("Data Last 10 Rows:", df.tail(10))
        # with col4:
        #     st.write("Data Description:", df.describe())
        st.subheader("Sales Chart")
        if 'Date' in df.columns and 'Amount' in df.columns:
            line_chart(df)
            monthly_bar_chart(df)
            yearly_bar_chart(df)
            value = st.number_input("Enter a Future Days", min_value=0)
            if st.button("Analyze And Predict"):
                st.success(f"Analyzing Sale Amount based on given data...")
                df['ds'] = df['Date']
                df['y'] = df['Amount']
                df.drop(columns=['Date','Amount'], inplace=True)
                predict_future_value(df,value)
        else:
            st.write("Please ensure your CSV file has 'Date' and 'Amount' columns for plotting.")
        