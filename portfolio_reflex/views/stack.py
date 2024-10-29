import reflex as rx

def stacks() -> rx.Component:
    skills = {
        "Python": ("notebook", ["Django", "Tkinter", "Pandas", "Numpy"]),
        "Javascript": ("braces", ["React", "Next.js", "Node.js", "Express"]),
        "Base de datos": ("database", ["Mysql", "Postgresql", "Sqlite"]),
        "Control de version": ("github", ["GitHub"]),
        "AWS": ("cloud", ["EC2", "S3", "IAM"]),
    }

    def create_skill_sublist(skill_name, icon, subskills):
        return rx.vstack(
            rx.hstack(
                rx.icon(icon, size=30),
                rx.text(skill_name, fontWeight="bold"),
            ),
            *[
                rx.text(f"○ {subskill}", align="center", justifyContent="center", width="100%")
                for subskill in subskills
            ],
            marginLeft="1rem"
        )

    skill_components = [
        create_skill_sublist(skill, icon, subskills)
        for skill, (icon, subskills) in skills.items()
    ]

    return rx.vstack(
        rx.stack(
            rx.heading("Habilidades", fontFamily="monospace", size='7'),
            display="flex",
            justifyContent="center",
            width="100%",
            marginBottom="1rem",

        ),
        rx.stack(
            *skill_components,
            display="flex",
            flexWrap="wrap",  # Permite que los elementos se envuelvan
            justifyContent="center",
            width="100%",
            marginBottom="1rem",
            gap="1rem"
        ),
        width="100%",
        padding="2rem",

    )
