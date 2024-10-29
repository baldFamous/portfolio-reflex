ABOUT_STYLE = {
    "display": "flex",
    "flexDirection": "column",
    "alignItems": "center",  # Asegura que el contenido esté centrado horizontalmente
    "justifyContent": "center",  # Centra el contenido verticalmente si es necesario
    "textAlign": "center",  # Centra el texto dentro de los bloques de texto
    "padding": "4rem 0",  # Agrega un padding generoso para una presentación espaciosa
    #"color": "#ffffff",  # Define el color del texto para los bloques de texto
    "width": "100%",  # Utiliza todo el ancho disponible
    "maxWidth": "900px",  # Establece un ancho máximo para el contenido
    "margin": "0 auto",  # Margen automático para centrar el bloque en la página
    "gap": "1rem",  # Espacio entre los componentes verticales
}

# Asegúrate de que los elementos internos también estén centrados
BUTTON_STYLE = {
    "colorScheme": "purple",  # Asume que este estilo existe y aplica el esquema de color
    "margin": "0.5rem",  # Añade márgenes alrededor de los botones para separación
    # Otros estilos para tus botones aquí
}


EXPERIENCE_STYLE = {
    "display": "flex",
    "flexDirection": "column",
    "justifyContent": "center",
    "alignItems": "center",
    "textAlign": "center",
    "flexWrap": "wrap",
    "padding": "4rem",
    "marginBottom": "2rem"
}


PROJECTS_STYLE = {
    "display": "flex",
    "flexDirection": "column",
    "alignItems": "center",
    "justifyContent": "center",
    "marginRight": "2.5rem",
    "width": "100%",
    "padding": "2rem",
    "gap": "1rem"
}


IMAGE_STYLE = {
    "height": "200px",
    "width": "350px",
    "borderRadius": "10px",
    "objectFit": "cover",
}


CARD_STYLE = {
    "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.2)",
    "transition": "0.3s",
    "margin": "1rem",
    "padding": "1rem",
    "borderRadius": "10px",
    "width": "100%",
    "maxWidth": "600px",
    #"backgroundColor": "#f9f9f9",
}


PAGE_CONTAINER_STYLE = {
    "paddingTop": "30px",  # Adjust the top padding to the height of your navbar
    "paddingBottom": "50px",
    "paddingLeft": "40px",
    "paddingRight": "20px",
    "backgroundColor": "#fffff",  # Set a base background color for the page
    "minHeight": "100vh",  # Make sure the page container takes minimum height of the viewport
    "boxSizing": "border-box",
    # centraliza el contenido en el contenedor de la página
    "display": "flex",
    "flexDirection": "column",
    "alignItems": "center",
    "justifyContent": "center",
}