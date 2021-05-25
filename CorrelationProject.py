import plotly.express as px
import csv 
import numpy as np

def getDataSource():
    coffee = []
    sleep = []
    with open("Coffee.csv") as f:
        df = csv.DictReader(f)
        for row in df:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))

    return {
        "x" : coffee,
        "y" : sleep,
    }

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlatiopn between sleep and coffee",correlation[0,1])

def plotFigure():
    with open("Coffee.csv") as f:
        df = csv.DictReader(f)
        fig = px.scatter(df,x = "Coffee in ml",y="sleep in hours")
        fig.show()
        
        

def main():
    dataSource = getDataSource()
    findCorrelation(dataSource)
    plotFigure()

main()