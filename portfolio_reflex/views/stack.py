import reflex as rx
from portfolio_reflex.styles.styles import STACKS_STYLE

def stacks() -> rx.Component:
    skills = {
        "Python": ["Django", "Pandas", "Math", "Seaborn", "Sklearn", "Pyspark"],
        "Base de datos": ["Mysql", "Postgresql", "Sqlite"],
        "Control de version": ["GitHub"],
        #"AWS": ["EC2", "Lambda", "Step Functions", "Glue", "S3"],
    }

    def create_skill_sublist(skill_name, subskills):
        return rx.vstack(
            rx.text(skill_name, style={"fontWeight": "bold"}),
            *[
                rx.text(f"— {subskill}")
                for subskill in subskills
            ],
            style={"marginLeft": "2rem"}
        )

    # Componentes de habilidades individuales con sublistas
    skill_components = [
        create_skill_sublist(skill, subskills)
        for skill, subskills in skills.items()
    ]

    return rx.vstack(
        rx.heading("Habilidades"),
        rx.stack(
            *skill_components,
        ),
        style={
            "display": "flex",
            "flexDirection": "column",
            "alignItems": "center",
            "justifyContent": "center",
            "width": "100%",
            "padding": "2rem",
            "gap": "1rem"
        }
    )