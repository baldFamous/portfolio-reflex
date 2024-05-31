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
        about(),
        rx.spacer(),
        stacks(),
        rx.spacer(),
        projects(),
        rx.spacer(),
        experience(),
        style=PAGE_CONTAINER_STYLE,
        background="radial-gradient(circle at 22% 11%, rgba(62, 180, 137, .40), hsla(0, 0%, 100%, 0) 19%), "
                   "radial-gradient(circle at 82% 25%, rgba(33, 150, 243, .36), hsla(0, 0%, 100%, 0) 35%), "
                   "radial-gradient(circle at 25% 61%, rgba(250, 128, 114, .56), hsla(0, 0%, 100%, 0) 55%)",


    )


app = rx.App(
    theme=rx.theme(
        appearance="dark", has_background=True, radius="medium", accent_color="mint"
    ),
)
app.add_page(index)
