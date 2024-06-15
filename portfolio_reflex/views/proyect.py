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
                    rx.image(src="project3.png", style=IMAGE_STYLE),
                    rx.heading("Event app 2.0"),
                    rx.text("Aplicación para la gestión de eventos, con gestion de usuarios y eventos. "
                            "Principalmente creada para poner en practica técnicas de desarrollo backend y frontend. "
                            "**Aun por afinar detalles**"),
                    rx.link(
                        rx.button(
                            rx.icon("link"), "Link a GitHub",
                            color_scheme="purple",
                        ),
                        href="https://github.com/baldFamous/app-event-manager",
                        is_external=True
                    )
                ),
                style=CARD_STYLE
            ),
            rx.card(  # Project 3
                rx.vstack(
                    rx.image(src="project4.png", style=IMAGE_STYLE),
                    rx.heading("Baby Clothing Store"),
                    rx.text("Pagina web diseñada especialmente para las micro empresas dedicadas a la venta "
                            "de ropa de bebé, con un diseño minimalista y fácil de usar. demo en github Pages "),
                    rx.hstack(
                        rx.link(
                            rx.button(
                                rx.icon("link"), "Link a GitHub",
                                color_scheme="purple",
                            ),
                            href="https://github.com/baldFamous/baby-clothing-store_preview",
                            is_external=True
                        ),
                        rx.link(
                            rx.button(
                                rx.icon("play"), "Demo",
                                color_scheme="purple",
                            ),
                            href="https://baldfamous.github.io/baby-clothing-store_preview/",
                            is_external=True
                        )
                    ),

                ),
                style=CARD_STYLE
            ),
        ),
        style=PROJECTS_STYLE,
    )
