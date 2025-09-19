#SORTING ARRAY BASED ON STR SIZE
arr = ["alice", "james","john","doe"]


#ordenar por length of word
arr.sort(key=lambda x: len(x))
print(arr)


arr.sort(key=lambda x: x[0] == "j", reverse=True) #pone primero a los que empiezan con j
print(arr)
