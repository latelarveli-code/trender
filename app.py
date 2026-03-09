import streamlit as st
from engine import fetch_innovation_data
from agent import analyze_opportunity
from styles import apply_styles

# Käytetään modulaarisia palasia
apply_styles()

st.title("AALTO-VUO | INTELLIGENCE TERMINAL")
st.write("Analysoidaan globaaleja innovaatioita ja työkaluja.")

if st.sidebar.button("PÄIVITÄ DATA", use_container_width=True):
    data = fetch_innovation_data()
    
    if not data.empty:
        for _, row in data.iterrows():
            op = analyze_opportunity(row['title'])
            
            with st.container(border=True):
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.subheader(row['title'])
                    st.write(f"**Kategoria:** {op['category']}")
                    st.write(f"**Strategia:** {op['action_plan']}")
                    
                    # Napit, joista sinä voit hyötyä (Affiliate)
                    c1, c2 = st.columns(2)
                    with c1:
                        st.link_button("LUE LÄHDE", row['url'])
                    with c2:
                        # Tämän napin takana voi olla affiliate-linkkisi
                        st.link_button("HANKI TYÖKALUT", op['tool_link'], type="primary")
                
                with col2:
                    st.metric("PÖHINÄ", row['score'])
    else:
        st.warning("Etsitään yhteyttä...")