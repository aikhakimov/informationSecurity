class RSA_Endpoint(object):
    def __init__(self, p, q, e):
        self.open_key_n = p * q
        self.open_key_e = e
        phi = (p - 1) * (q - 1)
        d = 10
        while (d * e) % phi != 1:
            d += 1
        self.closed_key_d = d

    def encrypt_message(self, message, e, n):
        return (message ** e) % n

    def decrypt_message(self, encrypted_message):
        decrypted_message = encrypted_message ** self.closed_key_d % self.open_key_n
        return decrypted_message


message = 12345
p = 3557
q = 2579
e = 17
Alice = RSA_Endpoint(p, q, e)
Bob = RSA_Endpoint(p, q, e)


b_encrypted = Bob.encrypt_message(message, Alice.open_key_e, Alice.open_key_n)
a_message = Alice.decrypt_message(b_encrypted)
print(b_encrypted)
print(a_message)
