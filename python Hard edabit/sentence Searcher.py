def sentence_searcher(txt,word):
    txt = txt.split(".")
    for i in txt:
        if word.lower() in i.lower():
            return "{}".format(i)
    
txt = "I have a cat. I have a mat. Things are going swell."
print(sentence_searcher(txt,"have"))

#I have a cat

def using_lambda(text,sentence):
    lst = ([i for i in txt.split(".") if (word.lower()) in i.lower()])
    return ''	if not lst else lst[0].strip()+'.'


text = "I have a cat. I have a mat. Things are going swell."
print(sentence_searcher(text,"have"))
