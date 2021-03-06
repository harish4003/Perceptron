from utils.model import Perceptron
from utils.all_utils import prepare_data, save_model, save_plot
import pandas as pd
import numpy as np

def main(data, eta, epochs, filename, plotname):

    model = Perceptron(eta=eta, epochs=epochs)
    model.fit(X, y)

    _ = model.total_loss()

    save_model(model, filename="or.model")
    save_plot(df, "or.png", model)

if __name__=="__main__":  # entry point
    OR = {
    "x1": [0,0,1,1],
    "x2": [0,1,0,1],
    "y": [0,1,1,1],
    }

    df = pd.DataFrame(OR)

    print(df)


    X,y = prepare_data(df)

    ETA = 0.3 # 0 and 1
    EPOCHS = 10

    main(data = OR,eta = ETA, epochs = EPOCHS, filename= "or.model", plotname = "or.png")