import streamlit as st
from style import PAGE_CONFIG_ICON

st.set_page_config(
    page_title="E-CPM | Canadian Professional Property Management",
    page_icon=PAGE_CONFIG_ICON,
    layout="wide",
)

pg = st.navigation([
    st.Page("Home.py", title="Home"),
    st.Page("1_Services.py", title="Services"),
    st.Page("2_Contact.py", title="Contact"),
])
pg.run()


st.markdown("### What we do")
st.markdown(
    "From routine upkeep to guest support, E-CPM takes care of the details "
    "so property owners don't have to. Here's a quick look — full details "
    "on the Services page."
)

st.markdown(key_teeth_divider(), unsafe_allow_html=True)

services_preview = [
    ("🛠️", "Maintenance & Repairs"),
    ("🧹", "Housekeeping"),
    ("🔑", "Property Care & Security"),
    ("🧳", "Guest & Owner Support"),
    ("🤝", "Vendor Management"),
]

cols = st.columns(len(services_preview))
for col, (icon, label) in zip(cols, services_preview):
    with col:
        st.markdown(
            f"""
            <div style="text-align:center;">
                <div style="font-size:1.8rem;">{icon}</div>
                <div style="font-size:0.85rem; font-weight:500; margin-top:0.25rem;">{label}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown(key_teeth_divider(), unsafe_allow_html=True)

st.markdown("### Reach us directly")
st.markdown(
    f"""
    <div class="contact-row">📞 <a href="{PHONE_HREF}">{PHONE}</a></div>
    <div class="contact-row">✉️ <a href="{EMAIL_HREF}">{EMAIL}</a></div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="ecpm-footer">© 2026 E-CPM — Canadian Professional Property Management</div>',
    unsafe_allow_html=True,
)
