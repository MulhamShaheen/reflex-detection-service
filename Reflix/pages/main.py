"""The main page."""

from Reflix.templates import template

import reflex as rx


@template(route="/main", title="Main")
def main() -> rx.Component:
    """The settings page.

    Returns:
        The UI for the settings page.
    """
    return rx.vstack(
        rx.heading("Main", font_size="3em"),
        rx.text("Welcome to Reflex!"),
        rx.text(
            "You can edit this page in ",
            rx.code("{your_app}/pages/settings.py"),
        ),
    )
