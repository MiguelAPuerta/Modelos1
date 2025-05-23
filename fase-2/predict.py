import argparse
import numpy as np
import os
import pandas as pd
import pickle
from loguru import logger
import cleaning

logger.info("Prediction started")

parser = argparse.ArgumentParser()
parser.add_argument('--input_file', required=True, type=str, help='a csv file with input data (no targets)')
parser.add_argument('--predictions_file', required=True, type=str, help='a csv file where predictions will be saved to')
parser.add_argument('--model_file', required=True, type=str, help='a pkl file with a model already stored (see train.py)')
parser.add_argument('--clean_data', default=True, action='store_true', help='if the set of data isn\'t clear and needs to be cleaned first (default it\'s true to clean the input)')

args = parser.parse_args()

model_file       = args.model_file
input_file        = args.input_file
predictions_file = args.predictions_file
clean = args.clean_data

if not os.path.isfile(model_file):
    logger.error(f"Model file {model_file} does not exist")
    exit(-1)

if not os.path.isfile(input_file):
    logger.error(f"Input file {input_file} does not exist")
    exit(-1)


logger.info("Loading input data")
predict_df = pd.read_csv(input_file)
testID = predict_df[['ID']].copy()

if clean:
    logger.info("Cleaning prediction data")
    predict_df = cleaning.clean_predict_data(predict_df)

values = predict_df.values

logger.info("Loading model")
with open('model.pkl', 'rb') as f:
    m = pickle.load(f)

logger.info("Making predictions")
preds = m.predict(values)

submission = pd.DataFrame([testID.ID, pd.Series(preds, name="RENDIMIENTO_GLOBAL")]).T

mapeo = {
    3: 'alto',
    2: 'medio-alto',
    1: 'medio-bajo',
    0: 'bajo'
}

submission['RENDIMIENTO_GLOBAL'] = submission['RENDIMIENTO_GLOBAL'].map(mapeo)

logger.info(f"Saving predictions to {predictions_file}")
submission.to_csv(predictions_file, index=False)