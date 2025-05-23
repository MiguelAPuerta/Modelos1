import argparse
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from loguru import logger
import os
import pandas as pd
import pickle
import cleaning

logger.info("Training started")

parser = argparse.ArgumentParser()
parser.add_argument('--data_file', required=True, type=str, help='a csv file with train data')
parser.add_argument('--model_file', required=True, type=str, help='where the trained model will be stored')
parser.add_argument('--clean_data', default=True, action='store_true', help='if the set of data isn\'t clear and needs to be cleaned first (default it\'s true to clean the input)')

args = parser.parse_args()

model_file = args.model_file
data_file  = args.data_file
clean = args.clean_data

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