"""The main page."""
import os

from Reflix.templates import template
import reflex as rx
from ..pipelines import detector
from PIL import Image
import datetime
from typing import TypedDict, List


class DetectionRequest(TypedDict):
    datetime: str
    source: Image.Image
    detects: list[str]


class State(rx.State):
    """The app state."""

    # The images to show.
    img: list[str]
    detects: list[Image.Image]
    history: list[DetectionRequest]

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
            now = datetime.datetime.now()
            with open(outfile, "wb") as file_object:
                file_object.write(upload_data)

            detects_path = f"media/detections/{file.filename}/"
            detector.save_predictions(outfile, detects_path)
            detects = list(os.scandir(detects_path+"crops/person/"))

            src_path = f"media/detections/{file.filename}/crops/person/"

            self.img.append(file.filename)
            self.detects = [Image.open(src_path + d.name) for d in detects]
            self.history.append({
                "datetime": f"{now.day}.{now.month}.{now.year} {now.hour}:{now.minute}",
                "source": Image.open(outfile),
                "detects": [src_path + d.name for d in detects]
            })
            print(self.history)


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
                State.detects,
                lambda img: rx.vstack(
                    rx.image(src=img),
                ),
            ),
            columns=[2],
            spacing="5px",
        ),
        padding="5em",
    )
