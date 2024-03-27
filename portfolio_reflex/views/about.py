import reflex as rx
from portfolio_reflex.styles.styles import ABOUT_STYLE


def about() -> rx.Component:
    return rx.hstack(
        rx.image(src="favicon.ico", height="200px", width="200px"),

        rx.vstack(

            rx.heading("Hola, soy Bastian Rodriguez"),
            rx.spacer(),
            rx.text(
                "Hola, soy bastian, soy un programador especializado principalmente en python, "
                "en el Backend web y tambien en el Analisis de datos. "
                "En esta web encontrarás mis proyectos de ambas areas mas destacados, "
                "asi mismo, verás mis redes para saber mas de mi.",

            ),
            rx.hstack(
                rx.link(
                    rx.button(
                        rx.icon("book-open-text"),

                    ),
                    href="/data/bastian_rodriguez_cv_es.pdf",
                    is_external=True
                ),
                rx.link(
                    rx.button(
                        rx.icon("github"),

                    ),
                    href="https://github.com/baldFamous",
                    is_external=True
                ),
                rx.link(
                    rx.button(
                        rx.icon("linkedin"),

                    ),
                    href="https://www.linkedin.com/in/bastian-rodriguez-r-8b0781211/",
                    is_external=True
                ),
            ),

        style=ABOUT_STYLE,
        ),

    )