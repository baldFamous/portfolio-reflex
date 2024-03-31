import reflex as rx
from portfolio_reflex.styles.styles import EXPERIENCE_STYLE

def experience() -> rx.Component:
    return rx.vstack(
        rx.heading("Experiencia", style={"textAlign": "center", "paddingBottom": "1rem"}),
        rx.stack(
            rx.vstack(
                rx.link("Black Nexus SPA", href="https://www.blacknexus.cl/", style={"fontWeight": "bold"}),
                rx.text("01/24 - Presente", style={"marginLeft": "1rem"}),
                rx.text("Encargado de desarrollar tareas en el backend enfocado "
                        "en el area de integracion de ventas a un sistema POS")
            )
        ),
        style=EXPERIENCE_STYLE
    )
