from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

#memulai enkripsi
key = b'1n1kunc1' #8 block size
data = b'ini akan kita enkripsi'
BLOCK_SIZE = 32

des = DES.new(key, DES.MODE_ECB)
padded_text = pad(data, BLOCK_SIZE)
encrypt = des.encrypt(padded_text)

# cetak
print(encrypt)

# dekripsi
key = b'1n1kunc1' #8 block size
des = DES.new(key, DES.MODE_ECB)
decrypt = des.decrypt(encrypt)
# cetak
print(decrypt)