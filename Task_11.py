def common_letters():
    s1 = ("house")
    s2 = ("computers")
    print("The common letters are: ")
    a = list (set(s1) & set(s2))
    for i in a:
         print (i)

common_letters()         