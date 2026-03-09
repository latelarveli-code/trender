import streamlit as st

def apply_launch_theme():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
        
        .stApp { background-color: #0d1117; color: #c9d1d9; font-family: 'Inter', sans-serif; }
        h1 { color: #d4af37 !important; font-weight: 600; letter-spacing: -1px; }
        .stButton>button {
            width: 100%;
            background-color: #d4af37;
            color: #0d1117;
            border-radius: 4px;
            border: none;
            padding: 0.5rem;
            font-weight: 600;
        }
        .opportunity-card {
            background-color: #161b22;
            border: 1px solid #30363d;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
        }
        </style>
    """, unsafe_allow_html=True)