import hashlib
import sha3
import bitstring

def hashIt(bytetext,hex=False):

    s = hashlib.sha3_256()
    s.update(bytetext)
    if hex:
        return s.hexdigest()
    else:
        return s.digest()

    empty = b''
    emptyAnswer = 'a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a'
    
    short = b'abc'
    shortAnswer = '3a985da74fe225b2045c172d6bd390bd855f086e3e9d525b46bfe24511431532'
    
    medium = b'abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq'
    mediumAnswer = '41c0dba2a9d6240849100376a8235e2c82e1b9998a999e21db32dd97496d3376'
    
    large = b'abcdefghbcdefghicdefghijdefghijkefghijklfghijklmghijklmnhijklmnoijklmnopjklmnopqklmnopqrlmnopqrsmnopqrstnopqrstu'
    largeAnswer = '916f6061fe879741ca6469b43971dfdb28b1a32dc36cb3254e812be27aad1d18'
    
    print("\nEmpty string:")
    
    print(hashIt(empty,True))
    print(emptyAnswer)
    
    print("\nShort string:")
    
    print(hashIt(short,True))
    print(shortAnswer)
    
    print("\nMedium string:")
    
    print(hashIt(medium,True))
    print(mediumAnswer)
    
    print("\nLarge string:")
    
    print(hashIt(large,True))
    print(largeAnswer)
    