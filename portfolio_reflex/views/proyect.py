import reflex as rx
from portfolio_reflex.styles.styles import PROJECTS_STYLE, CARD_STYLE, IMAGE_STYLE

def projects() -> rx.Component:
    return rx.stack(
        rx.heading("Proyectos"),
        rx.vstack(
            rx.card( # Project 1
                rx.vstack(
                    rx.image(src="project1.png", style=IMAGE_STYLE),
                    rx.heading("Sismo Management"),
                    rx.text(""
                            "Aplicación diseñada para conocer el estado de los sismos "
                            "provenientes de la plataforma USGS, enfocado en EEUU"),
                    rx.link(
                        rx.button(
                            rx.icon("link"), "Link a GitHub",
                            color_scheme="purple",
                        ),
                    href="https://github.com/baldFamous/sismo_project_frogmi",
                    is_external=True
                    )
                ),
                style=CARD_STYLE
            ),
            rx.card(
                rx.vstack( # Project 2
                    rx.image(src="project2.png", style=IMAGE_STYLE),
                    rx.heading("Event Manager"),
                    rx.text(""
                            "Aplicación basica diseñada para gestionar eventos. "
                            "Diseñada para postular a BlackNexus SPA"),
                    rx.link(
                        rx.button(
                            rx.icon("link"), "Link a GitHub",
                            color_scheme="purple",
                        ),
                        href="https://github.com/baldFamous/desafio_blacknexus",
                        is_external=True
                    )
                ),
                style=CARD_STYLE
            ),
            rx.card( # Project 3
                rx.vstack(
                    rx.image(src="favicon.ico", style=IMAGE_STYLE),
                    rx.heading("Titulo"),
                    rx.text(""
                            "Descripción"),
                    rx.link(
                        rx.button(
                            rx.icon("link"), "Link a GitHub",
                            color_scheme="purple",
                        ),
                        href="https://github.com/baldFamous/",
                        is_external=True
                    )
                ),
                style=CARD_STYLE
            ),
            rx.card( # Project 4
                rx.vstack(
                    rx.image(src="favicon.ico", style=IMAGE_STYLE),
                    rx.heading("Titulo"),
                    rx.text(""
                            "Descripción"),
                    rx.link(
                        rx.button(
                            rx.icon("link"), "Link a GitHub",
                            color_scheme="purple",
                        ),
                        href="https://github.com/baldFamous/",
                        is_external=True
                    )
                ),
                style=CARD_STYLE
            ),

            rx.card( # Project 5
                rx.vstack(
                    rx.image(src="favicon.ico", style=IMAGE_STYLE),
                    rx.heading("Titulo"),
                    rx.text(""
                            "Descripción"),
                    rx.link(
                        rx.button(
                            rx.icon("link"), "Link a GitHub",
                            color_scheme="purple",
                        ),
                        href="https://github.com/baldFamous/",
                        is_external=True
                    )
                ),
                style=CARD_STYLE
            ),
            rx.card( # Project 6
                rx.vstack(
                    rx.image(src="favicon.ico", style=IMAGE_STYLE),
                    rx.heading("Titulo"),
                    rx.text(""
                            "Descripción"),
                    rx.link(
                        rx.button(
                            rx.icon("link"), "Link a GitHub",
                            color_scheme="purple",
                        ),
                        href="https://github.com/baldFamous/",
                        is_external=True
                    )
                ),
                style=CARD_STYLE
            ),
        ),
        style=PROJECTS_STYLE,
    )
