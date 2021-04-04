from flask import Flask, render_template, request, redirect
import pandas as pd
import random
from bokeh.embed import components
from bokeh.models import HoverTool
from bokeh.plotting import figure, show

app = Flask(__name__)

def get_plot(df):
    #Make plot and customize

    p = figure(plot_width = 400, plot_height = 400, title = 'Sepal width vs. Length')
    x = df['sepal_length']
    y = df['sepal_width']
    p.circle(x, y)
    p.xaxis.axis_label = 'Sepal Length [cm]'
    p.yaxis.axis_label = 'Sepal Width [cm]'
    #p.title.text_font_size = '16pt'
    p.add_tools(HoverTool()) #Need to configure tooltips for a good HoverTool

    #Return the plot
    return(show(p))

@app.route('/')
def homepage():

    #Get the data, from somewhere
    df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
                     names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

    #Setup plot
    p = get_plot(df)
    script, div = components(p)

    #Render the page
    return render_template('home.html', script=script, div=div)




if __name__ == '__main__':
  app.run(port=33507)
