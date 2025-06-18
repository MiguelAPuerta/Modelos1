import pandas as pd
import pickle
from loguru import logger
import cleaning

global predict_status

def predict_model(input_file, predictions_file, model_file, clean):
    try:
        predict_status = "predicting"
        logger.info("Prediction started")

        logger.info("Loading input data")
        predict_df = pd.read_csv(input_file)
        testID = predict_df[['ID']].copy()

        if clean:
            logger.info("Cleaning prediction data")
            predict_df = cleaning.clean_predict_data(predict_df)

        values = predict_df.values

        logger.info("Loading model")
        with open(model_file, 'rb') as f:
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
        logger.info(submission.head().to_dict(orient='records'))
        submission.to_csv(predictions_file, index=False)
    except Exception as e:
        logger.error(f"predicting failed: {e}")
        predict_status = "not predicting"