def name(greeting, name = "you"):
    name = input("wat is je naam? ")
    return "{}, {}".format(greeting, name)

print(name("hallo", name))

def jaar(bent, age):
    age = input("hoe oud ben je? ")
    return "{}, {}".format(bent, age)

print(jaar("je bent dus", age = "jaar"))
