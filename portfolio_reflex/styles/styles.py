NAV_BAR_STYLE = {
    "display": "flex",
    "justifyContent": "space-evenly",  # This will distribute the spacing evenly
    "alignItems": "center",
    "padding": "10px 0",  # Slightly reduce the padding for a sleeker look
    "backgroundColor": "#20232a",  # A dark grey that's easier on the eyes than pure black
    "color": "#61dafb",  # A bright color for the links, often used in tech/design themes
    "fontFamily": "'Segoe UI', Roboto, Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif",
    "boxShadow": "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",  # A more nuanced shadow for depth
    "position": "fixed",  # Changed to 'fixed' to remain at the top when scrolling
    "top": "0",
    "left": "0",
    "right": "0",
    "zIndex": "1000",  # Ensure it stays above other content
    "height": "50px",  # A moderate height for the nav bar
    "borderBottom": "2px solid #61dafb",  # A bottom border to highlight the nav bar
}


ABOUT_STYLE = {
    "textAlign": "center",
    "padding": "4rem 0",  # Add generous padding for airy presentation
    "color": "#ffffff",  # Light grey background for the about section
}


STACKS_STYLE = {
    "display": "flex",
    "justifyContent": "space-around",
    "flexWrap": "wrap",  # This allows the contents to wrap on smaller screens
    "padding": "2rem",
}


PROJECTS_STYLE = {
    "display": "grid",
    "gap": "1rem",
    "padding": "2rem",
    #"backgroundColor": "#ffffff",
}


IMAGE_STYLE = {
    "height": "200px",
    "width": "auto",
    "borderRadius": "10px",
}


CARD_STYLE = {
    "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.2)",
    "transition": "0.3s",
    "margin": "1rem",
    "padding": "1rem",
    "borderRadius": "10px",
    #"backgroundColor": "#f9f9f9",
}


CONTACT_STYLE = {
    "display": "flex",
    "flexDirection": "column",
    "width": "50%",
    "maxWidth": "500px",
    "margin": "2rem auto",
    "padding": "2rem",
    "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
    "borderRadius": "8px",
    "backgroundColor": "#f9f9f9",
}


PAGE_CONTAINER_STYLE = {
    "paddingTop": "134px",  # Adjust the top padding to the height of your navbar
    "paddingBottom": "20px",
    "paddingLeft": "40px",
    "paddingRight": "20px",
    #"backgroundColor": "#fffff",  # Set a base background color for the page
    "minHeight": "100vh",  # Make sure the page container takes minimum height of the viewport
    "boxSizing": "border-box",
}