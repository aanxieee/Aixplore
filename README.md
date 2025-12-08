# AIxplore

Minimal Streamlit scaffold with future FastAPI backend hooks.

## Quick start

```bash
conda activate aixplore
pip install -r requirements.txt
streamlit run app/main.py
```

## Structure

- `app/` Streamlit entry point + pages.
- `backend/` reserved for a FastAPI service.
- `models/` saved ML models later.
- `data/` sample CSV/JSON inputs.

Feel free to drop datasets into `data/` and extend each page stub.
