from collections import Counter

def checkInclusion( s1: str, s2: str) -> bool:
    n1=len(s1)
    n2=len(s2)

    if n1 > n2:
        return False

    need = Counter(s1)
    window = Counter(s2[:n1])

    if need == window:
        return True

    left  = 0
    for right  in range(n1,n2):
        window[s2[right]] += 1
        window[s2[left]]  -= 1

        if window[s2[left]] ==0:
            del window[s2[left]]

        left +=1   
            if need == window:
            return True
    return False

print(checkInclusion("ab","eibaoui"))
        