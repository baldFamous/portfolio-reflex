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
        rx.heading("Bastian Rodriguez",
                   size="9",
                   marginTop="0.1px",
                   fontFamily="monospace",),

        # rx.text("Python Developer",
        #       marginTop="0.01px",
        #       marginBottom="1rem",
        #       fontFamily="monospace",
        #       size="5",),


        rx.text(
            "Desarrollador FullStack",
            size="5",
            fontFamily="monospace",),

        rx.stack(
            rx.link(
                rx.button(
                    rx.icon("book-open-text"), "CV",
                    color_scheme="purple",
                    style=BUTTON_STYLE,
                ),
                href="/data/R_bastian_cv.pdf",
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
