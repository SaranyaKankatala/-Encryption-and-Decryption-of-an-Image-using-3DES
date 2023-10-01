#server
from Crypto.Cipher import DES3
from hashlib import md5
import socket

port = 7890                  # Reserve a port for your service.
s = socket.socket()          # Create a socket object
host = "localhost"           # Get local machine name
s.bind((host, port))         # Bind to the port
s.listen(4)                  # Now wait for client connection.

print ("Server is waiting for client connection.........")
conn, addr = s.accept()     # Establish connection with client.
print ('Got connection from', addr)
key = input(' Enter Unique 3DES key: ')
hash_key = md5(key.encode('ascii')).digest()
triple_des_key = DES3.adjust_key_parity(hash_key)
cipher = DES3.new(triple_des_key, DES3.MODE_EAX, nonce=b'0')
Original_image= 'original_image.jpg'
encrypted_image='encrypted image.png'
with open(Original_image, 'rb')as f:
       file_bytes = f.read()
       print("original text:",file_bytes)
       new_file_bytes = cipher.encrypt(file_bytes)
       print("Encryption of original image is done..!!")
       conn.send(new_file_bytes)
       print("Encrypted image is sent securely to the client")
       print("cipher text:",new_file_bytes)
       conn.close()
with open(encrypted_image,'wb')as f:
       f.write(new_file_bytes)
print("Connection Closed...!!")
