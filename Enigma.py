from Utils import netejar_missatge, formatar_sortida

def crear_rotor(cablejat, notch):
    return {"cablejat": cablejat, "pos": 0, "notch": notch}

def avancar_rotors(rotors):
    rotors[0]["pos"] = (rotors[0]["pos"] + 1) % 26
    if rotors[0]["pos"] == (ord(rotors[0]["notch"]) - 65):
        rotors[1]["pos"] = (rotors[1]["pos"] + 1) % 26
        if rotors[1]["pos"] == (ord(rotors[1]["notch"]) - 65):
            rotors[2]["pos"] = (rotors[2]["pos"] + 1) % 26



def set_posicio_inicial(rotors, pos):
    for i in range(3):
        rotors[i]["pos"] = ord(pos[i].upper()) - 65

def xifrar_missatge(rotors, missatge, pos):
    set_posicio_inicial(rotors, pos)
    missatge = netejar_missatge(missatge)
    resultat = ""
    for lletra in missatge:
        avancar_rotors(rotors)
        char = lletra
        char = pasar_endavant(rotors[0], char)
        char = pasar_endavant(rotors[1], char)
        char = pasar_endavant(rotors[2], char)
        resultat += char
    return resultat

def desxifrar_missatge(rotors, missatge, pos):
    set_posicio_inicial(rotors, pos)
    missatge = netejar_missatge(missatge)
    resultat = ""
    for lletra in missatge:
        avancar_rotors(rotors)
        char = lletra
        char = pasar_endarrere(rotors[2], char)
        char = pasar_endarrere(rotors[1], char)
        char = pasar_endarrere(rotors[0], char)
        resultat += char
    return formatar_sortida(resultat, grups_de_cinc=False), resultat