import reflex as rx
from portfolio_reflex.styles.styles import ABOUT_STYLE

def experience() -> rx.Component:
    return rx.vstack(
        rx.heading("Experiencia",
                   fontFamily="monospace",
                   size='7',
                   display="flex",
                   justifyContent="center",
                   width="100%",
                   marginBottom="1rem"),
        rx.stack(
            rx.vstack(
                rx.link("Black Nexus SPA", href="https://www.blacknexus.cl/", fontWeight="bold"),

                rx.text("01/24 - 04/24", marginLeft="1rem"),

                rx.text("• Participé en el desarrollo de una API para un software Punto de venta", rx.spacer(),
                        "• Diseñé junto a un equipo el modelo de datos del software.", rx.spacer(),
                        "• Me encargué de crear las peticiones HTTP encargadas de las ventas y detalle de ventas,",
                         "asegurando la correcta funcionalidad y eficiencia del sistema.",
                        size='4',
                        justifyContent="center",)
            )
        ),
        style=ABOUT_STYLE
    )
