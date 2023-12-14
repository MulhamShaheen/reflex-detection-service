"""Welcome to Reflex!."""

from Reflix import styles

# Import all the pages.
from Reflix.pages import *

import reflex as rx

# Create the app and compile it.
app = rx.App(style=styles.base_style)
app.compile()
