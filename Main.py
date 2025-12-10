from Enigma import Enigma
from Utils import netejar_missatge

ROTORS = ["Rotor1.txt", "Rotor2.txt", "Rotor3.txt"]
ARCHIVO_MENSAJE = "Missatge.txt"
ARCHIVO_XIFRAT = "Xifrat.txt"
ARCHIVO_DESXIFRAT = "Desxifrat.txt"

def mostrar_menu():
    print("\n=== ENIGMA ===")
    print("1. Xifrar")
    print("2. Desxifrar")
    print("3. Sortir")

def obtener_posicion():
    return input("Posició inicial (3 lletres ABC): ").upper()

def xifrar(enigma):
    mensaje = netejar_missatge(input("Missatge per xifrar:\n "))
    with open(ARCHIVO_MENSAJE, "w") as f:
        f.write(mensaje)
    pos = obtener_posicion()
    cifrado, _ = enigma.xifrar_missatge(mensaje, pos)
    with open(ARCHIVO_XIFRAT, "w") as f:
        f.write(cifrado)
    print("Missatge xifrat:\n", cifrado)

def desxifrar(enigma):
    mensaje = "".join(open(ARCHIVO_XIFRAT).read().split())
    pos = obtener_posicion()
    descifrado, _ = enigma.desxifrar_missatge(mensaje, pos)
    with open(ARCHIVO_DESXIFRAT, "w") as f:
        f.write(descifrado)
    print("Missatge desxifrat:\n", descifrado)

def main():
    enigma = Enigma(ROTORS)    
    while True:
        mostrar_menu()
        opcion = input("Opció: ")
        if opcion == "1":
            xifrar(enigma)
        elif opcion == "2":
            desxifrar(enigma)
        elif opcion == "3":
            print("Sortint. Adéu!")
            break
        else:
            print("Opció invàlida!")

