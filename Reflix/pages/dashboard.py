"""The dashboard page."""
from Reflix.templates import template
from .main import State
import reflex as rx


@template(route="/dashboard", title="Dashboard")
def dashboard() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """

    return rx.vstack(
        rx.heading("Dashboard", font_size="3em"),
        rx.text("Welcome to Reflex!"),
        rx.text(
            "You can edit this page in "),
        rx.code("{your_app}/pages/dashboard.py"),
        State.img,
        rx.vstack(
            rx.foreach(
                State.history,
                lambda request:
                rx.card(
                    rx.hstack(
                        rx.image(src=request["source"], width="100px", height="auto"),
                        rx.text(request["datetime"]),

                        header=rx.heading(request["datetime"], size="md"),
                        size="sm",
                    ),
                ),
            )
        ),

    )
