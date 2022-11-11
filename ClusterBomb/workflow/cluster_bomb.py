#!/usr/local/bin/python3.11
import os
import sys
import argparse
from multiprocessing import Process


parser = argparse.ArgumentParser()

parser.add_argument("-t", "--target", help="Target IP or hostname")
parser.add_argument("-nd", "--nmapDirectory", help="nmap output directory")
parser.add_argument("-fd", "--ffufDirectory", help="ffuf output directory")
parser.add_argument("-gd", "--gobusterDirectory", help="gobuster output directory")

args = parser.parse_args()



def brute_force_directory(target):
  wordlist = "~/Desktop/OST/Wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt"
  threads = 20
  
  if args.ffufDirectory:
    os.system(f"ffuf -t {threads} -timeout 15 -ac -fc '429,403,404' -D -e 'asp,aspx,pl,php,html,htm,jsp,cgi' {target}/FUZZ -w {wordlist} -o {args.ffufDirectory}")
    
  else:
    print("You forgot to specify the output file")

  

def brute_force_domain(target):
  wordlist = "~/Desktop/OST/Wordlists/SecLists/Discovery/DNS/subdomains-top1million-110000.txt"

  if args.gobusterDirectory(target):
    os.system(f"gobuster dns -d {target} -w {wordlist} -o {args.gobusterDirectory}")



def scan_port(target):
  try:
    os.system(f"nmap -sC -sV -p- --min-rate=10000 {target} -oN {args.nmapDirectory}")
  except:
    if os.getuid() != 0:
      print("You have to run this program under root permission")
    


def main():
  p1 = Process(target=brute_force_directory, args=(args.target,))
  p2 = Process(target=brute_force_domain, args=(args.target,))
  p3 = Process(target=scan_port, args=(args.target,))

  p1.start()
  p2.star()
  p3.start()
  
  p1.join()
  p2.join()
  p3.join()



if __name__ == "__main__":
  main()
  sys.exit(0)