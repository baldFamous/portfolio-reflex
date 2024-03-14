import reflex as rx

def proyects() -> rx.Component:
    return rx.vstack(
        rx.heading("Proyectos"),
        rx.hstack(
            rx.card(
                rx.image(src="favicon.ico", height="200px", width="200px"),
                rx.heading("Proyecto 1"),
                rx.text("Descripción del proyecto 1"),
            ),
            rx.card(
                rx.image(src="favicon.ico", height="200px", width="200px"),
                rx.heading("Proyecto 2"),
                rx.text("Descripción del proyecto 2"),
            ),
            rx.card(
                rx.image(src="favicon.ico", height="200px", width="200px"),
                rx.heading("Proyecto 3"),
                rx.text("Descripción del proyecto 3"),
            ),
        )
    )