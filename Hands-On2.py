class RegresionLineal:
    def __init__(self, x_values, y_values):
        # Inicialización de la clase con valores de x y y
        self.x = x_values
        self.y = y_values
        # Inicialización de variables para los resultados de la regresión
        self.pendiente = None
        self.ordenada_en_el_origen = None
        self.correlacion = None
        # Calcular la regresión lineal y el coeficiente de correlación
        self.calcular_regresion_lineal()
        self.calcular_coeficiente_correlacion()

    def calcular_regresion_lineal(self):
        # Cálculo de sumatorias necesarias para la regresión lineal
        sumX = sum(self.x)
        sumY = sum(self.y)
        sumXY = sum(x * y for x, y in zip(self.x, self.y))
        sumX2 = sum(x ** 2 for x in self.x)
        
        # Cálculo de la pendiente y la ordenada en el origen
        self.pendiente = (len(self.x) * sumXY - sumX * sumY) / (len(self.x) * sumX2 - sumX ** 2)
        self.ordenada_en_el_origen = (sumY - self.pendiente * sumX) / len(self.x)

    def calcular_coeficiente_correlacion(self):
        # Cálculo de sumatorias necesarias para el coeficiente de correlación
        sumX = sum(self.x)
        sumY = sum(self.y)
        sumXY = sum(x * y for x, y in zip(self.x, self.y))
        sumX2 = sum(x ** 2 for x in self.x)
        sumY2 = sum(y ** 2 for y in self.y)
        
        # Cálculo del coeficiente de correlación
        self.correlacion = (len(self.x) * sumXY - sumX * sumY) / (((len(self.x) * sumX2 - sumX ** 2) * (len(self.x) * sumY2 - sumY ** 2)) ** 0.5)

    def calcular_coeficiente_determinacion(self):
        # Cálculo del coeficiente de determinación (R^2)
        return self.correlacion ** 2

    def imprimir_resultados(self):
        # Imprimir resultados de la regresión
        print("\nBeta0:", self.ordenada_en_el_origen, "+ Beta1:", self.pendiente)
        print("\nCoeficiente de correlación:", self.correlacion)
        print("Coeficiente de determinación:", self.calcular_coeficiente_determinacion())

    def predecir_datos_nuevos(self, nuevos_x):
        # Predecir valores para nuevos datos de x
        print("\nPredicciones nuevos datos:")
        for nuevo_x in nuevos_x:
            prediccion = self.pendiente * nuevo_x + self.ordenada_en_el_origen
            print("Para x =",nuevo_x,", la predicción es y =", prediccion)

# Inicializacion del metodo 
if __name__ == "__main__":
    
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    y = [2, 4, 6, 8, 10, 12, 14, 16, 18]

    # Crear una instancia de RegresionLineal
    regresion = RegresionLineal(x, y)

    # Imprimir resultados de la regresión
    regresion.imprimir_resultados()

    # Predecir nuevos valores de y para datos de x nuevos
    nuevos_x = [53, 36, 20, 25, 10]
    regresion.predecir_datos_nuevos(nuevos_x)
