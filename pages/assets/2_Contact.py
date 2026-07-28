import streamlit as st
from style import inject_css, logo_data_uri, key_teeth_divider, PAGE_CONFIG_ICON, PHONE, PHONE_HREF, EMAIL, EMAIL_HREF

st.set_page_config(
    page_title="Contact | E-CPM",
    page_icon=PAGE_CONFIG_ICON,
    layout="wide",
)
st.markdown(
    "<style>.block-container{max-width:900px; padding-top:2rem;}</style>",
    unsafe_allow_html=True,
)

inject_css()

st.markdown(
    f"""
    <img src="{logo_data_uri('navy')}" style="height:52px; margin-bottom:0.5rem;" />
    <h1>Get in Touch</h1>
    <p style="opacity:0.8; margin-top:-0.5rem;">
        Questions about your property? Reach us directly — no forms, just a call or an email.
    </p>
    """,
    unsafe_allow_html=True,
)

st.markdown(key_teeth_divider(), unsafe_allow_html=True)

st.markdown(
    f"""
    <div class="service-card" style="max-width:420px;">
        <div class="contact-row" style="font-size:1.2rem;">
            📞 <a href="{PHONE_HREF}">{PHONE}</a>
        </div>
        <div class="contact-row" style="font-size:1.2rem;">
            ✉️ <a href="{EMAIL_HREF}">{EMAIL}</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="ecpm-footer">© 2026 E-CPM — Canadian Professional Property Management</div>',
    unsafe_allow_html=True,
)
