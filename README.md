# EDA_Dashboard
Exploratory Data Analysis Dashboard

## Explanation

This application is an Exploratory Data Analysis (EDA) dashboard that allows the user to interact with the data through different visualization charts. The user can upload a dataset and visualize the data distribution in different ways, including scatterplots, histograms, and boxplots.

The layout of the dashboard is divided into three main components. The first component allows the user to select the x and y columns to be plotted on a scatterplot. The second component is a dropdown that allows the user to select a column for the histogram. The third component is a boxplot that shows the distribution of all numerical columns in the dataset.

The scatterplot and histogram charts are interactive, and the user can change the x and y columns of the scatterplot and the histogram column by selecting different options from the dropdowns. The application uses the Dash framework, Plotly library, and Pandas library to visualize and manipulate the data. The application also uses callbacks to update the charts in real-time based on user inputs.

You can add more functionalities yourself, based on your use case.

## Libraries

-     Pandas: For data manipulation and analysis
-     Dash: For building the web application
-     Dash core components: For building the user interface elements
-     Dash HTML components: For defining the layout of the web application
-     Plotly: For creating interactive plots and charts

To install these libraries run the following command:

`pip install pandas dash dash_core_components dash_html_components plotly
`

## Interface

![Interface](https://user-images.githubusercontent.com/56083377/221260467-b741d7fd-57ac-4988-870a-09eb95fb2b5b.png)
