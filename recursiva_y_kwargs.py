

database={"persona1":{"primer nombre": "pablo", "segundo nombre": "emilio", "primer apellido": "gomez", "segundo apellido": "Picasso"},
          "persona2":{"primer nombre": "juan", "segundo nombre": "antonio", "primer apellido": "perez", "segundo apellido": "lopez"}, 
          "persona3":{"primer nombre": "maria", "segundo nombre": "luisa", "primer apellido": "garcia", "segundo apellido": "martinez"},
          "persona4":{"primer nombre": "luis", "primer apellido": "gomez", "segundo apellido": "garcia"},
          "persona5":{"primer nombre": "luis", "segundo nombre": "antonio", "primer apellido": "gomez"}, ##Me quedé sin inspuracion para nombres asique compio y agrego mas claves y datos
            "persona6":{"primer nombre": "luis", "segundo nombre": "antonio", "primer apellido": "gomez", "segundo apellido": "lopez"},
            "persona7":{"primer nombre": "luis", "segundo nombre": "antonio", "primer apellido": "gomez", "segundo apellido": "lopez", "tercer apellido": "martinez"},
            "persona8":{"primer nombre": "luis", "segundo nombre": "antonio", "primer apellido": "gomez", "segundo apellido": "lopez", "tercer apellido": "martinez", "cuarto apellido": "perez"},
            "persona9":{"primer nombre": "luis", "segundo nombre": "antonio", "primer apellido": "gomez", "segundo apellido": "lopez", "tercer apellido": "martinez", "cuarto apellido": "perez", "quinto apellido": "garcia"},
            "persona10":{"primer nombre": "luis", "segundo nombre": "antonio", "primer apellido": "gomez", "segundo apellido": "lopez", "tercer apellido": "martinez", "cuarto apellido": "perez", "quinto apellido": "garcia", "sexto apellido": "gomez"},
            "persona11":{"primer nombre": "luis", "segundo nombre": "antonio", "primer apellido": "gomez", "segundo apellido": "lopez", "tercer apellido": "martinez", "cuarto apellido": "perez", "quinto apellido": "garcia", "sexto apellido": "gomez", "septimo apellido": "perez"},
}

      
def buscar_datos(*args, **database):

    datos_invalidos = 0
    atributos  =  len(args)
    

    for key, datos in database.items():
        
        contador = 0

        for datspersona, Nombres in datos.items():
            
            if len(datos) == atributos: ## si los datos ingresados coinciden con los de la base de datos, se suma 1 a la variable contador
                if Nombres in args:
                    contador += 1
                if atributos == contador: ## si la variable contador es igual a la cantidad de datos ingresados, se retorna el mensaje que indica que la persona existe en la base de datos
                
                    return f"La persona {key} existe en la base de datos."
                
            else: ## si los datos ingresados no coinciden con los de la base de datos, se suma 1 a la variable datos_invalidos
                
                datos_invalidos += 1
                break
            
    if len(database) == datos_invalidos: ## si la cantidad de datos invalidos es igual a la cantidad de datos en la base de datos, se retorna el mensaje que indica que los datos ingresados son insuficientes
        return "Datos ingresados insuficientes para verificar en la base de datos."  
    else:      
        return "La persona que buscas no existe en la base de datos."
           
        


if __name__ == "__main__":
    datospersona=()
    while True:
    
        dnombres = input("Ingrese los datos de la persona que desea buscar: ")
       
        
        datospersona = datospersona + tuple(dnombres.split())
       
        continuar = input("Desea seguir ingresando datos? (s/n): ")

        if continuar == "n":
            
            print(buscar_datos(*datospersona, **database))

            datospersona=()
            dnombres=""

            continuar = input("Desea volver a ingresar datos? (s/n): ")

            if continuar == "n":
                break

    

    