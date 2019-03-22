from Recibo import Recibo

recibo = Recibo(12.16, 1200, 800) #Ejemplo del primer recibo que se generó
recibo.calcularCosto()
print ('El pago del recibo es de: ', recibo.getTotalApagar())



recibo2 = Recibo(9, 1000, 300) #Ejemplo del segundo recibo quese generó
recibo2.calcularCosto()
print ("El pago del segundo recibo es de: ", recibo2.getTotalApagar())