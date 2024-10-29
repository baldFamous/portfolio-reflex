import reflex as rx
from portfolio_reflex.styles.styles import PROJECTS_STYLE, CARD_STYLE, IMAGE_STYLE

def projects() -> rx.Component:
    return rx.stack(
        rx.heading("Proyectos",
                   fontFamily="monospace",
                   size='7',
                   display="flex",
                   justifyContent="center",
                   width="100%",
                   marginBottom="1rem"),

        rx.vstack(
            rx.card(  # Project 4
                rx.vstack(
                    rx.image(src="catalogo.png", style=IMAGE_STYLE),
                    rx.heading("Catalogo de productos",),
                    rx.text("Web diseñada para la muestra de productos online "
                            "con la posibilidad de filtrar por categorías.",),
                    rx.hstack(
                        rx.link(
                            rx.button(
                                rx.icon("link"), "Link a GitHub",
                                color_scheme="purple",
                            ),
                            href="https://github.com/baldFamous/catalogo-muestra",
                            is_external=True
                        ),
                        rx.link(
                            rx.button(
                                rx.icon("play"), "Demo",
                                color_scheme="purple",
                            ),
                            href="https://catalogo-muestra.vercel.app",
                            is_external=True
                        )
                    ),

                ),
                style=CARD_STYLE
            ),
        ),
        style=PROJECTS_STYLE,
    )
