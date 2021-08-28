#function as an object
def hello(sound):
    return sound.upper()

v = hello
print(v("hi"))

#function as an argument
def shout(sound):
    return sound.lower()

def greet(func):
    j = func("I am passed as an argument")
    print(j)

greet(shout)

def check(x):
    def adde(y):
        return (x+y)
    return adde

d = check(15)
print(d(10))