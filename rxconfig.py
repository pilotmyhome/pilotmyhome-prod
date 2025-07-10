import reflex as rx

class PilotmyhomeConfig(rx.Config):
    pass

config = PilotmyhomeConfig(
    app_name="pilotmyhome",
    # This line tells the frontend not to attempt a WebSocket connection.
    api_url="javascript:void(0)",
)