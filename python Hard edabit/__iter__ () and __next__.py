def sentence_searcher(txt):
    

    a=txt.split()
    c = a.__iter__()
    return (c.__next__())


txt = "I have a cat. I have a mat. Things are going swell."

print(sentence_searcher(txt))



# I




mylist = iter(["apple", "banana", "cherry"])
x = next(mylist, "orange")
print(x)
	
#apple	