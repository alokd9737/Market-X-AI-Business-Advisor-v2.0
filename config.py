import os
import streamlit as st

APP_NAME = "Market X AI Business Advisor"

APP_ICON = "💼"

PRIMARY_COLOR = "#0B1F3A"

SECONDARY_COLOR = "#C9A227"

BACKGROUND = "#F7F8FA"

CARD = "#FFFFFF"

TEXT = "#1F2937"

SUCCESS = "#00875A"

WARNING = "#FF8B00"

REPORT_FOLDER = "reports"

LEAD_FOLDER = "leads"

DATA_FOLDER = "data"

LOGO_PATH = "assets/logo.png"

FAVICON = "assets/favicon.png"


def get_secret(key, default=""):
    try:
        return st.secrets.get(key, default)
    except Exception:
        return os.getenv(key, default)
