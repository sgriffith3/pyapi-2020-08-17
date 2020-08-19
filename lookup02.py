#!/usr/bin/env python3
import requests
import argparse


def parze():
  parser = argparse.ArgumentParser(description="Get Brand Info from the fonoapi")
  parser.add_argument("-b", "--brand", required=True, help="Provide the name of the brand you want info about")
  return parser.parse_args()

def main():
  args = parze()
  mytoken = '8c7017832771467f5f66b9d3b7c039bc4ec14ad0fde04412'
  myapi = "https://fonoapi.freshpixl.com/v1/getlatest"
  mybuiltapi = myapi + "?token=" + mytoken
  
  ## ask user for a brand to search on
  #brand = input("What brand of device are you searching for?")
  brand = "&brand=" + args.brand
  
  ## translate our JSON response to a series of Python lists and dictionaries
  myjson = requests.get(mybuiltapi + brand).json()
  
  ## Display a list of what inside our JSON
  for x in myjson:
    print(x)
  
if __name__ == '__main__':
  main()

