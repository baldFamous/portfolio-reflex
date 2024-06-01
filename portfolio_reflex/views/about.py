import reflex as rx
from portfolio_reflex.styles.styles import ABOUT_STYLE, BUTTON_STYLE, PROJECTS_STYLE



def about() -> rx.Component:
    return rx.stack(
        rx.badge(
            rx.flex(
                rx.icon("check", size=24),
                rx.text(" Disponible ", size="4"),
                spacing="1"
            ),
            color_scheme="green"
        ),
        rx.heading("Bastian Rodriguez, programador junior",
                   marginBottom="1rem",
                   size="9",
                   marginTop="0.1px",
                   fontFamily="monospace",),

        rx.text(
            "Hola, soy bastian, un programador especializado principalmente en Python, "
            "en el Backend web y también en el Análisis de datos. "
            "En esta web encontrarás mis proyectos de ambas áreas, "
            "así mismo, verás mis redes para saber más de mí.",
            size="5",
        ),
        rx.stack(
            rx.link(
                rx.button(
                    rx.icon("book-open-text"), "CV",
                    color_scheme="purple",
                    style=BUTTON_STYLE,
                ),
                href="/data/BASTIAN_CV.pdf",
                is_external=True
            ),
            rx.link(
                rx.button(
                    rx.icon("github"), "GitHub",
                    color_scheme="purple",
                    style=BUTTON_STYLE,
                ),
                href="https://github.com/baldFamous",
                is_external=True
            ),
            rx.link(
                rx.button(
                    rx.icon("linkedin"), "LinkedIn",
                    color_scheme="purple",
                    style=BUTTON_STYLE,
                ),
                href="https://www.linkedin.com/in/bastian-rodriguez-8b0781211/",
                is_external=True
            ),
            rx.link(
                rx.button(
                    rx.icon("mail"), "bastian3967a@gmail.com",
                    color_scheme="purple",
                    style=BUTTON_STYLE,
                ),
                href="mailto:bastian3967a@gmail.com"
            ),

            display="flex",
            justifyContent="space-around",
            flexWrap="wrap",
            padding="1rem",

        ),
        style=ABOUT_STYLE
    )
