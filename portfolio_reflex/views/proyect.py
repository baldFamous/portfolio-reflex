import reflex as rx
from portfolio_reflex.styles.styles import PROJECTS_STYLE, CARD_STYLE, IMAGE_STYLE

def projects() -> rx.Component:
    return rx.stack(
        rx.heading("Proyectos"),
        rx.hstack(
            rx.card(
                rx.image(src="favicon.ico", style=IMAGE_STYLE),
                rx.heading("Proyecto 1"),
                rx.text("Descripción del proyecto 1"),
                rx.link(
                    rx.button(
                        rx.icon("link"),
                        color_scheme="purple",
                    ),
                    href="https://github.com/baldFamous",
                    is_external=True
                ),
                style=CARD_STYLE,
            ),
            rx.card(
                rx.image(src="favicon.ico", style=IMAGE_STYLE),
                rx.heading("Proyecto 2"),
                rx.text("Descripción del proyecto 2"),
                rx.link(
                    rx.button(
                        rx.icon("link"),
                        color_scheme="purple",
                    ),
                    href="https://github.com/baldFamous",
                    is_external=True
                ),
                style=CARD_STYLE,
            ),
            rx.card(
                rx.image(src="favicon.ico", style=IMAGE_STYLE),
                rx.heading("Proyecto 3"),
                rx.text("Descripción del proyecto 3"),
                rx.link(
                    rx.button(
                        rx.icon("link"),
                        color_scheme="purple",
                    ),
                    href="https://github.com/baldFamous",
                    is_external=True
                ),
                style=CARD_STYLE,
            ),

        ),
        rx.hstack(
            rx.card(
                rx.image(src="favicon.ico", style=IMAGE_STYLE),
                rx.heading("Proyecto 4"),
                rx.text("Descripción del proyecto 4"),
                rx.link(
                    rx.button(
                        rx.icon("link"),
                        color_scheme="purple",
                    ),
                    href="https://github.com/baldFamous",
                    is_external=True
                ),
                style=CARD_STYLE,
            ),
            rx.card(
                rx.image(src="favicon.ico", style=IMAGE_STYLE),
                rx.heading("Proyecto 5"),
                rx.text("Descripción del proyecto 5"),
                rx.link(
                    rx.button(
                        rx.icon("link"),
                        color_scheme="purple",
                    ),
                    href="https://github.com/baldFamous",
                    is_external=True
                ),
                style=CARD_STYLE,
            ),
            rx.card(
                rx.image(src="favicon.ico", style=IMAGE_STYLE),
                rx.heading("Proyecto 6"),
                rx.text("Descripción del proyecto 6"),
                rx.link(
                    rx.button(
                        rx.icon("link"),
                        color_scheme="purple",
                    ),
                    href="https://github.com/baldFamous",
                    is_external=True
                ),
                style=CARD_STYLE,
            ),

        ),
        style=PROJECTS_STYLE,
    )
