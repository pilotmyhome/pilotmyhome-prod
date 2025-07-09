import reflex as rx

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Pilot My Home"),
            rx.text("Site upgrade in progress. Please check back shortly."),
            spacing="4",
            align="center"
        ),
        height="100vh",
    )

app = rx.App()
app.add_page(index)