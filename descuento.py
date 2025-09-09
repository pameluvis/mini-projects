class Descuento:
    def calculo(self, productos: int, subtotal:float):
        if (productos>5 and subtotal>200):
            total = subtotal - (subtotal*.15)
        elif (subtotal>200 and productos<=5):
            total = subtotal - (subtotal*.10)
        elif (subtotal <100 and subtotal<= 200):
            total = subtotal - (subtotal*.5)
        else:
            total = subtotal
        return total
    
monto = float(input("Ingresa el monto total de la compra: "))
productos = int(input("Ingresa el total de productos: "))

d = Descuento()
total_final = d.calculo(productos, monto)

print(f"El total a pagar después del descuento es: {total_final}")