list=["1","2","5a","10b","abc","10","50"]

for i in list:
    try:
        result=int(i)
        print(result)
    except ValueError:
        continue