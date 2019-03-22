class Recibo:
    # El doble guión que el atributo es privado.
    __costoKw = float(0)
    __lecturaActual = int(0)
    __lecturaAnterior = int(0)
    __consumoKw = float(0)
    __totalApagar = float(0)

     #Se realiza la introducción correspondiente a los datos.
    def __init__(self, costoKw, lecturaActual, lecturaAnterior):
        self.__costoKw = costoKw
        self.__lecturaActual = lecturaActual
        self.__lecturaAnterior =lecturaAnterior

    #Se debe respetar la identación, para que el código logre ejecutarse de manera correcta.
    def calcularCosto(self): #Indica el método
        #Se realizan las lecturas correspondientes
        self.__consumoKw = self.__lecturaActual - self.__lecturaAnterior
        if(self.__consumoKw < 501):
            self.__totalApagar = (self.__consumoKw * self.__costoKw) * 1.22
        if(self.__consumoKw > 500 & self.__consumoKw < 901):
            self.__totalApagar = (self.__consumoKw * self.__costoKw) * 1.18
        if(self.__consumoKw > 900):
            self.__totalApagar = (self.__consumoKw * self.__costoKw) * 1.12

    #Método get, el cual se utiliza para retornar un valor, y dar salidas a los mensajes
    def getTotalApagar(self):
        return self.__totalApagar
