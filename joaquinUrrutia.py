
#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video], ...]

productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}


#stock = {modelo: [precio, stock], ...]

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}

def stock_marca():
    marca=input("Ingrese modelo a consultar (Ej:GF75HD): ")
    for i in stock.items():
        print("El stock es:",stock[marca][1])
        break



def busqueda_precio():
        try:
            p_min=int(input("Ingrese el precio minimo: "))
            p_max=int(input("Ingrese el precio maximo: "))
            resultados=[]

            for modelo,(precio,inventario) in stock.items():
                if inventario >0 and p_min <=precio <=p_max:
                    marca=productos[modelo][0]
                    resultados.append(f"{marca}--{modelo}")
                    
                    


            if resultados:
                for item in sorted(resultados):
                    print(item)
                    
                    

            else:
                print("No hay notebooks en ese rango de precios")
                
        except ValueError:
            print("Debe ingresar valores enteros") 



def actualizar_precio(modelo,nuevo_precio):
    if modelo in stock:
        stock[modelo][0]=nuevo_precio
        return True
    else:
        return False
    

print("***MENU PRINCIPAL***")
print("1) Stock marca.")
print("2) Búsqueda por precio.")
print("3) Actualizar precio.")
print("4) Salir.")

opc=input("Ingrese opcion: ")

if opc=="1":
    stock_marca()
    
    
elif opc=="2":
    busqueda_precio()

elif opc=="3":
    while True:
        modelo=input("Ingrese modelo a actualizar: ").strip().upper()
        try:
            nuevo_precio=int(input("Ingrese el nuevo precio: ")) 
            if actualizar_precio(modelo,nuevo_precio):
                print("Precio actualizado")
                seguir=input("Desea actualizar otro precio (si/no)? ")
                if seguir!="si":
                    break
            else:
                print("El modelo no existe")

        except ValueError:
            print("Debe ingresar un precio valido (entero).")
            

elif opc=="4":
    print("Programa Finalizado")
    
    
    
else:
    print("Debe seleccionar una opción válida!!")
    
    
    
    
