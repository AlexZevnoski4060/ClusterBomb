#!/usr/local/bin/python3.11
import os
import sys
import argparse



parser = argparse.ArgumentParser()

parser.add_argument("-t", "--target", help="Target IP or hostname")
parser.add_argument("-nd", "--nmapDirectory", help="nmap output directory")

args = parser.parse_args()



def scan_port(target):
  try:
    os.system(f"nmap -sC -sV -p- --min-rate=10000 {target} -oN {args.nmapDirectory}")
  except:
    if os.getuid() != 0:
      print("You have to run this program under root permission")



def main():
  scan_port(args.target)



if __name__ == "__main__":
  main()
  sys.exit(0)