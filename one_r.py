import pandas

class OneR():
    def __init__(self, d_e, c, d_p):
        self.datos_entrenamiento = d_e
        self.datos_prueba = d_p
        self.clase = c
        self.regla = None

    def tablas_frecuencia(self):
        print("Creando tabla de frecuencias")

        tablas_frecuencia = {}
        for columna in self.datos_entrenamiento.columns:
            frecuencia = self.datos_entrenamiento[columna].value_counts()
            tablas_frecuencia[columna] = frecuencia

        return tablas_frecuencia

    def frecuencia_errores(self, tabla_frecuencia):
        print ("Calulado desempeño")

        reglas = {}
        tasa_errores = {}

        for atributo, tabla in tabla_frecuencia.items():
            reglas_atributo = {}
            tasa_errores = 0.0

            for valor in tabla.index:
                rule = f"If {atributo} is {valor}, predict {tabla.loc[valor]}"
                reglas_atributo[valor] = rule

                # Calculamos la tasa de error para esta regla
                tasa_errores += tabla.loc[valor].sum() - tabla.loc[valor].max()

            # Guardamos las reglas y la tasa de error para este atributo
            reglas[atributo] = reglas_atributo
            tasa_errores[atributo] = tasa_errores / len(tabla.index)

        return tasa_errores

    def seleccionar_tabla(self, t_e):
        print("Seleccionando tabla")

        mejor_tabla = min(t_e, key=t_e.get)
        return mejor_tabla
        
    def evaluar_pruebas(self):
        print("Evaluando datos de prueba")
        aciertos = 0

        # Aplicar la regla a cada instancia
        for i, instancia in self.datos_prueba.iterrows():
            valor_atributo = instancia[self.regla]
            prediccion_clase = self.regla.get(valor_atributo, None)

            if prediccion_clase is not None:
                # Comparar con la clase real
                actual_class = instancia['Play']
                print(f"Instancia {i}: Clase esperada: {actual_class}, Clase estimada: {prediccion_clase}")

                # Actualizar el conteo de predicciones correctas
                if prediccion_clase == actual_class:
                    aciertos += 1
            else:
                print(f"Instancia {i}: No se pudo aplicar la regla para el valor {valor_atributo}")

        # Calcular el porcentaje de acierto
        accuracy = (aciertos / len(self.datos_prueba)) * 100
        print(f"\nPorcentaje de acierto: {accuracy:.2f}%")

    def crear_regla(self):
        tablas = self.tablas_frecuencia()
        t_errores = self.frecuencia_errores(tablas)
        self.regla = self.seleccionar_tabla(t_errores)

