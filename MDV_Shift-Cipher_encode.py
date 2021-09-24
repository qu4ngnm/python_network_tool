def encrypt():
    plain_text = input("Nhap vao ban ro: ")
    key = input("Nhap vao key : ")
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher_text = ''
    new_ind = 0
    key = int(key)
    for i in plain_text:
        if i.lower() in alphabet:
            new_ind = alphabet.index(i) + key
            cipher_text += alphabet[new_ind%26]
        else:
            cipher_text += i
    print("Ban ma la: " + cipher_text)

