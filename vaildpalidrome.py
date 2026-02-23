def vaildplandrome(alpha):

    
    right = 0
    lift = len(alpha) - 1

    while right < lift:
        if alpha[right] != alpha[lift]:
            return False
        right +=1
        lift -=1
    return True

print(vaildplandrome("abcdcba"))              