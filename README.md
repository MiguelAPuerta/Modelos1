# Fase 1

Para la ejecucion de la primera fase solo se debera de ejecutar todo el notebook de manera sequencial, este contiene analisis realizado a la solucion y junto con ese analisis esta la organizacion de la data de entrenamiento y de testeo, al final del notebook se encontraran el modelo entrenado y un resultado de prediccion exportado a un .csv



# Fase 2

docker build -t train-predict .  

docker run --rm -v %cd%:/app --name train-predict train-predict python train.py --data_file train.csv --model_file model.pkl

docker run --rm -v %cd%:/app --name train-predict train-predict python predict.py --input_file test.csv --model_file model.pkl --predictions_file submission.csv
