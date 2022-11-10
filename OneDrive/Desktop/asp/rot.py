plaintext = input("enter the text : ")
abc = "abcdefghijklmnopqrstuvwxyz"
encrypt = "".join([abc[(abc.find(c)+13)%26] for c in plaintext])
decrypt = "".join([abc[(abc.find(c)+13)%26] for c in encrypt])
print("Encrypted text is : "+encrypt)
print("original text is : "+ decrypt)
