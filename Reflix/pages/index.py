"""The home page of the app."""

from Reflix.templates import template

import reflex as rx


@template(route="/", title="Home", image="/github.svg")
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """

    return rx.vstack(
        rx.heading("Reflex People Detection Service", font_size="2em"),
        rx.text("A service created to demonstrate web framework ",
                rx.link("Reflex", href="https://reflex.dev/")),
        rx.divider(),
        rx.grid(
            rx.grid_item(
                rx.card(
                    rx.text(
                        "Image upload form page, where you can upload an image for processing\n "
                        "For detection, the service uses ",
                        rx.code("YOLOv8")),
                    header=rx.heading("Main", size="lg"),
                    footer=rx.link("To main >", href="/main", size="sm"),
                    size="md",
                    justify="space-between"
                ),
                row_span=1,
                col_span=1
            ),
            rx.grid_item(
                rx.card(
                    rx.text("The page where you can see the history of you user requests. "
                            "Authentication not available yet"),
                    header=rx.heading("Dashboard", size="lg"),
                    footer=rx.link("To dashboard >", href="/dashboard", size="sm"),
                    size="md",
                    justify="space-between"
                ),
                row_span=1, col_span=1),
            template_columns="repeat(2, 1fr)",
            h="100%",
            gap=4,
        )
    )
