#project by: Daniel A. dos Santos 

#operation choice
MODE_ENCRYPT = 1
MODE_DECRYPT = 0
#do the encryption 
def caesar(text, key, mode):
    alphabet = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ1234567890!@#$%*' + ' '
    new_data = ''
    for i in text: 
        index = alphabet.find(i)
        if index == -1: 
            new_data += i
        else:
            new_index = index + key if mode == MODE_ENCRYPT else index - key 
            new_index = new_index % len(alphabet) 
            new_data += alphabet[new_index:new_index+1]
    return new_data
#processing results
key = 7
answer = input("Process a message? Y-yes or N-no \n")
while ((answer == 'Y') or (answer == 'y')): 
    mode = input(" 1 - Encrypt \n 0 - Decrypt \n")
    original = input("Message to be processed: ")
    ciphered = caesar(original, key, MODE_ENCRYPT)
    plain = caesar(original, key, MODE_DECRYPT)
    if mode == '1':
        print(' Message encrypted:', ciphered)
    else:
        print(' Message dencrypted:', plain)
    answer = input("Process a new message? Y-yes or N-no \n")
    if ((answer == 'n') or (answer == 'N')): 
        print ("\n Goodbye! \n ")
        break