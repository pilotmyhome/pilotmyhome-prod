import reflex as rx

class PilotmyhomeConfig(rx.Config):
    pass

config = PilotmyhomeConfig(
    app_name="pilotmyhome",
    api_url="http://localhost:8000",
)