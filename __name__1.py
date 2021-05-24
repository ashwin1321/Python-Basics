from typing import Mapping

                            #########                  if __name__ == __main__                 ##########


def printh(string):
    return f"This is a string {string}"

def add(n,m):
    return n+m

print(" the name is ", __name__)                            # for this program the __name__ is __main__
# if we import this file in other, the __name__ is the name of this file eg: (__name1__)

if __name__ == '__main__':                                  # this particular program in this only executes in this whole program,
# if we import this file and run , this doesnot executes in that program

    print(printh('abcd'))

    a = add(2,3)
    print(a)
