"""The main page."""

from Reflix.templates import template
import reflex as rx


class State(rx.State):
    """The app state."""

    # The images to show.
    img: list[str]

    async def handle_upload(
            self, files: list[rx.UploadFile]
    ):
        """Handle the upload of file(s).

        Args:
            files: The uploaded files.
        """
        for file in files:
            upload_data = await file.read()
            outfile = f"media/{file.filename}"

            # Save the file.
            with open(outfile, "wb") as file_object:
                file_object.write(upload_data)

            # Update the img var.
            self.img.append(file.filename)


@template(route="/main", title="Main")
def main() -> rx.Component:
    """The main view."""
    return rx.vstack(
        rx.heading("Main page"),
        rx.text("Загрузите сюда фотографию для дитекции"),
        rx.upload(
            rx.vstack(
                rx.button(
                    "Select File",
                    bg="white",
                    border=f"1px solid",
                ),
                rx.text(
                    "Drag and drop files here or click to select files"
                ),
            ),
            multiple=False,
            accept={
                "image/png": [".png"],
                "image/jpeg": [".jpg", ".jpeg"],
            },
            max_files=1,
            border=f"1px dotted",
            padding="5em",
        ),
        rx.button(
            "Upload",
            on_click=lambda: State.handle_upload(
                rx.upload_files()
            ),
        ),
        rx.responsive_grid(
            rx.foreach(
                State.img,
                lambda img: rx.vstack(
                    rx.image(src=img),
                    rx.text(img),
                ),
            ),
            columns=[2],
            spacing="5px",
        ),
        padding="5em",
    )
