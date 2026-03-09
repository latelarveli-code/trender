import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        .stApp { background-color: #0b0d11; }
        h1, h2, h3 { font-family: 'Inter', sans-serif; color: #d4af37 !important; }
        .stButton>button {
            background-color: #d4af37;
            color: #0b0d11;
            border-radius: 4px;
            font-weight: bold;
        }
        div[data-testid="stVerticalBlockBorderWrapper"] {
            background-color: #151921;
            border: 1px solid #2d333b;
            padding: 20px;
        }
        </style>
        """, unsafe_allow_html=True)