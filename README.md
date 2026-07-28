<img src="assets/logo_steelblue.png" height="80" alt="E-CPM logo" />

**Canadian Professional Property Management**  
Reliable, skilled, and experienced care for your property.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ecpmsa.streamlit.app/)

---

### Run locally

**Option A — with `uv` (recommended, faster)**

`uv` is a fast Python package manager. Install it once on Windows:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Then run the app:

```powershell
uv sync
uv run streamlit run streamlit_app.py
```

**Option B — with plain `pip`**

```powershell
pip install streamlit
streamlit run streamlit_app.py
```
