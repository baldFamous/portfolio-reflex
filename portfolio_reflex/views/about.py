import reflex as rx


def about() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(src="favicon.ico", height="200px", width="200px"),
            rx.heading("Hola, soy Alejandro Sánchez"),
            rx.text(
                "Soy un desarrollador de software apasionado por la tecnología y la programación. "
                "Me encanta aprender y compartir conocimientos. "
                "En este sitio podrás encontrar información sobre mi experiencia, "
                "proyectos y tecnologías que he utilizado."
            ),
        ),
    )