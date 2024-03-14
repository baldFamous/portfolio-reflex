from rxconfig import config
import reflex as rx
from portfolio_reflex.views.about import about
from portfolio_reflex.views.nav import nav_bar
from portfolio_reflex.views.stack import stacks
from portfolio_reflex.views.proyect import proyects
from portfolio_reflex.views.contact import contact

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
google = "https://www.google.com"
linkedin = "https://www.linkedin.com"
filename = f"{config.app_name}/{config.app_name}.py"



def index() -> rx.Component:
    return rx.vstack(
        nav_bar(),
        about(),
        rx.spacer(),
        stacks(),
        proyects(),
        contact(),

    )

app = rx.App()
app.add_page(index)
