
# içerisine verilen ismi büyük harfle geriye döndürür.
def return_big_name(name):
    return str(name).upper()


isim=return_big_name("veli")
print(isim)

print(abs(-40))
# built-in function
print(round(12.5))

print(int(10.1))
print(str(10.2))

print(min([1,2,45,67,90]))
li=[10,123,32,1,3214,431,2,213,-1]
print(li)
li.sort(reverse=True)
print(li)