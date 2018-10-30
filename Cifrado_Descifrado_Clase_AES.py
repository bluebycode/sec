from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Util import Counter
import base64

class AES_CIPHER:

    BLOCK_SIZE_AES = 16

    def __init__(self, key):
        """Inicializa las variables locales"""
        self.key = key

    def cifrar(self, cadena, IV):
        """Cifra el parametro cadena (de tipo String), y devuelve el texto cifrado binario"""
        datos = cadena.encode("utf-8")
        cipher = AES.new(self.key, AES.MODE_CBC, IV)
        return cipher.encrypt(pad(datos,type(self).BLOCK_SIZE_AES))

    def descifrar(self, datos, IV):
        """Cifra el parametro datos (de tipo binario), y devuelve la cadena en claro de tipo String"""
        cipher = AES.new(self.key, AES.MODE_CBC, IV)
        return unpad(cipher.decrypt(datos), type(self).BLOCK_SIZE_AES).decode("utf-8", "ignore")

key = get_random_bytes(16) # Clave aleatoria de 128 bits
IV = get_random_bytes(16)  # IV aleatorio de 128 bits
datos = "Hola Mundo con AES en modo CBC"
print(datos)
d = AES_CIPHER(key)
cifrado = d.cifrar(datos, IV)
print(cifrado)
descifrado = d.descifrar(cifrado, IV)
print(descifrado)