import streamlit as st
from style import PAGE_CONFIG_ICON

st.set_page_config(
    page_title="E-CPM | Canadian Professional Property Management",
    page_icon=PAGE_CONFIG_ICON,
    layout="wide",
)

pg = st.navigation([
    st.Page("Home.py", title="Home"),
    st.Page("pages/1_Services.py", title="Services"),
    st.Page("pages/2_Contact.py", title="Contact"),
])
pg.run()

