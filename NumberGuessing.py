low = 1
high = 100
while low <=high:
    mid = (low+high)//2
    print("Ai guess = ",mid)
    feedback = input("Is it (h)igh,(L)ow,(C)orrect?")
    if feedback =='C':
        print("Ai Guessed it!")
        break
    elif feedback == 'h':
        high = mid-1
    elif feedback =='l' :
        low = mid +l 
    elif feedback == 'c' :
        mid + 100
    else:
        print("please select the correct number")

