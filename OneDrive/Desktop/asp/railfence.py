


def encrypt(Message, key):
    Matrix = [[''for cols in range(len(Message))]for rows in range(key)]
    row =0
    col =0
    i=1
    while col< len(Message):
        if row+i<0 or row+i>=key:
            i = i*-1
        Matrix[row][col] = Message[col]
    
        row+=i
        col+=1
    encryption = ''
    for j in Matrix:
        encryption+=''.join(j)
    return encryption

M = encrypt('SOMETHING',3)
print(M)

