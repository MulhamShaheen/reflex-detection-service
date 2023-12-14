"""The home page of the app."""

from Reflix import styles
from Reflix.templates import template

import reflex as rx


@template(route="/", title="Home", image="/github.svg")
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    rx.heading("Main", font_size="3em"),
    rx.text("Welcome to Reflex!"),
    rx.text(
        "You can edit this page in ",
        rx.code("{your_app}/pages/settings.py"),
    ),
    with open("README.md", encoding="utf-8") as readme:
        content = readme.read()

    return rx.markdown(content, component_map=styles.markdown_style)
