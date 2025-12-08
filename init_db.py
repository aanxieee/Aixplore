import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backend.db import init_db

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully!")
