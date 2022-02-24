from fileinput import filename
from utils.model import Perceptron
from utils.all_utils import prepare_data, save_model, save_plot
import pandas as pd
import numpy as np

def main(data, eta, epochs, filename, plotname):

    model = Perceptron(eta=eta, epochs=epochs)
    model.fit(X, y)

    _ = model.total_loss()

    save_model(model, filename="and.model")
    save_plot(df, "and.png", model)

if __name__=="__main__":  # entry point
    AND = {
    "x1": [0,0,1,1],
    "x2": [0,1,0,1],
    "y": [0,0,0,1],
    }

    df = pd.DataFrame(AND)

    print(df)


    X,y = prepare_data(df)

    ETA = 0.3 # 0 and 1
    EPOCHS = 10

    main(data = AND,eta = ETA, epochs = EPOCHS, filename= "and.model", plotname = "and.png")