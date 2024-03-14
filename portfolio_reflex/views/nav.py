import reflex as rx

def nav_bar() -> rx.Component:
    return (rx.flex(
        rx.link("Home", href="/"),
        rx.link("About", href="/about"),
        rx.link("Projects", href="/projects"),
        rx.link("Contact", href="/contact")
    ))
