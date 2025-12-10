import re
ALFABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def netejar_missatge(text):
    limpio = ""
    for c in text:
        if 'A' <= c <= 'Z':
            limpio += c
    return limpio

def llegir_fitxer_rotor(fitxer):
    if not os.path.exists(fitxer):
        with open(fitxer, 'w') as f:
            f.write(ALFABET + "\nZ\n")
        return ALFABET, 'Z'

    with open(fitxer, 'r') as f:
        linies = []
        for l in f:
            linies.append(l.strip())

        cablejat = linies[0] if len(linies) > 0 else ALFABET
        notch = linies[1] if len(linies) > 1 else 'Z'
        return cablejat, notch

def escriure_fitxer_rotor(fitxer, cablejat, notch):
    try:
        with open(fitxer,'w') as f:
            f.write(cablejat + "\n" + notch + "\n")
        return True
    except:
        return False
