n = int(input("cantidad de productos diferentes: "))
total=0
ivaTotal=0
products=[]
for i in range(1, n+1):
    product = []
    code=int(input("codigo: "))
    name=str(input("nombre: "))
    amount=int(input("cantidad: "))
    price=float(input("Valor unitario: "))
    typeIva=int(input("Tipo de iva: "))
    priceProduct = price*amount
    if typeIva==1:
        iva=0
    elif typeIva==2:
        iva=priceProduct*0.05
    elif typeIva==3:
        iva=priceProduct*0.19
    ivaPrice=priceProduct+iva
    total+=ivaPrice
    ivaTotal+=iva
    product.append(name)
    product.append(code)
    product.append(iva)
    product.append(priceProduct)
    product.append(ivaPrice)
    products.append(product)
products.sort()  
for product in products:
    for datos in range(1,len(product)):
        print(product[datos])
print(total)
print(ivaTotal)