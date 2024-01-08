import math
import random

# Function to convert to 256 bits
def convertTo256Bits(key):
    res = key.to_bytes((key.bit_length() + 7) // 8, byteorder='big')
    if len(res) < 32:
        res = b'\x00' * (32 - len(res)) + res
    elif len(res) > 32:
        res = res[-32:]
    return res

if __name__ == "__main__":
    p = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844980366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
    g = 2
    # --- Diffie-Hellman ---
    private1 = random.randint(2, p - 2)
    private2 = random.randint(2, p - 2)
    
    print(f"Randomly generated private key 1: {private1}")
    print(f"Randomly generated private key 2: {private2}")

    # Public keys
    public1 = pow(g, private1, p)
    public2 = pow(g, private2, p)
    # Shared secret
    shared1 = pow(public2, private1, p)
    shared2 = pow(public1, private2, p)
    convertTo256Bits(shared1)
    convertTo256Bits(shared2)

    print("\nShared 1 hex: ", convertTo256Bits(shared1).hex())
    print("Shared 1 decimal: ", int(convertTo256Bits(shared1).hex(), 16))
    print("Shared 2 hex: ", convertTo256Bits(shared2).hex())
    print("Shared 2 decimal: ", int(convertTo256Bits(shared2).hex(), 16))
