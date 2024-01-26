max_tries=10
no_guess=0
word="goodmorning"
word=word.lower()


while True:
    k=input("guess letter:")
    if k in word:
        print(word+"contains"+k)
        word=word.replace(k,"")
        print(len(word))
        if(len(word)==0):
            print("you win")
            break
    else:
        print("wrong")
        no_guess=no_guess+1
        if(no_guess>=max_tries):
            print("you loss")
            break

    
