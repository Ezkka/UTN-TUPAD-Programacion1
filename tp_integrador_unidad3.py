# Ejercicio 1: Caja del Kiosco

print("--- EJERCICIO 1: CAJA DEL KIOSCO ---")

cliente = input("Nombre del cliente: ")

while cliente.isalpha() == False or cliente == "":
    cliente = input("Error, pone solo letras (sin espacios): ")
    
cant_str = input("Cuantos productos lleva?: ")
while cant_str.isdigit() == False or int(cant_str) <= 0:
    cant_str = input("Error, pone un numero mayor a cero: ")
cantidad_productos = int(cant_str)

plata_sin_desc = 0
plata_con_desc = 0

for i in range(cantidad_productos):
    print(f"\n--- Producto {i + 1} ---")
    
    precio_str = input("Precio del producto: ")
    while precio_str.isdigit() == False or int(precio_str) <= 0:
        precio_str = input("Error, el precio tiene que ser un numero: ")
    precio = int(precio_str)
    
    
    tiene_desc = input("Tiene descuento? (S/N): ").lower()
    while tiene_desc != "s" and tiene_desc != "n":
        tiene_desc = input("Poner S o N nada mas: ").lower()
        
    plata_sin_desc = plata_sin_desc + precio
    
    
    if tiene_desc == "s":
        precio_final = precio - (precio * 0.10)
    else:
        precio_final = precio
        
    plata_con_desc = plata_con_desc + precio_final


ahorro_total = plata_sin_desc - plata_con_desc
promedio = plata_con_desc / cantidad_productos


print("\n--- TICKET ---")
print(f"Cliente: {cliente}")
print(f"Total sin descuentos: ${plata_sin_desc}")
print(f"Total con descuentos: ${plata_con_desc:.2f}")
print(f"Ahorro: ${ahorro_total:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")



# Ejercicio 2: Acceso al Campus y Menu Seguro

print("--- EJERCICIO 2: ACCESO AL CAMPUS ---")

usuario_db = "alumno"
clave_db = "python123"

intentos = 0
pudo_entrar = False


while intentos < 3 and pudo_entrar == False:
    print(f"\nIntento {intentos + 1} de 3")
    user = input("Usuario: ")
    password = input("Clave: ")
    
    if user == usuario_db and password == clave_db:
        pudo_entrar = True
    else:
        print("Error: credenciales invalidas.")
        intentos = intentos + 1
        
if pudo_entrar == False:
    print("Cuenta bloqueada.")
else:
    print("Acceso concedido.")
    salir_menu = False
    
   
    while salir_menu == False:
        print("\n1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        opcion_menu = input("Opcion: ")
        
        while opcion_menu.isdigit() == False:
            opcion_menu = input("Error: ingrese un numero valido. Opcion: ")
        
        opc_int = int(opcion_menu)
        
        if opc_int < 1 or opc_int > 4:
            print("Error: opcion fuera de rango.")
        elif opc_int == 1:
            print("Estado: Inscripto")
        elif opc_int == 2:
            clave_nueva = input("Nueva clave (minimo 6 letras/numeros): ")
            
            while len(clave_nueva) < 6:
                print("Error: minimo 6 caracteres.")
                clave_nueva = input("Nueva clave: ")
            
            clave_repite = input("Confirme nueva clave: ")
            if clave_nueva == clave_repite:
                clave_db = clave_nueva 
                print("Clave cambiada con exito.")
            else:
                print("Las claves no son iguales. Cancelado.")
        elif opc_int == 3:
            print("A estudiar!!")
        elif opc_int == 4:
            print("Saliendo del campus...")
            salir_menu = True



        
# Ejercicio 3: Agenda de Turnos

print("--- EJERCICIO 3: AGENDA DE TURNOS ---")


lunes_t1 = ""
lunes_t2 = ""
lunes_t3 = ""
lunes_t4 = ""

martes_t1 = ""
martes_t2 = ""
martes_t3 = ""

operador = input("Nombre del operador: ")
while operador.isalpha() == False:
    operador = input("Colocar solo letras: ")
    
cerrar_agenda = False

while cerrar_agenda == False:
    print("\n--- AGENDA ---")
    print("1. Reservar")
    print("2. Cancelar")
    print("3. Ver agenda")
    print("4. Ver resumen")
    print("5. Salir")
    
    eleccion = input("Opcion: ")
    while eleccion.isdigit() == False or int(eleccion) < 1 or int(eleccion) > 5:
        eleccion = input("Elegi del 1 al 5: ")
    eleccion = int(eleccion)
    
    if eleccion == 1:
        dia = input("Elegir dia (1=Lunes, 2=Martes): ")
        while dia != "1" and dia != "2":
            dia = input("Solo 1 o 2: ")
            
        paciente = input("Nombre del paciente: ")
        while paciente.isalpha() == False:
            paciente = input("Solo letras: ")
            
        if dia == "1":
            
            if paciente == lunes_t1 or paciente == lunes_t2 or paciente == lunes_t3 or paciente == lunes_t4:
                print("Ese paciente ya esta anotado el Lunes.")
            else:
                
                if lunes_t1 == "": lunes_t1 = paciente; print("Turno Lunes 1 anotado")
                elif lunes_t2 == "": lunes_t2 = paciente; print("Turno Lunes 2 anotado")
                elif lunes_t3 == "": lunes_t3 = paciente; print("Turno Lunes 3 anotado")
                elif lunes_t4 == "": lunes_t4 = paciente; print("Turno Lunes 4 anotado")
                else: print("Lunes lleno total.")
        else:
            if paciente == martes_t1 or paciente == martes_t2 or paciente == martes_t3:
                print("Ese paciente ya esta anotado el Martes.")
            else:
                if martes_t1 == "": martes_t1 = paciente; print("Turno Martes 1 anotado")
                elif martes_t2 == "": martes_t2 = paciente; print("Turno Martes 2 anotado")
                elif martes_t3 == "": martes_t3 = paciente; print("Turno Martes 3 anotado")
                else: print("Martes lleno.")
                
    elif eleccion == 2:
        dia = input("Elegir dia a cancelar (1=Lunes, 2=Martes): ")
        while dia != "1" and dia != "2":
            dia = input("Solo 1 o 2: ")
            
        paciente_borrar = input("Nombre a borrar: ")
        while paciente_borrar.isalpha() == False:
            paciente_borrar = input("Solo letras: ")
        
        lo_borre = False
        
        
        if dia == "1":
            if lunes_t1 == paciente_borrar: lunes_t1 = ""; lo_borre = True
            elif lunes_t2 == paciente_borrar: lunes_t2 = ""; lo_borre = True
            elif lunes_t3 == paciente_borrar: lunes_t3 = ""; lo_borre = True
            elif lunes_t4 == paciente_borrar: lunes_t4 = ""; lo_borre = True
        else:
            if martes_t1 == paciente_borrar: martes_t1 = ""; lo_borre = True
            elif martes_t2 == paciente_borrar: martes_t2 = ""; lo_borre = True
            elif martes_t3 == paciente_borrar: martes_t3 = ""; lo_borre = True
            
        if lo_borre == True:
            print("Turno borrado de la agenda.")
        else:
            print("No esta anotado ese dia.")
            
    elif eleccion == 3:
        dia = input("Que dia queres ver? (1=Lunes, 2=Martes): ")
        while dia != "1" and dia != "2":
            dia = input("Solo 1 o 2: ")
            
        if dia == "1":
            print("\n--- LUNES ---")
            if lunes_t1 == "": print("Turno 1: (libre)") 
            else: print(f"Turno 1: {lunes_t1}")
            
            if lunes_t2 == "": print("Turno 2: (libre)") 
            else: print(f"Turno 2: {lunes_t2}")
            
            if lunes_t3 == "": print("Turno 3: (libre)") 
            else: print(f"Turno 3: {lunes_t3}")
            
            if lunes_t4 == "": print("Turno 4: (libre)") 
            else: print(f"Turno 4: {lunes_t4}")
        else:
            print("\n--- MARTES ---")
            if martes_t1 == "": print("Turno 1: (libre)") 
            else: print(f"Turno 1: {martes_t1}")
            
            if martes_t2 == "": print("Turno 2: (libre)") 
            else: print(f"Turno 2: {martes_t2}")
            
            if martes_t3 == "": print("Turno 3: (libre)") 
            else: print(f"Turno 3: {martes_t3}")
            
    elif eleccion == 4:
        
        cant_lunes = 0
        if lunes_t1 != "": cant_lunes += 1
        if lunes_t2 != "": cant_lunes += 1
        if lunes_t3 != "": cant_lunes += 1
        if lunes_t4 != "": cant_lunes += 1
        
        cant_martes = 0
        if martes_t1 != "": cant_martes += 1
        if martes_t2 != "": cant_martes += 1
        if martes_t3 != "": cant_martes += 1
        
        print("\n--- RESUMEN ---")
        print(f"Lunes: {cant_lunes} ocupados, {4 - cant_lunes} libres.")
        print(f"Martes: {cant_martes} ocupados, {3 - cant_martes} libres.")
        
        if cant_lunes > cant_martes:
            print("El Lunes esta mas lleno.")
        elif cant_martes > cant_lunes:
            print("El Martes esta mas lleno.")
        else:
            print("Estan empatados de turnos.")
            
    elif eleccion == 5:
        print("Cerrar agenda.")
        cerrar_agenda = True




    
# Ejercicio 4: Escape Room (Boveda)

print("--- EJERCICIO 4: LA BOVEDA ---")


energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha = 0 

agente = input("Nombre del agente: ")
while agente.isalpha() == False:
    agente = input("Error, solo letras: ")
    
jugando = True

while jugando == True:
    
    if energia <= 0 or tiempo <= 0:
        print("\nDERROTA. Te quedaste sin energia o tiempo.")
        jugando = False
        continue
        
    if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
        print("\nDERROTA (bloqueo). Sono la alarma y no te da el tiempo.")
        jugando = False
        continue
        
    
    if cerraduras_abiertas == 3:
        print(f"\n¡VICTORIA! Safaste {agente}, abriste todo.")
        jugando = False
        continue
        
    if alarma == True:
        estado_alarma = "ON"
    else:
        estado_alarma = "OFF"
        
    print(f"\n[ Energia: {energia} | Tiempo: {tiempo} | Abiertas: {cerraduras_abiertas}/3 | Alarma: {estado_alarma} ]")
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")
    
    accion_boveda = input("Elegi: ")
    while accion_boveda.isdigit() == False or int(accion_boveda) < 1 or int(accion_boveda) > 3:
        accion_boveda = input("Pone 1, 2 o 3: ")
    accion_boveda = int(accion_boveda)
    
    if accion_boveda == 1:
        racha = racha + 1
        energia = energia - 20
        tiempo = tiempo - 2
        
        if racha == 3:
            alarma = True
            print("Le diste muy fuerte, se trabo la puerta y arranco la alarma.")
        else:
            if energia < 40 and alarma == False:
                print("Estas sin energia casi. Riesgo de alarma!")
                azar = input("Pone un numero 1, 2 o 3: ")
                while azar.isdigit() == False or int(azar) < 1 or int(azar) > 3:
                    azar = input("Dale, un numero del 1 al 3: ")
                
                if azar == "3":
                    alarma = True
                    print("Te la mandaste. Alarma activada!!")
                else:
                    cerraduras_abiertas += 1
                    print("Abriste de milagro en silencio.")
            else:
                if alarma == False:
                    cerraduras_abiertas += 1
                    print("Cerradura abierta, bien ahi.")
                else:
                    print("Ya esta sonando la alarma, no podes forzar sin que se note.")
    
    elif accion_boveda == 2:
        racha = 0
        energia = energia - 10
        tiempo = tiempo - 3
        print("Hackeando la base de datos...")
        
        
        for i in range(4):
            codigo_parcial = codigo_parcial + "A"
            print(f"Hackeo: {codigo_parcial}")
        
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Adentro. Se abrio sola una cerradura.")
    
    elif accion_boveda == 3:
        racha = 0
        energia = energia + 15
        tiempo = tiempo - 1
        if alarma == True:
            energia = energia - 10
            print("El ruido te saca vida (-10 de energia extra).")
            
        if energia > 100:
            energia = 100 
        print("Un respiro no viene mal.")




    
# Ejercicio 5: Escape Room (La Arena del Gladiador)

print("--- EJERCICIO 5: LA ARENA DEL GLADIADOR ---")


vida_mia = 100
vida_bot = 100
mis_pociones = 3
mi_ataque = 15
ataque_bot = 12

print("BIENVENIDO A LA ARENA")
nombre_glad = input("Nombre del Gladiador: ")
while nombre_glad.isalpha() == False:
    print("Error: Solo se permiten letras.")
    nombre_glad = input("Nombre del Gladiador: ")
    
print("\n=== INICIO DEL COMBATE ===")


while vida_mia > 0 and vida_bot > 0:
    print(f"\n{nombre_glad} (HP: {vida_mia}) vs Enemigo (HP: {vida_bot}) | Pociones: {mis_pociones}")
    print("Que vas a hacer?")
    print("1. Ataque Pesado")
    print("2. Rafaga Veloz")
    print("3. Curar")
    
    opcion_pelea = input("Opcion: ")
    while opcion_pelea.isdigit() == False or int(opcion_pelea) < 1 or int(opcion_pelea) > 3:
        print("Error: Ingrese un numero valido entre 1 y 3.")
        opcion_pelea = input("Opcion: ")
    opcion_pelea = int(opcion_pelea)
    
   
    if opcion_pelea == 1:
       
        danio_final = float(mi_ataque)
        if vida_bot < 20:
            danio_final = mi_ataque * 1.5
            print("¡GOLPE CRÍTICO!")
            
        vida_bot = vida_bot - int(danio_final) 
        print(f"¡Atacaste al enemigo por {int(danio_final)} puntos de daño!")
        
    elif opcion_pelea == 2:
        print(">> ¡Inicias una rafaga de golpes!")
        
        for k in range(3):
            vida_bot = vida_bot - 5
            print("> Golpe conectado por 5 de daño")
            
    elif opcion_pelea == 3:
        if mis_pociones > 0:
            vida_mia = vida_mia + 30
            mis_pociones = mis_pociones - 1
            print("Te curaste 30 de vida!")
        else:
            print("¡No quedan pociones!")
    
    
    if vida_bot > 0:
        vida_mia = vida_mia - ataque_bot
        print(f">> ¡El enemigo contraataca y te ataco por {ataque_bot} puntos de daño!")
        print("=== NUEVO TURNO ===")


print("\n=== FIN DE LA BATALLA ===")
if vida_mia > 0:
    print(f"¡VICTORIA! {nombre_glad} ha ganado la batalla.")
else:
    print("DERROTA. Has caido en combate.")