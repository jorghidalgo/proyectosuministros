import os 
import datetime

os.system("cls")

fecha_actual=datetime.date.today()

folio=10007
folio=folio+1

suministros=[
             ["p001","Caja de mascarillas medicas",50,3000],
             ["p002","Alcohol Etilico",25,6000],
             ["p003","Termometro de mercurio",20,3000],
             ["p004","Salbutamol",30,3500],
             ["p005","Caja de jeringas",40,8700],
             ["p006","Caja de guantes de latex",30,4000],
             ["p007","Gasas",10,1500],
             ["p008","Vendas",33,5000],
             ["p009","Catèter Intravenoso",5,20000],
             ["p010","Tensiometro digital",2,8000],
            ]



ventas=[
        [10001,fecha_actual,"p001",2,6000],
        [10002,fecha_actual,"p002",3,18000],
        [10003,fecha_actual,"p003",2,6000],
        [10004,fecha_actual,"p004",1,3500],
        [10005,fecha_actual,"p005",4,34800],
        [10006,fecha_actual,"p006",2,8000],
        [10007,fecha_actual,"p007",2,3000],    
        [10008,fecha_actual,"p008",2,10000],
        [10009,fecha_actual,"p009",2,40000],
        [10010,fecha_actual,"p009",2,16000],
            
        ]


opcion=0

######

def buscar_id(id_ingresada):
    for producto in suministros:
        if producto[0] == id_ingresada:
            print(producto[0])
            print(producto[1])
            print(producto[2])
            print(producto[3])
            return producto
        
def buscar_id(id_ingresada):
    for producto in suministros:
        if producto[0] == id_ingresada:
            print(producto[0])
            print(producto[1])
            print(producto[2])
            print(producto[3])
            return producto
   

###########

while opcion<=4:

    print("""
    
               SISTEMA DE VENTAS
        -------------------------------
        1. Vender suministros
        2. Reportes
        3. Mantenedores
        4. Salir
          
          """)
    opcion=int(input("Ingrese una opciòn entre 1-4"))

    match opcion:
        case 1:
            print("vender producto")
        case 2: pass
        case 3:
            os.system("cls")
            op=0
            while op<=6:
                print("""
                            Mantenedor de Productos
                      --------------------------------
                      1. Agregar
                      2. Buscar
                      3. Eliminar 
                      4. Listar
                      5. Salir al menu principal       
                     """ )
                
                op=int(input("ingrese una opcion 1-6 "))
                match op:
                    case 1: 
                        print("\n agregar productos \n")
                        #Agregar
                        print("Agregar suministros a la lista de productos \n")
                        id=input("Ingrese la id ")
                        producto=input("Ingrese el nombre del producto: ")
                        stock=int(input("Ingrese el stock del producto "))
                        precio=int(input("Ingrese el precio del producto"))

                        suministros.append([[id,producto,stock,precio]]) 
                    case 2: #buscar por id
                        print("Buscar producto \n")
                        id_ingresada = input("Ingrese el id a buscar: ")
                        buscar_id(id_ingresada)
                    case 3: 
                        print("Eliminar producto \n")
                        id_ingresada = input("Ingrese la ID del producto a eliminar")
                        eliminar_id(id_ingresada)

                    case 4: 
                        print(suministros)
                    case 5: 
                        if op==5:
                            break
        case 4:
            print("Saliendo...")
            break
            

    if opcion==5:
        break

print("Fin del menu ")     














