#client
from Crypto.Cipher import DES3
from hashlib import md5
import socket
s = socket.socket()         # Create a socket object
host = "localhost"          # Get local machine name
port = 7890                 # Reserve a port for your service.
s.connect((host, port))
print("Client got connected to the server")
while True:
    Decrypted_image = 'decrypted_image.png'

    key = input('Enter Unique key same as Server for 3DES key: ')
    hash_key = md5(key.encode('ascii')).digest()
    triple_des_key = DES3.adjust_key_parity(hash_key)
    cipher = DES3.new(triple_des_key, DES3.MODE_EAX, nonce=b'0')

    with open(Decrypted_image, 'wb') as f:
        new_file_bytes=s.recv(10000)
        f.write(new_file_bytes)
        print("opened")
        print("cipher text:",new_file_bytes)
    with open(Decrypted_image,'rb') as f:
        Binary_file=f.read()
        print("Image received and ready for Decryption")
        Decrypted_bytes = cipher.decrypt(Binary_file)
        print("Image is Decrypted Successfully..")

    with open(Decrypted_image, 'wb') as output_file:
        output_file.write(Decrypted_bytes)
        print('Operation Done!')
        break
s.close()
print("connection closed")

