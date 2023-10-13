import random
import string

l=list(string.ascii_lowercase)
random.shuffle(l)
result=''.join(l)
print('Alphabet Shuffle: '+result)

randC=random.choice(string.ascii_lowercase)
print('Random Letter Alphabet:', randC)

randE=random.sample([3, 0, -1 , 4.2, 55], 2)
print('Two random elements from [3, 0, -1 , 4.2, 55]: ', randE)

randI=random.randint(1, 10)
print('Integer random number from 1 to 10:', randI)


