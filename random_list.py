#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jlegind
#
# Created:     12-07-2013
# Copyright:   (c) jlegind 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import random

def main():
    ran_list = ["one", "two", "three", "four", "five"]
    while ran_list:
        ran_item = random.choice(ran_list)
        print ran_item
        ran_list.remove(ran_item)


if __name__ == '__main__':
    main()
