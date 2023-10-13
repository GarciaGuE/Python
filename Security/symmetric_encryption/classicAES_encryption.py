import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

data=b"secret"
data+=b" word"
key=get_random_bytes(16)
cipher=AES.new(key, AES.MODE_CBC)
ct_bytes=cipher.encrypt(pad(data, AES.block_size))

# A random cipher.iv has been generated.
# cipher.iv and ct_bytes are of type 'bytes'.
# We can store ct_bytes and cipher.iv in any way we want.
# In this example, we'll use the JSON format.
# However, JSON doesn't support bytes, only strings.
# b64encode() encodes to Base64, and from there to str there is no issue.
# If we don't convert to Base64 first, it could cause problems in JSON.
iv=b64encode(cipher.iv).decode('utf-8')
ct=b64encode(ct_bytes).decode('utf-8')
result={}
result["iv"]=iv
result["ciphertext"]=ct
print(result)
print("key = {}".format(key.hex()))
with open('data.json', 'w') as outfile:
    json.dump(result, outfile)
print("bye.")