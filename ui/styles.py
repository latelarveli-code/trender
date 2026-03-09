import streamlit as st

def apply_launch_theme():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;500;700&display=swap');
        
        .stApp { 
            background-color: #050505; 
            color: #ffffff; 
            font-family: 'Space Grotesk', sans-serif; 
        }
        
        .card {
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 20px;
        }

        h1 { font-weight: 700; color: #d4af37 !important; text-transform: uppercase; letter-spacing: -1px; }
        
        /* Piilotetaan Streamlitin brändäys */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Streamlitin omien painikkeiden tyylitys */
        .stButton>button {
            border-radius: 5px;
            background-color: #1a1a1a;
            color: #d4af37;
            border: 1px solid #d4af37;
            font-weight: 600;
        }
        </style>
    """, unsafe_allow_html=True)