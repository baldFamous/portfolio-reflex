import reflex as rx
from portfolio_reflex.styles.styles import CONTACT_STYLE

def contact() -> rx.Component:
    return rx.form(
        rx.text("Contacto"),
        rx.text("Nombre"), rx.input(placeholder="Nombre"),
        rx.text("Correo"), rx.input(placeholder="Correo"),
        rx.text("Asunto"), rx.input(placeholder="Asunto"),
        rx.button("Enviar"),
        style=CONTACT_STYLE,
    )
