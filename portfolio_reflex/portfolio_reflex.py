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
        style=PAGE_CONTAINER_STYLE
    )


app = rx.App(
)
app.add_page(index)
