from Crypto.Cipher import Blowfish
from struct import pack

key = b'KunciIniSangatRahasia'
data = b'data ini akan kita enkripsi'

bs = Blowfish.block_size
chiper = Blowfish.new(key, Blowfish.MODE_CBC)

plen = bs - len(data) % bs
padding = [plen] * plen
padding = pack('b' * plen, * padding)
msg = chiper.iv + chiper.encrypt(data + padding)
# cetak
print(msg)