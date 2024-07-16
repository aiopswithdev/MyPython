import random

# print("------------Encoding-------------")

def s_enc(msg):
        y, w = [], []
        l_msg = [x for x in msg]
        alp= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789*&%$#@!"
        if len(l_msg)<3:
            y = l_msg[::-1]
            for el in y:
                print(el, end="")
            return ("")
        else:
            l = l_msg[0]
            l_msg.append(l)
            l_msg.remove(l_msg[0])
            for i in range(3):
                l_msg.append(random.choice(alp))
                l_msg.insert(i, random.choice(alp))
            w = l_msg
            for el in w:
                print(el, end="")
            return ("")
def b_enc(msg):
        l1 = msg.split()
        for k in range(len(l1)):
            print(s_enc(l1[k]), end=" ")

# print("------------Decoding-------------")

def s_dec(msg):

    l_msg = [x for x in msg]
    if len(l_msg)<3 and len(l_msg)!=0:
        z = l_msg[::-1]
        for el1 in z:
            print(el1, end="")
        return ""

    if len(l_msg)>3:
        b_g, b_h, b_i = l_msg[0], l_msg[1], l_msg[2]
        l_msg.remove(b_g)
        l_msg.remove(b_h)
        l_msg.remove(b_i)
        for j in range(3):
            l_msg.pop(-1)
        a = l_msg[-1]
        l_msg.pop(-1)
        l_msg.insert(0, a)
        for el1 in l_msg:
            print(el1, end="")
        return ""
def b_dec(msg):
     l2 = msg.split()
     for k1 in range(len(l2)):
          print(s_dec(l2[k1]), end=" ")

while True:
    msg = input("\nEnter your message to encode/decode: ")
    while True:
        user = input("Type 'enc' for Encode, 'dec' for Decode: ")
        if user!="enc" and user!="dec":
            print("Please enter a valid input")
            continue
        else:
            break
    if user.lower()=="enc":
        if msg.split()==1:
            print("\nEncoded Message: ")
            s_enc(msg)
        else:
            print("\nEncoded Message: ")
            b_enc(msg)
    else:
        if msg.split()==1:
            print("\nDecoded Message: ")
            s_dec(msg)
        else:
            print("\nDecoded Message: ")
            b_dec(msg)
    while True:
        user1 = input("\n\nDo you wish to continue? 'y' for Yes, 'n' for No: ")
        if user1!="y" and user1!="n":
            print("Please enter a valid input")
            continue
        else:
            break
    if user1.lower()=="y":
        continue
    elif user1.lower()=="n":
        break
print("\nThanks for using us!")