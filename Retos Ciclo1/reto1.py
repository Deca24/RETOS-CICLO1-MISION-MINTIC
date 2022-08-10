n=int(input("Ingrese la cantidad de articulos: "))

PriceTotal=0

for i in range (1, n+1):
    code=int(input("Ingrese el código del producto: "))
    name=str(input("Ingrese el nombre del producto: "))
    amount=float(input("Ingrese la cantidad de productos: "))
    product=float(input("Ingrese el precio del producto: "))
    PriceProduct=product*amount
    Iva=PriceProduct*0.19
    ValorFinal=PriceProduct+Iva
    PriceTotal+=ValorFinal
    print(f"Código: {code}")
    print(f"Nombre: {name}")
    print(f"Precio con iva: {ValorFinal}")
print(f"Valor total a pagar: {PriceTotal}")
