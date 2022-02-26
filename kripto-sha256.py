from Crypto.Hash import SHA256

# enkripsi
data = b'data ini akan di enkripsi'
hasher = SHA256.new()
hasher.update(data)
result = hasher.hexdigest()
# cetak
print(result)
# karena ini metode hash, jadi kita tidak bisa melakukan dekripsi scr langsung