from rxconfig import config
import reflex as rx
from portfolio_reflex.views.about import about
from portfolio_reflex.views.stack import stacks
from portfolio_reflex.views.proyect import projects
from portfolio_reflex.views.experience import experience
from portfolio_reflex.styles.styles import PAGE_CONTAINER_STYLE

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
google = "https://www.google.com"
linkedin = "https://www.linkedin.com"
filename = f"{config.app_name}/{config.app_name}.py"

def index() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.color_mode.switch(padding_top="2px"),
            rx.text("Light/Dark")
        ),

        about(),
        rx.spacer(),
        stacks(),
        rx.spacer(),
        projects(),
        rx.spacer(),
        experience(),
        style=PAGE_CONTAINER_STYLE,
        background="radial-gradient(circle at 22% 11%, rgba(62, 180, 137, .57), hsla(0, 0%, 100%, 0) 29%), " # verde
                   "radial-gradient(circle at 82% 29%, rgba(33, 150, 243, .57), hsla(0, 0%, 100%, 0) 35%), " # azul
                   "radial-gradient(circle at 25% 61%, rgba(250, 128, 114, .57), hsla(0, 0%, 100%, 0) 45%)," # rojo
                   "radial-gradient(circle at 82% 95%, rgba(190, 214, 74, .57), hsla(0, 0%, 100%, 0) 45%)", # amarillo


    )


app = rx.App(
    theme=rx.theme(
        has_background=False, radius="full", accent_color="mint"
    ),
)
app.add_page(index)
