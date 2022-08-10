n = int(input("Ingrese la cantidad de productos: "))
total=0
ivaTotal=0
products=[]
articles={1:"Lapiz",2:"Cuaderno",3:"Borrador",4:"Regla",5:"ColoresX12",6:"Escuadra",7:"Calculadora",8:"CrayonesX6"}
prices={1:2500,2:4500,3:1500,4:5000,5:24000,6:4700,7:45000,8:8900}
for i in range(1, n+1):
    product = []
    code=int(input("Ingrese el código del producto: "))
    name=articles.get(code)
    amount=int(input("Ingrese la cantidad de productos comprados"))
    price=float(prices.get(code))
    typeIva=int(input("Ingrese el tipo de IVA"))
    priceProduct=price*amount
    if typeIva==1:
        iva=0
    elif typeIva==2:
        iva=priceProduct*0.05
    elif typeIva==3:
        iva=priceProduct*0.19
    ivaPrice=priceProduct+iva
    total+=ivaPrice
    ivaTotal+=iva
    product.append(code)
    product.append(name)
    product.append(priceProduct)
    product.append(ivaPrice)
    products.append(product)
for product in products:
    for x in range(len(product)):
        print(product[x])
print(total)
print(ivaTotal)