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
        
        /* Kortit: Lasiefekti */
        .card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 30px;
            margin-bottom: 25px;
            transition: all 0.4s ease;
        }
        .card:hover {
            border-color: #d4af37;
            background: rgba(212, 175, 55, 0.05);
            transform: translateY(-5px);
        }

        /* Isot otsikot */
        h1 { font-weight: 700; letter-spacing: -2px; color: #d4af37 !important; text-transform: uppercase; }
        
        /* Napit */
        .stButton>button {
            background: #d4af37;
            color: black;
            border-radius: 50px;
            border: none;
            padding: 10px 25px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        /* Piilotetaan Streamlitin turhat osat */
        header {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)