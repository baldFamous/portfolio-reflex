import reflex as rx
from portfolio_reflex.styles.styles import EXPERIENCE_STYLE

def experience() -> rx.Component:
    return rx.vstack(
        rx.heading("Experiencia", textAlign="center", paddingBottom="1rem"),
        rx.stack(
            rx.vstack(
                rx.link("Black Nexus SPA", href="https://www.blacknexus.cl/", fontWeight="bold"),

                rx.text("01/24 - Presente", marginLeft="1rem"),

                rx.text("En este puesto colaboré con el equipo de desarrollo Backend, trabajando en un sistema "
                        "hibrido entre Punto de Venta (POS) y Planificador de recursos empresariales (ERP) "
                        "durante la estadía en este puesto asumimos las tareas desde "
                        "diseñar la base de datos, hasta el desarrollo de la API REST, fuimos participe de reuniones "
                        "semanales para la planificación y revisión de tareas,  ")
            )
        ),
        style=EXPERIENCE_STYLE
    )
