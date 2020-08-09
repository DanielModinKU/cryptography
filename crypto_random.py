import random 
import numpy as np 

#IMPORTANT: messy, not clean code thrown together quickly. Needs clean up, variables, names etc are a mess. Random experiment to test principles.

#key 
original_key = 10**200
key = original_key

#test string to be encrypted 
s = "this is test information"

#binary placeholder
s_binary  = []

#random data 
rd = []

#randoms seeds
sds = []


#convert to list of binary numbers decoded using unicode scheme (saved as decimal 10 integers)
for ch in s: 
    s_binary.append(ord(ch))
    
#create list of random seeds with key 
for ch in s:
    random.seed(key)
    sds.append(random.randint(0,10**500))
    key = key +1

#generate random data 
for seed in sds: 
    random.seed(seed)
    rd.append(random.randint(0,10**500))

    
#numpy arrays 
np1 = np.array(s_binary)
np2 = np.array(rd)
    
#add to real data 
np3 = np2 + np1 

#print(np3)


#now decrypt data using a given key

given_key = original_key
key_sds = []
decrypted_random_data = []


#first generate the random seeds 
for i in np3: 
    random.seed(given_key)
    key_sds.append(random.randint(0,10**500))
    given_key = given_key +1 
    
    
#now create random data
for seed in key_sds:
    random.seed(seed)
    decrypted_random_data.append(random.randint(0,10**500))
    
#now create original data 
np22 = np.array(decrypted_random_data)

np_decrypted_data = np3 - np22 

#print(np_decrypted_data)

#convert back to text 
np_decrypted_data = np_decrypted_data.tolist() 

#apply conversion from bytes to unicode character encoding 
np_decrypted_data = [chr(item) for item in np_decrypted_data]

#back to text 
final = ''.join(np_decrypted_data)

print(final)


    

    


