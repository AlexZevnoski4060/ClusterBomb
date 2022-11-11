#!/usr/local/bin/python3.11
import os
import sys
import argparse
from multiprocessing import Process

parser = argparse.ArgumentParser()

parser.add_argument("-t", "--target", help="Target IP or hostname")
parser.add_argument("-fd", "--ffufDirectory", help="ffuf output directory")
parser.add_argument("-gd", "--gobusterDomain", help="gobuster output directory")

args = parser.parse_args()



def brute_force_directory(target):
  wordlist = "~/Desktop/OST/Wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt"
  threads = 20
  
  if args.ffufDirectory:
    #os.system(f"ffuf -t {threads} -timeout 15 -ac -fc '429,403,404' -D -e 'asp,aspx,pl,php,html,htm,jsp,cgi' -u {target}/FUZZ -w {wordlist} -o {args.ffufDirectory}")
    os.system(f"ffuf -t {threads} -u http://{target}/FUZZ -w {wordlist} -fc '403,302,429,404'")
    
  else:
    print("You forgot to specify the output file")
    
    

def brute_force_domain(target):
  wordlist = "~/Desktop/OST/Wordlists/SecLists/Discovery/DNS/subdomains-top1million-110000.txt"

  if args.gobusterDomain:
    os.system(f"gobuster dns -d {target} -w {wordlist} -o {args.gobusterDomain}")



def main():
  # brute_force_directory(args.target)
  # brute_force_domain(args.target)
  p1 = Process(target=brute_force_directory, args=(args.target,))
  p2 = Process(target=brute_force_domain, args=(args.target,))
  
  p1.start()
  p2.start()
  
  p1.join()
  p2.join()



if __name__ == "__main__":
  main()
  sys.exit(0)