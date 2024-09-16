import time
import os


alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


def limpiar_pantalla():

    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Linux y macOS
        os.system('clear')


def cifrar(nombre_cifrado):
    limpiar_pantalla()

    if nombre_cifrado == "Cesar":
        print("CIFRADO DEL CESAR\n\n")

        texto = input("Introduce el texto a cifrar: ").upper()

        print(f"\nMensaje cifrado: {cifrar_cesar(texto)}")

        aux = input("\n\nPresiona cualquier tecla para regresar...")
        sub_menu("Cesar")

    elif nombre_cifrado == "Polybios":
        print("CIFRADO POLYBIOS\n\n")
        return
    elif nombre_cifrado == "Vigenere":
        print("CIFRADO VIGENÉRE\n\n")

        texto = input("Introduce el texto a cifrar: ").upper()
        clave = input("Introduce la clave: ").upper()

        cifrar_vegenere(texto, clave)

        aux = input("\n\nPresiona cualquier tecla para regresar...")
        sub_menu("Vigenere")
    else:
        print("Error")
        time.sleep(2)
        menu()


def decifrar(nombre_cifrado):
    limpiar_pantalla()

    if nombre_cifrado == "Cesar":
        print("CIFRADO DEL CESAR\n\n")
        texto_cifrado = input("Introduce el texto cifrado: ").upper()

        print(f"\nMensaje descifrado: {descifrar_cesar(texto_cifrado)}")


        aux = input("\n\nPresiona cualquier tecla para regresar...")
        sub_menu("Cesar")

    elif nombre_cifrado == "Polybios":
        print("CIFRADO POLYBIOS\n\n")

        return
    elif nombre_cifrado == "Vigenere":
        print("CIFRADO VIGENÉRE\n\n")

        texto_cifrado = input("Introduce el texto cifrado: ").upper()
        clave = input("Introduce la clave: ").upper()

        descifrar_vegenere(texto_cifrado, clave)

        aux = input("\n\nPresiona cualquier tecla para regresar...")
        sub_menu("Vigenere")
    else:
        print("Error")
        time.sleep(2)
        menu()


#Cifrado Vegenére

def texto_Clave_vegenere(texto, clave):
    #variables de apoyo
    clave_expandida = ""
    indice_clave = 0

    #Recorrido por el texto plano
    for letra in texto:
        #Verificar que el caracter es una letra o un "Ñ"
        if letra.isalpha() or letra == "Ñ":
            #Guarda el resultado de igualar el caracter del texto plano con el de la clave
            clave_expandida += clave[indice_clave % len(clave)].upper() #
            indice_clave += 1
        else:
            #Cuando el caracter es un espacio, lo almacena
            clave_expandida += letra  
          
    return clave_expandida

def cifrar_vegenere(texto, clave):
    
    llave = texto_Clave_vegenere(texto, clave)
    resultado = ""
    indice_clave = 0

    for letra in texto:
        if letra.isalpha() or letra == "Ñ":

            valor_letra_texto = alfabeto.index(letra.upper())
            valor_letra_llave = alfabeto.index(llave[indice_clave].upper())

            valor_resultado = (valor_letra_texto + valor_letra_llave) % len(alfabeto)
            resultado += alfabeto[valor_resultado]

            indice_clave += 1
        else:
            resultado += letra  # Mantener espacios y otros caracteres sin cambios
            indice_clave += 1

    print(f"\nTexto cifrado: {resultado}")


#Cifrado el Cesar

def cifrar_cesar(mensaje, desplazamiento=3):
    """
    Cifra un mensaje usando el cifrado César con un desplazamiento de 3 por defecto.
    """
    resultado = []
    
    for letra in mensaje:
        if letra.isalpha():  # Si es una letra
            base = ord('A') if letra.isupper() else ord('a')
            nueva_letra = chr((ord(letra) - base + desplazamiento) % 26 + base)
            resultado.append(nueva_letra)
        else:
            # Si no es una letra, lo dejamos como está (espacios, puntuación, etc.)
            resultado.append(letra)
    
    return ''.join(resultado)

"""
DECIFRADOS
"""

#Decifrado del Cesar

def descifrar_cesar(mensaje, desplazamiento=3):
    """
    Descifra un mensaje cifrado con el cifrado César, usando el mismo desplazamiento.
    """

    #print(cifrar_cesar(mensaje, -desplazamiento))
    return cifrar_cesar(mensaje, -desplazamiento)  # Invertimos el desplazamiento para descifrar

#Decifrado Vegenére

def descifrar_vegenere(texto_cifrado, clave):
    llave = texto_Clave_vegenere(texto_cifrado, clave)
    resultado = ""
    indice_clave = 0

    for letra in texto_cifrado:
        if letra.isalpha() or letra == "Ñ":

            valor_letra_texto = alfabeto.index(letra.upper())
            valor_letra_llave = alfabeto.index(llave[indice_clave].upper())

            valor_resultado = (valor_letra_texto - valor_letra_llave) % len(alfabeto)
            resultado += alfabeto[valor_resultado]

            indice_clave += 1
        else:
            resultado += letra  # Mantener espacios y otros caracteres sin cambios
            indice_clave += 1


    print(f"\nTexto decifrado: {resultado}")
    #return resultado





def mostrar_menu():
    print("Menú:\n")
    print("1. Cifrado del Cesar")
    print("2. Cifrado Polybios")
    print("3. Cifrado Vigenére")
    print("0. Salir")


def sub_menu(titulo):
    limpiar_pantalla()
    opcion=""
    while opcion != "3":
        print(f"CIFRADO {titulo.upper()}\n")

        print("1. Cifrar texto")
        print("2. Decifrar texto")
        print("3. Regresar\n")

        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            cifrar(titulo)
        elif opcion == "2":
            decifrar(titulo)
        elif opcion == "3":
            time.sleep(5)
            print("\n\nRegresando al menu...")
            time.sleep(1)
            break
        else:
            limpiar_pantalla()
            print("Opción no válida.")

    limpiar_pantalla()
    menu() 
           



def menu():
    limpiar_pantalla()
    while True:
        mostrar_menu()
        opcion = input("\n\nSelecciona una opción: ")
        if opcion == "1":
            sub_menu("Cesar")   
        elif opcion == "2":
            opcion2()
        elif opcion == "3":
            sub_menu("Vigenere")
        elif opcion == "4":
            limpiar_pantalla()
            print("\nSaliendo del programa...")
            time.sleep(1)
            break
        else:
            print("\nOpción no válida. Inténtalo de nuevo.")
            limpiar_pantalla()


print("holaaaaaa")

menu()