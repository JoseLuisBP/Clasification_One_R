import pandas

from one_r import OneR


def main():
    archivo_ubicacion = "datasets/golf-dataset-categorical.csv"
    tam_conjunto_entrenamiento = 0.7
    columna_clase = 'Play'

    conjunto_datos = pandas.read_csv(archivo_ubicacion)

    atributos_entrenamiento = conjunto_datos.sample(frac=tam_conjunto_entrenamiento)
    clase_entrenamiento = atributos_entrenamiento[columna_clase]
    atributos_entrenamiento = atributos_entrenamiento.drop(columns = columna_clase)

    atributos_prueba = conjunto_datos.drop(atributos_entrenamiento.index)
    clase_prueba = atributos_prueba[columna_clase]
    atributos_prueba = atributos_prueba.drop(columns = [columna_clase])

    modelo = OneR(atributos_entrenamiento, clase_entrenamiento, atributos_prueba, clase_prueba)

    modelo.crear_regla()

    modelo.evaluar_pruebas()

if __name__ == '__main__':
    main()