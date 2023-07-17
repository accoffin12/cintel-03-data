# iris_server.py
"""_Overview_
Creating a new tab for shiny app to display the Iris Data. Initially the csv is loaged into a dataframe 
and then the server functions are defined in the get_iris_server.py file. """

import pathlib
from shiny import render
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


from util_logger import setup_logger
logger, logname = setup_logger(__name__)

def get_iris_server_functions(input, output, session):
    path_to_data = pathlib.Path(__file__).parent.joinpath("data").joinpath("iris.csv")
    iris_df = pd.read_csv(path_to_data)

    total_count = len(iris_df)

    @output
    @render.table
    def iris_table():
        return iris_df
    @output
    @render.text
    def iris_record_count_string():
        message = f"Showing {total_count} records"
        logger.debug(f"filter message: {message}")
        return message

    @output
    @render.plot
    def iris_plot():
        """
        Use Seaborn to make a quick scatterplot.
        Provide a pandas DataFrame and the names of the columns to plot.
        Learn more at https://stackabuse.com/seaborn-scatter-plot-tutorial-and-examples/
        """
        iris_plt = sns.scatterplot(
            data=iris_df,
            x="sepal_length",
            y="sepal_width",
        )
        return iris_plt

    # return a list of function names for use in reactive outputs
    return [
        iris_table,
        iris_record_count_string,
        iris_plot,
    ]
