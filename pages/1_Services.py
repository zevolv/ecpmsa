import streamlit as st
from style import inject_css, logo_data_uri, key_teeth_divider

st.markdown(
    "<style>.block-container{max-width:900px; padding-top:2rem;}</style>",
    unsafe_allow_html=True,
)

inject_css()

st.markdown(
    f"""
    <img src="{logo_data_uri('navy')}" style="height:52px; margin-bottom:0.5rem;" />
    <h1>Services</h1>
    <p style="opacity:0.8; margin-top:-0.5rem;">
        Everything your property needs, handled locally and reliably.
    </p>
    """,
    unsafe_allow_html=True,
)

st.markdown(key_teeth_divider(), unsafe_allow_html=True)

SERVICES = [
    ("🛠️", "Maintenance & Repairs",
     "Interior and exterior upkeep, minor repairs, and routine inspections "
     "to keep your property in top condition year-round."),
    ("🧹", "Housekeeping",
     "Deep cleaning, turnover cleaning between guests or tenants, and "
     "fresh laundry services."),
    ("🔑", "Property Care & Security",
     "Secure key holding, storm checks, and regular visual walk-throughs "
     "so you always know your property is safe."),
    ("🧳", "Guest & Owner Support",
     "Airport pickups and drop-offs, plus pre-arrival stocking of "
     "groceries and supplies before you or your guests arrive."),
    ("🤝", "Vendor Management",
     "Coordinating local contractors, gardeners, or pool care — one "
     "point of contact instead of many."),
]

for icon, title, desc in SERVICES:
    st.markdown(
        f"""
        <div class="service-card" style="margin-bottom: 1rem;">
            <h4>{icon} &nbsp; {title}</h4>
            <p>{desc}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    '<div class="ecpm-footer">© 2026 E-CPM — Canadian Professional Property Management</div>',
    unsafe_allow_html=True,
)
