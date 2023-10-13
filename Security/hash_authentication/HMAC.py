from Crypto.Hash import HMAC, SHA256

#Message
secret=b'Swordfish'

#Create an HMAC object with SHA256 as the digest algorithm
h=HMAC.new(secret, digestmod=SHA256)

#Update the HMAC with the message
h.update(b'Hello')

#Get the hexadecimal output of the HMAC-SHA256
print("HMAC-SHA256 Output:", h.hexdigest())