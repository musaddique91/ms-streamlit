import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Title of the app
st.title("Data Analysis And Predications")
saleTab, stockTab, expenseTab = st.tabs(["Sales", "Stock", "Expense"])
with saleTab:
    sales_file = st.file_uploader("Upload your CSV file", type="csv")
    if sales_file is not None:
        # Read the Excel file
        df = pd.read_csv(sales_file)
        st.dataframe(df)
        col1, col2= st.columns(2)
        with col1:
                st.write("Data Preview:", df.head(10))
        with col2:
            st.write("Data Description:", df.describe())
        # Plot charts
        # Plot charts
        st.subheader("Sales Chart")
        # df['Sales'].plot(kind='line')
        # plt.title("Sales Over Time")
        # st.pyplot(plt)
        if 'Date' in df.columns and 'Amount' in df.columns:
            # Line Chart (Time series over Date)
            fig1 = px.line(df, x='Date', y='Amount', title="Amount Over Time (Line Chart)")
            st.plotly_chart(fig1)

            df.set_index('Date', inplace=True)
            df_monthly = df.resample('M').sum()
            df_monthly.reset_index(inplace=True)
            fig = px.bar(df_monthly, x='Date', y='Amount', title="Monthly Sales Amount (Bar Chart)", labels={'Date': 'Month', 'Amount': 'Sales Amount'})
            fig.update_layout(
                xaxis_title="Month",
                yaxis_title="Sales Amount",
                xaxis_tickformat="%b %Y"  # Show month and year on x-axis
            )
            st.plotly_chart(fig)

        else:
            st.write("Please ensure your CSV file has 'Date' and 'Amount' columns for plotting.")
