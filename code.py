def caesar(word, rotat, typo):
    result=''
    for letter in word:
        if typo == 'decode':            
            letter = chr(ord(letter) - rotat)
                        
        else :
            letter = chr(ord(letter) + rotat)

        result += letter

    return result 

end= True
while end:
    command = input('type encode or decode ')
    word = input('give word ')
    rotat= int(input('rotation '))

    if command == 'encode' :
        print(caesar(word, rotat, command))

    elif command=='decode':
        print(caesar(word, rotat, command))
    else : print('unknown to me ! ')

    ans = input('>> yes > or < no << ')
    if ans == 'no':
        end = False
        print('thanks for using')
