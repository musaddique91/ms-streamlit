import streamlit as st
from streamlit_option_menu import option_menu
import st_ds_tabs as ds_tabs

# Custom CSS to style the sidebar and main content
def side_nav():
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            background-color: #2E3440;
            color: #ECEFF4;
        }
        .sidebar .sidebar-content .stButton>button {
            background-color: #5E81AC;
            color: #ECEFF4;
            border-radius: 5px;
            padding: 10px 20px;
            width: 100%;
            border: none;
            margin-bottom: 10px;
        }
        .sidebar .sidebar-content .stButton>button:hover {
            background-color: #81A1C1;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Left Sidebar Menu
    with st.sidebar:
        st.title("Main Menu")
        selected = option_menu(
            menu_title=None,  # No title
            options=["Home","Data Analysis And Prediction", 'Settings'],  # Menu options
            icons=["house", "cloud-upload", 'gear'],  # Icons for each option
            menu_icon="cast",  # Menu icon
            default_index=0,  # Default selected option
        )

    # Right-Side Container
    if selected == "Home":
        st.title("Home Page")
        st.write("Welcome to the Home Page!")
        
        # Add content to the right side
        col1, col2 = st.columns(2)  # Split the right side into two columns
        with col1:
            st.header("Column 1")
            st.write("This is the first column on the right side.")
        with col2:
            st.header("Column 2")
            st.write("This is the second column on the right side.")
    elif selected == "Data Analysis And Prediction":
        ds_tabs.data_analysis_and_prediction()
        
        # Add content to the right side
    elif selected == "Settings":
        st.title("Settings Page")
        st.write("This is the Settings Page.")
        # Add settings-related content here