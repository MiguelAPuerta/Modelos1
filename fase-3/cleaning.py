import numpy as np
import pandas as pd

def rename(df, located, name):
    df.loc[located, 'ESTU_PRGM_ACADEMICO'] = name

def combinations(df):
  located = df['ESTU_PRGM_ACADEMICO'].str.contains('DERECHO') & ~df['ESTU_PRGM_ACADEMICO'].str.contains('DERECHOS')
  rename(df, located, 'DERECHO')
  located = df['ESTU_PRGM_ACADEMICO'].str.contains('EMPRESAS') | (df['ESTU_PRGM_ACADEMICO'].str.contains('ADMINISTRACI') & df['ESTU_PRGM_ACADEMICO'].str.contains('NEGOCIO') & ~df['ESTU_PRGM_ACADEMICO'].str.contains('INTERNACIONALES'))
  rename(df, located, 'ADMINISTRACION DE EMPRESAS')
  located = df['ESTU_PRGM_ACADEMICO'].str.contains('CONTADUR') & ~df['ESTU_PRGM_ACADEMICO'].str.contains('INTERNACIONAL')
  rename(df, located, 'CONTADURIA PUBLICA')
  located = df['ESTU_PRGM_ACADEMICO'].str.contains('PSICOLOG')
  rename(df, located, 'PSICOLOGIA')
  located = df['ESTU_PRGM_ACADEMICO'].str.contains('INGENIE') & df['ESTU_PRGM_ACADEMICO'].str.contains(' INDUSTRIAL')
  rename(df, located, 'INGENIERIA INDUSTRIAL')
  located = df['ESTU_PRGM_ACADEMICO'].str.contains('CIVIL')
  rename(df, located, 'INGENIERIA CIVIL')
  located = df['ESTU_PRGM_ACADEMICO'].str.contains('MEDICINA') & ~df['ESTU_PRGM_ACADEMICO'].str.contains('VETERINARIA')
  rename(df, located, 'MEDICINA')
  located = df['ESTU_PRGM_ACADEMICO'].str.contains('INGENIE') & df['ESTU_PRGM_ACADEMICO'].str.contains('SISTEMAS')
  rename(df, located, 'INGENIERIA DE SISTEMAS')
  located = df['ESTU_PRGM_ACADEMICO'].str.contains('TRABAJO SOCIAL')
  rename(df, located, 'TRABAJO SOCIAL')
  located = df['ESTU_PRGM_ACADEMICO'].str.contains('ENFERMER')
  rename(df, located, 'ENFERMERIA')
  located = df['ESTU_PRGM_ACADEMICO'].str.contains('ARQUITECTURA')
  rename(df, located, 'ARQUITECTURA')
  located = df['ESTU_PRGM_ACADEMICO'].str.contains('SALUD ') & ~df['ESTU_PRGM_ACADEMICO'].str.contains('GERENCIA')
  rename(df, located, 'SALUD OCUPACIONAL')
  located = df['ESTU_PRGM_ACADEMICO'].str.contains('AMBIENTAL') & df['ESTU_PRGM_ACADEMICO'].str.contains('INGENIE')
  rename(df, located, 'INGENIERIA AMBIENTAL')
  located = (df['ESTU_PRGM_ACADEMICO'].str.contains('NEGOCIOS') | df['ESTU_PRGM_ACADEMICO'].str.contains('FINANZAS')) & df['ESTU_PRGM_ACADEMICO'].str.contains('INTERNACIONALES') | (df['ESTU_PRGM_ACADEMICO'].str.contains('CONTADUR') & df['ESTU_PRGM_ACADEMICO'].str.contains('INTERNA'))
  rename(df, located, 'NEGOCIOS INTERNACIONALES')
  located = (df['ESTU_PRGM_ACADEMICO'].str.contains('PEDAGOG') & ~df['ESTU_PRGM_ACADEMICO'].str.contains('REHABILITACI') & ~df['ESTU_PRGM_ACADEMICO'].str.contains('TIERRA') & ~df['ESTU_PRGM_ACADEMICO'].str.contains('ENFASIS') & ~df['ESTU_PRGM_ACADEMICO'].str.contains('REEDUCATIVA')) | df['ESTU_PRGM_ACADEMICO'].str.contains('INFANTIL') | df['ESTU_PRGM_ACADEMICO'].str.contains('PREESCOLAR')
  rename(df, located, 'PEDAGOGIA INFANTIL')
  located = df['ESTU_PRGM_ACADEMICO'].str.contains('ECONOM') & ~df['ESTU_PRGM_ACADEMICO'].str.contains('INTERNACIONAL') & ~df['ESTU_PRGM_ACADEMICO'].str.contains('FILOSOFIA')
  rename(df, located, 'ECONOMIA')
  located = df['ESTU_PRGM_ACADEMICO'].str.contains('MEC') & df['ESTU_PRGM_ACADEMICO'].str.contains('NICA') & ~df['ESTU_PRGM_ACADEMICO'].str.contains('ELECTRO') & ~df['ESTU_PRGM_ACADEMICO'].str.contains('MECATR')
  rename(df, located, 'INGENIERIA MECANICA')
  located = df['ESTU_PRGM_ACADEMICO'].str.contains('ELECTR') & df['ESTU_PRGM_ACADEMICO'].str.contains('NICA') & ~df['ESTU_PRGM_ACADEMICO'].str.contains('MEC')
  rename(df, located, 'INGENIERIA ELECTRONICA')
  located = df['ESTU_PRGM_ACADEMICO'].str.contains('FISIOTERAPIA')
  rename(df, located, 'FISIOTERAPIA')
  located = df['ESTU_PRGM_ACADEMICO'].str.contains('COMUNICACI') & df['ESTU_PRGM_ACADEMICO'].str.contains('SOCIAL')
  rename(df, located, 'COMUNICACION SOCIAL')
  located = df['ESTU_PRGM_ACADEMICO'].str.contains('ODONTOLOG')
  rename(df, located, 'ODONTOLOGIA')
  located = df['ESTU_PRGM_ACADEMICO'].str.contains('ADMINISTRACI') & df['ESTU_PRGM_ACADEMICO'].str.contains('BLICA')
  rename(df, located, 'ADMINISTRACION PUBLICA')
  located = df['ESTU_PRGM_ACADEMICO'].str.contains('QUIMICA')
  rename(df, located, 'INGENIERIA QUIMICA')
  located = df['ESTU_PRGM_ACADEMICO'].str.contains('ADMINISTRACI') & df['ESTU_PRGM_ACADEMICO'].str.contains('FINANCIERA')
  rename(df, located, 'ADMINISTRACION FINANCIERA')
  located = df['ESTU_PRGM_ACADEMICO'].str.contains('VETERINARIA') | df['ESTU_PRGM_ACADEMICO'].str.contains('ZOOTECNIA')
  rename(df, located, 'MEDICINA VETERINARIA')
  top25 = df['ESTU_PRGM_ACADEMICO'].value_counts(dropna=False).head(25).index
  df.loc[~df['ESTU_PRGM_ACADEMICO'].isin(top25), 'ESTU_PRGM_ACADEMICO'] = 'OTROS'

def yes_no_ratio(rate, name, df):
  # Calculate the number of values to replace
  replace_yes = int(rate * df[name].eq('nan').sum())

  # Get indices of values to replace
  replace_indices_yes = df.index[df[name] == 'nan'].tolist()[:replace_yes]
  replace_indices_no = df.index[df[name] == 'nan'].tolist()[replace_yes:]

  # Replace values in the DataFrame
  df.loc[replace_indices_yes, name] = 'Si'
  df.loc[replace_indices_no, name] = 'No'
  df[name].value_counts(dropna=False)

def nan_replace(df):
  df['ESTU_VALORMATRICULAUNIVERSIDAD'] = df['ESTU_VALORMATRICULAUNIVERSIDAD'].replace('nan', 'No pagó matrícula')
  df['ESTU_HORASSEMANATRABAJA'] = df['ESTU_HORASSEMANATRABAJA'].replace('nan', '0')
  df['FAMI_ESTRATOVIVIENDA'] = df['FAMI_ESTRATOVIVIENDA'].replace('nan', 'Sin Estrato')
  df['FAMI_EDUCACIONPADRE'] = df['FAMI_EDUCACIONPADRE'].replace('nan', 'No sabe')
  df['FAMI_EDUCACIONMADRE'] = df['FAMI_EDUCACIONMADRE'].replace('nan', 'No sabe')
  yes_no_ratio(0.89, 'FAMI_TIENEINTERNET', df)
  yes_no_ratio(0.86, 'FAMI_TIENELAVADORA', df)
  yes_no_ratio(0.36, 'FAMI_TIENEAUTOMOVIL', df)
  yes_no_ratio(0.44, 'ESTU_PAGOMATRICULAPROPIO', df)
  yes_no_ratio(0.91, 'FAMI_TIENECOMPUTADOR', df)

def mapping(df):
  mappings = {
        'PERIODO': {
            20213: 8,
            20212: 7,
            20203: 6,
            20202: 5,
            20196: 4,
            20195: 3,
            20194: 2,
            20184: 1,
            20183: 0
        },
        'ESTU_VALORMATRICULAUNIVERSIDAD': {
            'Más de 7 millones': 7,
            'Entre 5.5 millones y menos de 7 millones': 6,
            'Entre 4 millones y menos de 5.5 millones': 5,
            'Entre 2.5 millones y menos de 4 millones': 4,
            'Entre 1 millón y menos de 2.5 millones': 3,
            'Entre 500 mil y menos de 1 millón': 2,
            'Menos de 500 mil': 1,
            'No pagó matrícula': 0
        },
        'ESTU_HORASSEMANATRABAJA': {
            'Más de 30 horas': 4,
            'Entre 21 y 30 horas': 3,
            'Entre 11 y 20 horas': 2,
            'Menos de 10 horas': 1,
            '0': 0
        },
        'FAMI_ESTRATOVIVIENDA': {
            'Estrato 6': 6,
            'Estrato 5': 5,
            'Estrato 4': 4,
            'Estrato 3': 3,
            'Estrato 2': 2,
            'Estrato 1': 1,
            'Sin Estrato': 0
        },
        'FAMI_TIENELAVADORA': {'Si': 1, 'No': 0},
        'FAMI_TIENEINTERNET': {'Si': 1, 'No': 0},
        'FAMI_TIENEAUTOMOVIL': {'Si': 1, 'No': 0},
        'FAMI_TIENECOMPUTADOR': {'Si': 1, 'No': 0},
        'ESTU_PAGOMATRICULAPROPIO': {'Si': 1, 'No': 0},
        'FAMI_EDUCACIONPADRE': {
            'Postgrado': 11,
            'Educación profesional completa': 10,
            'Educación profesional incompleta': 9,
            'Técnica o tecnológica completa': 8,
            'Técnica o tecnológica incompleta': 7,
            'Secundaria (Bachillerato) completa': 6,
            'Secundaria (Bachillerato) incompleta': 5,
            'Primaria completa': 4,
            'Primaria incompleta': 3,
            'Ninguno': 2,
            'No sabe': 1,
            'No Aplica': 0
        },
        'FAMI_EDUCACIONMADRE': {
            'Postgrado': 11,
            'Educación profesional completa': 10,
            'Educación profesional incompleta': 9,
            'Técnica o tecnológica completa': 8,
            'Técnica o tecnológica incompleta': 7,
            'Secundaria (Bachillerato) completa': 6,
            'Secundaria (Bachillerato) incompleta': 5,
            'Primaria completa': 4,
            'Primaria incompleta': 3,
            'Ninguno': 2,
            'No sabe': 1,
            'No Aplica': 0
        }
    }

  for col, mapeo in mappings.items():
    if col in df.columns:
        df[col] = df[col].map(mapeo)
    else:
        print(f"Warning: column {col} not found in DataFrame.")

def mapping_train(df):
  mapeo = {
      'alto': 3,
      'medio-alto': 2,
      'medio-bajo': 1,
      'bajo': 0
  }

  df['RENDIMIENTO_GLOBAL'] = df['RENDIMIENTO_GLOBAL'].map(mapeo)
  mapping(df)

def onehot(df, programa):
  places = df[programa].value_counts(dropna=False).index
  hot = pd.Series(np.zeros(len(df[programa])))
  df_list = df[programa].to_list()
  for i in range(len(places)):
    hot.name = programa+'_'+places[i]
    for j in range(len(hot)):
      if (places[i] == df_list[j]):
        hot[j] = 1
      else:
        hot[j] = 0
    df = pd.concat([df,hot],axis=1)
  df = df.drop(programa, axis=1)
  return df

def finish_data(df):
  for columna in df.columns:
    if df.dtypes[columna] == 'float64':
        df[columna] = df[columna].astype(np.int64)

def clean_train_input(df):
  train = df.copy()

  if 'FAMI_TIENEINTERNET.1' in train.columns:
    train = train.drop('FAMI_TIENEINTERNET.1', axis=1)

  train = train.fillna('nan')
  combinations(train)

  nan_rows = train[train.isin(['nan']).sum(axis=1) >= 9]
  train = train.drop(nan_rows.index)
  train.reset_index(drop=True, inplace=True)
  nan_replace(train)


  if 'ID' in train.columns:
    train = train.drop('ID', axis=1)
  if 'ESTU_PRIVADO_LIBERTAD' in train.columns:
    train = train.drop('ESTU_PRIVADO_LIBERTAD', axis=1)
  mapping_train(train)

  train = onehot(train, 'ESTU_PRGM_DEPARTAMENTO')
  train = onehot(train, 'ESTU_PRGM_ACADEMICO')
  finish_data(train)

  column_to_move = train.pop("RENDIMIENTO_GLOBAL")
  train.insert(len(train.columns), "RENDIMIENTO_GLOBAL", column_to_move)
  return train

def clean_predict_data(test):
  test = test.drop('FAMI_TIENEINTERNET.1', axis=1)

  test = test.fillna('nan')

  combinations(test)

  nan_replace(test)

  if 'ID' in test.columns:
    test = test.drop('ID', axis=1)
  if 'ESTU_PRIVADO_LIBERTAD' in test.columns:
    test = test.drop('ESTU_PRIVADO_LIBERTAD', axis=1)

  mapping(test)

  test = onehot(test, 'ESTU_PRGM_DEPARTAMENTO')
  test = onehot(test, 'ESTU_PRGM_ACADEMICO')
  finish_data(test)
  return test