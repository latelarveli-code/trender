import streamlit as st

def show_newsletter_signup():
    with st.sidebar:
        st.markdown("---")
        st.subheader("📩 Viikoittainen Intelligence-raportti")
        st.write("Saa syvempää analyysia suoraan sähköpostiisi.")
        email = st.text_input("Sähköpostiosoite", placeholder="sinun@email.fi")
        if st.button("Tilaa raportti"):
            if email:
                st.success("Kiitos! Olet nyt listalla.")
                # Tässä vaiheessa voit tallentaa sähköpostin esim. CSV-tiedostoon tai tietokantaan
            else:
                st.error("Syötä sähköposti.")