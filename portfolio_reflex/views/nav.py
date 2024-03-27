import reflex as rx
from portfolio_reflex.styles.styles import NAV_BAR_STYLE

def nav_bar() -> rx.Component:

    return (rx.flex(

        rx.link("Home", href="/"),
        rx.link("About", href="/about"),
        rx.link("Projects", href="/projects"),
        rx.link("Contact", href="/contact"),
        style=NAV_BAR_STYLE,
    ))


