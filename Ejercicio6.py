'''
determine el IVA (19%) de una venta realizada, indicando el valor
original, el valor del IVA y el valor de la venta con IVA incluido
'''
Valor = int(input("Ingrese el valor del producto: $ "))
IVA = 0.19
ValorFinal = (Valor * IVA) + Valor

print("El precio del producto es: ", ValorFinal)






