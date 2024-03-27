import reflex as rx
from portfolio_reflex.styles.styles import STACKS_STYLE

def stacks() -> rx.Component:
    return rx.vstack(
        rx.heading("Habilidades"),
        rx.hstack(
            rx.card(
                rx.heading("Python"),
                rx.text("+2 years of on-hands experience"),
            ),
            rx.card(
                rx.heading("Java"),
                rx.text("+1 year of on-hands experience"),
            ),
            rx.card(
                rx.heading("GIT"),
                rx.text("+2 years of on-hands experience"),
            ),
        ),
        style=STACKS_STYLE,
    )