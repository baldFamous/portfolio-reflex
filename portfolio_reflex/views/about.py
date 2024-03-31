import reflex as rx
from portfolio_reflex.styles.styles import ABOUT_STYLE, BUTTON_STYLE


def about() -> rx.Component:
    return rx.stack(
        rx.heading("Bastian Rodriguez, programador junior", style={"marginBottom": "1rem"}),
        rx.image(src="favicon.ico", height="200px", width="200px", style={"alignSelf": "center"}),
        rx.text(
            "Hola, soy bastian, soy un programador especializado principalmente en python, "
            "en el Backend web y también en el Análisis de datos. "
            "En esta web encontrarás mis proyectos de ambas áreas más destacados, "
            "así mismo, verás mis redes para saber más de mí.",
            style={"marginBottom": "1rem"}  # Añade espacio debajo del texto
        ),
        rx.stack(
            rx.link(
                rx.button(
                    rx.icon("book-open-text"),
                    color_scheme="purple",
                    style=BUTTON_STYLE,
                ),
                href="/data/bastian_rodriguez_cv_es.pdf",
                is_external=True
            ),
            rx.link(
                rx.button(
                    rx.icon("github"),
                    color_scheme="purple",
                    style=BUTTON_STYLE,
                ),
                href="https://github.com/baldFamous",
                is_external=True
            ),
            rx.link(
                rx.button(
                    rx.icon("linkedin"),
                    color_scheme="purple",
                    style=BUTTON_STYLE,
                ),
                href="https://www.linkedin.com/in/bastian-rodriguez-r-8b0781211/",
                is_external=True
            ),
            rx.link(
                rx.button(
                    rx.icon("mail"),
                    color_scheme="purple",
                    style=BUTTON_STYLE,
                ),
                href="mailto:curso.bastian@gmail.com"
            ),
            style={"justifyContent": "center"}
        ),
        style=ABOUT_STYLE
    )