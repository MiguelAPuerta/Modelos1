# Fase 1

Para la ejecucion de la primera fase solo se debera de ejecutar todo el notebook de manera sequencial, este contiene analisis realizado a la solucion y junto con ese analisis esta la organizacion de la data de entrenamiento y de testeo, al final del notebook se encontraran el modelo entrenado y un resultado de prediccion exportado a un .csv



# Fase 2

Descargar la carpeta de la fase dos, dentro de esta misma se deberan colocar train.csv y test.csv que se dan como ejemplo para la competición, estos se pueden encontrar en:
https://www.kaggle.com/competitions/udea-ai4eng-20241/data

Contruimos nuestro docker:

    docker build -t train-predict .  

Ejecutamos el codigo para entrenar un modelo:

    docker run --rm -v %cd%:/app --name train-predict train-predict python train.py --data_file train.csv --model_file model.pkl
Esto puede tomar unos minutos.

Finalmente ejecutamos el siguiente comando para predecir con el modelo generado anteriormente:

    docker run --rm -v %cd%:/app --name train-predict train-predict python predict.py --input_file test.csv --model_file model.pkl --predictions_file submission.csv
