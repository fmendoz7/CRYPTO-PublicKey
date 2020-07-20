"""
    ASSUMPTIONS
        - Alice and Bob agree upon
            > Prime module (n)
            > Base generator (g)

    METHOD
        - Alice has private key: a. Bob has private key: b
        - Alice calculates public key: g^a * mod (n)
        - Bob calculates public key: g^b * mod (n)
        - Alice calculates shared key: (g^b * mod (n))^a * mod (n)
        - Bob calculates shared key: (g^a * mod (n))^b * mod (n)
        - (g^b)^a == (g^a)^b
"""

# PROGRAMMER: Francis Mendoza

# REMEMBER: Randomness is critical for strong cryptography
import random 

mod = random.getrandbits(512) #specified as our prime number
g = 6

print("PUBLIC INFORMATION: " )
print("MOD", mod)
print("BASE GENERATOR: ", g)
print("--------------------------------------------------------")

alicePrivate = random.getrandbits(512)
alicePublic = pow(g, alicePrivate, mod) # pow(base, exponent, modulus)
print("ALICE PUBLIC: ", alicePublic)

bobPrivate = random.getrandbits(512)
bobPublic = pow(g, bobPrivate, mod)
print("BOB PUBLIC: ", bobPublic)
print("--------------------------------------------------------")

aliceShared = pow(bbobPublic, alicePrivate, mod)
bobShared = pow(aalicePublic, bobPrivate, mod)

print(" >> ALICE SHARED: ", aliceShared)
print(" >> BOB SHARED: ", bobShared)
print("--------------------------------------------------------")

message = "Cao Cao was the King Of Wei"

from Crypto.Cipher import AES

