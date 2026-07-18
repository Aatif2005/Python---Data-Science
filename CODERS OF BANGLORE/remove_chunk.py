with open("initialdata.txt", encoding='utf-8') as f:
    data = f.read()
    #print(data)
chunks = data.split("\n\n")
print(chunks[1])