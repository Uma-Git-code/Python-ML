def emoji_convertor(msg):    
    words = msg.split(" ")
    emoji ={
        "happy" : "😊",
        "sad" : "😒",
        "good" : "👍",
    }
    outmsg = ""
    for word in words:
        outmsg = outmsg + emoji.get(word, word) + " "
    return outmsg

in1 = input(">>>")
out1 = emoji_convertor(in1)
print(out1)