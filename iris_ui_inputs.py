# iris_ui_inputs
#Creating the inputs information for Iris Data set

from shiny import ui
#Creating sliders and table for iris data set
def get_iris_inputs():
    return ui.panel_sidebar(
         ui.h2("Iris Interaction"),
            ui.tags.hr(),
            ui.input_slider(
            "Iris_Sepal_Lenght_Range",
            "Sepal Length (cm)",
            min=0,
            max=8,
            value=[0, 8],
        ),
        ui.input_slider(
            "Iris_Sepal_wider_Range",
            "Sepal Width(cm)",
            min=0,
            max=5,
            value=[0, 5],
        ),
        ui.input_slider(
            "Iris_Petal_Length_range",
            "Petal Length(cm)",
            min=0,
            max=7,
            value=[0, 7],
            ),
        ui.input_slider(
            "Iris_Petal_Width",
            "Petal Width(cm)",
            min=0,
            max=3,
            value=[0, 3],
        ),
        ui.input_checkbox("Iris_Species_setosa", "setosa", value=True),
        ui.input_checkbox("Iris_Species_versicolor", "versicolor", value=True),
        ui.input_checkbox("Iris_Species_virginica", "virginica", value=True),
        ui.tags.hr(),
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )
       
        
        