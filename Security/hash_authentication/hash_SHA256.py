from Crypto.Hash import SHA256

#Object creation
hash_object=SHA256.new(data=b'First')

#Update with new data
hash_object.update(b'Second')
hash_object.update(b'Third')

#Equivalent to the previous updates
#hash_object.update(b'SecondThird')

#Get bytes of the hash value
print("Hash code:", hash_object.digest())

#Hexadecimal representation of the hash value
print("SHA256 Output:", hash_object.hexdigest())

#Size of the hash value in bytes and block size
print("Hash size:", hash_object.digest_size)
print("Block size:", hash_object.block_size)