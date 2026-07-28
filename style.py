"""
Shared design tokens and CSS for the E-CPM site.
Import inject_css() at the top of every page.
"""
import streamlit as st
import base64
from pathlib import Path

ASSETS = Path(__file__).parent / "assets"

# ---- Design tokens ---------------------------------------------------
STEEL_BLUE = "#4F7B93"
STEEL_BLUE_DARK = "#3E6478"
NAVY = "#1B2733"
POWDER_BLUE = "#E4F1FA"
WHITE = "#FFFFFF"
ACCENT_RED = "#D52B1E"

PHONE = "+34 642075704"
PHONE_HREF = "tel:+34642075704"
EMAIL = "ECPMSA@gmail.com"
EMAIL_HREF = "mailto:ECPMSA@gmail.com"


def _b64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode()


def logo_data_uri(variant: str = "navy") -> str:
    fname = {"navy": "logo_navy.png", "white": "logo_white.png", "steel": "logo_steelblue.png"}[variant]
    return f"data:image/png;base64,{_b64(ASSETS / fname)}"


def key_teeth_divider(color: str = STEEL_BLUE, height: int = 18) -> str:
    """A thin repeating key-teeth notch pattern used as a section divider,
    echoing the logo's key motif instead of a plain <hr>."""
    return f"""
    <div style="
        width:100%; height:{height}px; margin: 0.25rem 0 1.75rem 0;
        background: repeating-linear-gradient(
            90deg,
            {color} 0px, {color} 3px,
            transparent 3px, transparent 6px,
            {color} 6px, {color} 9px,
            transparent 9px, transparent 16px
        );
        clip-path: polygon(0 0, 100% 0, 100% 40%, 0 100%);
        opacity: 0.85;
    "></div>
    """


PAGE_CONFIG_ICON = str(ASSETS / "favicon.png")


def inject_css():
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@500&display=swap');

        html, body, [class*="css"] {{
            font-family: 'Inter', sans-serif;
            color: {NAVY};
        }}

        h1, h2, h3, h4 {{
            font-family: 'Space Grotesk', sans-serif !important;
            color: {NAVY};
            letter-spacing: -0.01em;
        }}

        .stApp {{
            background: {WHITE};
        }}

        [data-testid="stHeader"] {{
            background: rgba(0,0,0,0);
        }}

        .mono {{
            font-family: 'IBM Plex Mono', monospace;
        }}

        /* Curved steel-blue hero band, echoing the business card's cut corner */
        .hero-band {{
            background: linear-gradient(135deg, {STEEL_BLUE} 0%, {STEEL_BLUE_DARK} 100%);
            border-radius: 0 0 48px 0;
            padding: 2.75rem 2.5rem 3rem 2.5rem;
            margin: -1rem -1rem 2rem -1rem;
            color: {WHITE};
        }}
        .hero-band h1, .hero-band h3, .hero-band p {{
            color: {WHITE} !important;
        }}

        .tagline {{
            font-size: 1.15rem;
            font-weight: 400;
            opacity: 0.92;
            margin-top: 0.25rem;
        }}

        /* CTA button */
        .cta-button {{
            display: inline-block;
            background: {WHITE};
            color: {STEEL_BLUE_DARK} !important;
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 600;
            padding: 0.65rem 1.6rem;
            border-radius: 8px;
            text-decoration: none !important;
            margin-top: 1.25rem;
            box-shadow: 0 2px 10px rgba(0,0,0,0.12);
            transition: transform 0.15s ease;
        }}
        .cta-button:hover {{
            transform: translateY(-2px);
        }}

        /* Service card */
        .service-card {{
            background: {POWDER_BLUE};
            border-radius: 14px;
            padding: 1.4rem 1.5rem;
            height: 100%;
            border-left: 4px solid {STEEL_BLUE};
        }}
        .service-card h4 {{
            margin-top: 0;
            margin-bottom: 0.4rem;
            font-size: 1.05rem;
        }}
        .service-card p {{
            margin: 0;
            font-size: 0.93rem;
            line-height: 1.5;
            color: {NAVY};
            opacity: 0.85;
        }}

        /* Contact info rows */
        .contact-row {{
            display: flex;
            align-items: center;
            gap: 0.7rem;
            font-family: 'IBM Plex Mono', monospace;
            font-size: 1.05rem;
            padding: 0.5rem 0;
        }}
        .contact-row a {{
            color: {NAVY};
            text-decoration: none;
        }}
        .contact-row a:hover {{
            color: {STEEL_BLUE_DARK};
            text-decoration: underline;
        }}

        footer {{visibility: hidden;}}

        .ecpm-footer {{
            margin-top: 3rem;
            padding-top: 1.2rem;
            border-top: 1px solid {POWDER_BLUE};
            font-size: 0.85rem;
            opacity: 0.65;
            text-align: center;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
