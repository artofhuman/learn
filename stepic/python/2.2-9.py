from simplecrypt import decrypt, DecryptionException

with open("passwords.txt") as inp:
    passwords = inp.read().strip().split('\n')

    with open("encrypted.bin", "rb") as inp:
        encrypted = inp.read()

        for pswd in passwords:
            try:
                print(decrypt(pswd, encrypted))
            except(DecryptionException):
                next
