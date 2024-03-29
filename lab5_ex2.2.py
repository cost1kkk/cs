import random

def betaGenerator(p, g, publicKey):
    betaG = pow(g, publicKey, p)
    return betaG

def encrypt_elgamal(decimalList, g, betaG, p):
    k = random.randint(2, p - 2)
    r = pow(g, k, p)
    encryptedMessage = []

    for i in range(len(decimalList)):
        t = pow(betaG, k, p)
        t = (t * decimalList[i]) % p
        encryptedMessage.append(t)
    return r, encryptedMessage

def decrypt_elgamal(t, r, publicKey, p):
    r = pow(r, -publicKey, p)
    decryptedMessage = []

    for i in range(len(t)):
        decryptedMessage.append((r * t[i]) % p)
    return decryptedMessage

if __name__ == "__main__":
    p = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
    g = 2

    # Baxanean Constantin in decimal from the previous exercise
    decimalResult = 1480340038230756872041454103038037098971294062

    # --- ElGamal ---
    k = random.randint(1, p - 2)
    publicKey = pow(g, k, p)
    betaGeneratorValue = betaGenerator(p, g, publicKey)
    print ("\n Results for : Baxanean Constantin")
    print("Decimal message: ", decimalResult)
    r, t = encrypt_elgamal([decimalResult], g, betaGeneratorValue, p)
    print("Encrypted message: ", r, t[0])
    decryptedText = decrypt_elgamal([t[0]], r, publicKey, p)
    print("Decrypted decimal message:", decryptedText)
