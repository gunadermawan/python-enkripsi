from Crypto.Cipher import AES

data = b'data ini akan kita enkripsi'
key = b'1n1kunC1116h3h3h' #16 blok kunci

#enkripsi

chiper = AES.new(key, AES.MODE_EAX)
nonce = chiper.nonce
chiperText, tag = chiper.encrypt_and_digest(data)
# cetak

print(chiperText, '\n', tag, '\n', nonce, '\n')

#dekripsi
key = b'1n1kunC1116h3h3h' #16 blok kunci
chiper = AES.new(key, AES.MODE_EAX, nonce)
plaintext = chiper.decrypt(chiperText)
try:
    chiper.verify(tag)
    print(plaintext.decode())
except ValueError:
    print("Kunci anda salah atau terjadi kesalahan olah data")