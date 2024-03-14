import reflex as rx

def stacks() -> rx.Component:
    return rx.vstack(
        rx.heading("Habilidades"),
        rx.hstack(
            rx.card(
                rx.heading("tecnologia1"),
                rx.text("Aquí va la experiencia"),
            ),
            rx.card(
                rx.heading("tecnologia2"),
                rx.text("Aquí van los proyectos"),
            ),
            rx.card(
                rx.heading("tecnologia3"),
                rx.text("Aquí van las tecnologías"),
            ),
            rx.card(
                rx.heading("tecnologia4"),
                rx.text("Aquí va la formación"),
            ),
        )
    )