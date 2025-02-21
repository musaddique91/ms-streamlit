import streamlit as st
import st_sales_pred as sales_pred

def data_analysis_and_prediction():
    st.title("Data Analysis And Prediction")
    st.write("This is the Data Analysis And Prediction tab.")
    tab1, tab2 = st.tabs(["Date Value Prediction", "Stock Analysis and Prediction"])

    # Tab 1: Date Value Prediction
    with tab1:
        st.title("Date Value Analysis and Prediction")
        st.write("Upload your csv file having columns names ['Date' and 'Amount']. based on this You can make a prediction.")
        sales_pred.sales_analysis()
    
    # Tab 2: Stock Analysis and Prediction
    with tab2:
        st.title("Stock Analysis and Prediction")
        # Add content for Stock Analysis and Prediction
        st.header("Stock Data")
        stock_symbol = st.text_input("Enter stock symbol (e.g., AAPL)")
        start_date = st.date_input("Select start date")
        end_date = st.date_input("Select end date")
        
        if st.button("Analyze"):
            st.success(f"Analyzing stock {stock_symbol} from {start_date} to {end_date}")