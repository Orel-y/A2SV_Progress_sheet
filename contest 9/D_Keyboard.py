tc = int(input())
for _ in range(tc):
    s = input()
    st = list(s)
    st.sort()
    counter = {}
    unique_ar = []
    res = ""

    for ch in st:
        counter[ch] = counter.get(ch, 0) + 1
        
        if ch in counter:
            unique_ar.append(ch)

    for key, value in counter.items():
        if value % 2 == 1:
            res += key

    
    print(res)