from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from loguru import logger
import os
import pandas as pd
import pickle
import cleaning

global train_status

def train_model(data_file, model_file, clean):
    try:
        train_status = "training"
        logger.info("Training started")

        if os.path.isfile(model_file):
          logger.info(f"Overwriting existing model file {model_file}")

        logger.info("Loading train data")
        train = pd.read_csv(data_file)

        if clean:
          logger.info("Cleaning training data")
          train = cleaning.clean_train_input(train)

        X = train.values[:,:-1]
        y = train["RENDIMIENTO_GLOBAL"].values

        Xtr, Xts, ytr, yts = train_test_split(X,y)

        logger.info("Fitting model")
        model = RandomForestClassifier(n_estimators=350, max_depth=20)
        model.fit(Xtr,ytr)

        # save the model
        with open(model_file, "wb") as f:
          pickle.dump(model, f)
        logger.info(f"Training Complete, new model created. Saved to {model_file}")
    except Exception as e:
        logger.error(f"Training failed: {e}")
        train_status = "not training"