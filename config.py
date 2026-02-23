"""Configuration settings for the HealthGPT application."""

# App settings
APP_CONFIG = {
    "page_title": "HealthGPT - Your AI Health Assistant",
    "page_icon": "🏥",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# Theme colors
THEME = {
    "primary": "#3b82f6",
    "secondary": "#1d4ed8",
    "accent": "#60a5fa",
    "background": "#0f172a",
    "surface": "#1e293b",
    "text": "#e2e8f0",
    "text_secondary": "#94a3b8",
    "border": "#334155",
    "hover": "#2563eb"
}

# Model settings
MODEL_CONFIG = {
    "name": "gpt-oss:120b-cloud",
    "base_url": "http://localhost:11434/"
}

# Default user profile
DEFAULT_USER_PROFILE = {
    "name": "",
    "age": "",
    "gender": "",
    "conditions": [],
    "medications": [],
    "allergies": [],
    "last_checkup": ""
}
