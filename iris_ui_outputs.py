"""_Overview_
This code is used for the outputs that are created after working with 
the iris dataset."""

from shiny import ui

def get_iris_outputs():
    return ui.panel_main(
        ui.hr("Main Panel with Reactive Output"),
        ui.tags.hr(),
        ui.tags.section(
        ui.h3("Iris: Scatter Plot"),
        ui.output_plot("iris_scatterplot"),
        ui.tags.hr(),
        ui.h3("Iris Table"),
        ui.output_text("iris_record_count_string"),
        ui.output_table("iris_table"),
        ui.tags.hr(),
        ),
    )