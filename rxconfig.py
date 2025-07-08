import reflex as rx

class PilotmyhomeConfig(rx.Config):
    pass

config = PilotmyhomeConfig(
    app_name="pilotmyhome",
    db_url="sqlite:///reflex.db",
    env=rx.Env.PROD,
)
