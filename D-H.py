class DH_Endpoint(object):
    def __init__(self, public_key1, public_key2, private_key):
        self.public_key1 = public_key1
        self.public_key2 = public_key2
        self.private_key = private_key
        self.full_key = None

    def generate_partial_key(self):
        partial_key = self.public_key1 ** self.private_key
        partial_key = partial_key % self.public_key2
        return partial_key

    def generate_full_key(self, partial_key_r):
        full_key = partial_key_r ** self.private_key
        full_key = full_key % self.public_key2
        self.full_key = full_key
        return full_key

    def encrypt_message(self, message):
        encrypted_message = ""
        key = self.full_key
        for c in message:
            encrypted_message += chr(ord(c) + key)
        return encrypted_message

    def decrypt_message(self, encrypted_message):
        decrypted_message = ""
        key = self.full_key
        for c in encrypted_message:
            decrypted_message += chr(ord(c) - key)
        return decrypted_message


message = "Test message."
a_public = 1234
a_private = 4321
b_public = 4675
b_private = 7837
Alice = DH_Endpoint(a_public, b_public, a_private)
Bob = DH_Endpoint(a_public, b_public, b_private)

a_partial = Alice.generate_partial_key()
b_partial = Bob.generate_partial_key()
a_full = Alice.generate_full_key(b_partial)
b_full = Bob.generate_full_key(a_partial)
print(a_partial, b_partial, a_full, b_full)

b_encrypted = Bob.encrypt_message(message)
a_message = Alice.decrypt_message(b_encrypted)
print(b_encrypted)
print(a_message)
