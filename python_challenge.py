text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"

str1 = "abcdefghijklmnopqrstuvwxyz"
str2 = "cdefghijklmnopqrstuvwxyzab"
table = text.maketrans(str1, str2)
print(table)

print("maketrans and translate method:", text.translate(table))


# Challenge 2
  #first attempt - the long way

code = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def translator(words):
  new_list = []
  for letter in words:
    if letter == " ":
      new_list.append(" ")
    if letter == "a":
      new_list.append("c")
    if letter == "b":
      new_list.append("d")
    if letter == "c":
      new_list.append("e")
    if letter == "d":
      new_list.append("f")
    if letter == "e":
      new_list.append("g")
    if letter == "f":
      new_list.append("h")
    if letter == "g":
      new_list.append("i")
    if letter == "h":
      new_list.append("j")
    if letter == "i":
      new_list.append("k")
    if letter == "j":
      new_list.append("l")
    if letter == "k":
      new_list.append("m")
    if letter == "l":
      new_list.append("n")
    if letter == "m":
      new_list.append("o")
    if letter == "n":
      new_list.append("p")
    if letter == "o":
      new_list.append("q")
    if letter == "p":
      new_list.append("r")
    if letter == "q":
      new_list.append("s")
    if letter == "r":
      new_list.append("t")
    if letter == "s":
      new_list.append("u")
    if letter == "t":
      new_list.append("v")
    if letter == "u":
      new_list.append("w")
    if letter == "v":
      new_list.append("x")
    if letter == "w":
      new_list.append("y")
    if letter == "x":
      new_list.append("z")
    if letter == "y":
      new_list.append("a")
    if letter == "z":
      new_list.append("b")
  print(('').join(new_list))

translator(code)
