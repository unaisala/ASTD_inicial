# ROOT DIRECTORY OF THE PROJECT

from dash import Dash, dcc, html, page_registry, page_container, callback, Output, Input
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SLATE])

# NAVIGATION BAR
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("BY COUNTRY ", href="/")),
        dbc.NavItem(dbc.NavLink("BY YEAR ", href="/page2")),
        dbc.NavItem(dbc.NavLink("MAP ", href="/page3")),
        dbc.NavItem(dbc.NavLink("sectors ", href="/sectors")),
        # dbc.DropdownMenu(
        #     children=[
        #         dbc.DropdownMenuItem("More pages", header=True),
        #         dbc.DropdownMenuItem("Page 2", href="#"),
        #         dbc.DropdownMenuItem("Page 3", href="#"),
        #     ],
        #     nav=True,
        #     in_navbar=True,
        #     label="More",
        # ),
    ],
    brand="CO2 EMISSIONS",
    brand_href="/"#,
    # color="primary",
    # dark=True,
)


# POSSIBLE FOOTER DEFINED HERE 


app.layout = html.Div([
    navbar,
    page_container
])


if __name__ == '__main__': 
    app.run_server (debug=True, port = 8053)
