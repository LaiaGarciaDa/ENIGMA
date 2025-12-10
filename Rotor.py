ALFABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def crear_rotor(cablejat, notch, pos_inicial='A'):
    cablejat_invers_llista = [''] * 26
    for i in range(26):
        char_out = cablejat[i]
        idx = 0
        for j in range(26):
            if ALFABET[j] == char_out:
                idx = j
                break

        cablejat_invers_llista[idx] = ALFABET[i]

    cablejat_invers = "".join(cablejat_invers_llista)
    lletra = pos_inicial.upper()
    posicio = 0
    for i in range(26):
        if ALFABET[i] == lletra:
            posicio = i
            break

    return {
        "cablejat": cablejat,
        "cablejat_invers": cablejat_invers,
        "notch": notch.upper(),
        "pos": posicio
    }

    
def girar(rotor):
    lletra_abans = ALFABET[rotor["pos"]]
    rotor["pos"] = (rotor["pos"] + 1) % 26
    return lletra_abans == rotor["notch"]

def set_posicio_inicial(rotor, lletra):
    lletra = lletra.upper()
    pos = 0
    for i in range(26):
        if ALFABET[i] == lletra:
            pos = i
            break
    rotor["pos"] = pos

def mapeig(rotor, char_in, invers=False):
    index_in = 0
    for i in range(26):
        if ALFABET[i] == char_in:
            index_in = i
            break
    shifted_in = (index_in + rotor["pos"]) % 26
    if invers:
        buscar = ALFABET[shifted_in]
        index_out_wiring = 0
        for i in range(26):
            if rotor["cablejat_invers"][i] == buscar:
                index_out_wiring = i
                break
    else:
        buscar = rotor["cablejat"][shifted_in]
        index_out_wiring = 0
        for i in range(26):
            if ALFABET[i] == buscar:
                index_out_wiring = i
                break

    index_out = (index_out_wiring - rotor["pos"]) % 26
    return ALFABET[index_out]


def passar_endavant(rotor, char):
    return mapeig(rotor, char, invers=False)

def passar_endarrere(rotor, char):
    return mapeig(rotor, char, invers=True)
