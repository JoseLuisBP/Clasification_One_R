import pandas

class OneR():
    def __init__(self, d_e, c_e, d_p, c_p):
        self.datos_entrenamiento = d_e
        self.clase_entrenamiento = c_e
        self.datos_prueba = d_p
        self.clase_prueba = c_p
        # self.regla

    def tablas_frecuencia(self):
        print ("Creando tablas ...")

    def frecuencia_errores(self):
        print ("Calulado errores")

    def seleccionar_tabla(self):
        print("seleccionando tabla")
        # self.regla = 0
        print("imprime tabla")

    def evaluar_pruebas(self):
        print("evaluando datos de prueba")

    def crear_regla(self):
        self.tablas_frecuencia()
        self.frecuencia_errores()
        self.seleccionar_tabla()

