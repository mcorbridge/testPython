import sys


print("---------------------------------------------------------------")

x = 9

def goop():
    global x
    x = x + 9
    print(x)


goop()

# python closure
def foo():

  counter = 1

  def bar():
    nonlocal counter
    counter += 1


  return bar

bar = foo()
bar()
bar()
bar()


# recursive function
def outer(arg):
    print("outer " + str(arg))
    if arg >= 10:
        sys.exit()
    else:
        print("inner " + str(arg))
        arg = arg + 1
        outer(arg)
    return


outer(0)


