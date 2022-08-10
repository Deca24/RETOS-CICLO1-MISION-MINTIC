n=int(input("Ingrese la cantidad de articulos: "))
PriceTotal=0
ivaTotal=0
code=[]
name=[]
amount=[]
product=[]
TypeIva=[]
PriceProduct=[]
iva=[]
ivaPrice=[]
for i in range (1, n+1):
    code.append(int(input("Ingrese el código del producto: ")))
    name.append(str(input("Ingrese el nombre del producto: ")))
    amount.append(float(input("Ingrese la cantidad de productos comprados: ")))
    product.append(float(input("Precio del Producto sin IVA: ")))
    TypeIva.append(int(input("Ingrese el tipo de IVA: ")))
print(len(code))
print(len(name))
print(len(amount))
print(len(product))
print(len(TypeIva))
for i in range (n):
    PriceProduct.append(amount[i]*product[i])
    if TypeIva[i]==1:
        iva.append(0)
    if TypeIva[i]==2:
        iva.append(PriceProduct[i]*0.05)          
    if TypeIva[i]==3:
        iva.append(PriceProduct[i]*0.19)
    ivaPrice.append(PriceProduct[i]+iva[i])
    ivaTotal+=iva[i]
    PriceTotal+=ivaPrice[i]
    print(code[i])
    print(name[i])
    print(PriceProduct[i])
    print(ivaPrice[i])
print(PriceTotal)
print(ivaTotal)