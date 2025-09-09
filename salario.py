def salario(horas):
    if (horas == 40):
        salario = 5500
    elif (horas<40):
        salario = (horas *135) *2
    elif (horas>40): 
        horas_extra = horas - 40
        salario = ((horas_extra*135) + 5500)

    return salario

nombre = input("Ingresa tu nombre: ")
semana1 = float(input("Ingresa el numero de horas que trabajaste en la semana 1: "))
semana2 = float(input("Ingresa el numero de horas que trabajaste en la semana 2: "))
rfc = input("Ingresa tu RFC: ")

salario_quincenal = salario(semana1) + salario(semana2)

print(f"El nombre del trabajador es: {nombre}\n Su RFC es: {rfc}\n Su pago quincenal es: {salario_quincenal}" )