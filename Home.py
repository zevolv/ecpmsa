import streamlit as st
from style import inject_css, logo_data_uri, key_teeth_divider, PHONE, PHONE_HREF, EMAIL, EMAIL_HREF

st.markdown(
    "<style>.block-container{max-width:900px; padding-top:2rem;}</style>",
    unsafe_allow_html=True,
)

inject_css()

# ---- Hero -------------------------------------------------------------
st.markdown(
    f"""
    <div class="hero-band">
        <img src="{logo_data_uri('white')}" style="height:50px; margin-bottom:0.75rem;" />
        <div class="hero-title">Canadian Professional Property Management</div>
        <p class="tagline">Reliable, skilled, and experienced care for your property.</p>
    </div>
    """,
    unsafe_allow_html=True,
)
if st.button("Get in Touch", type="primary", key="cta"):
    st.switch_page("pages/2_Contact.py")

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
