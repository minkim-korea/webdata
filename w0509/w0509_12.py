import requests
from bs4 import BeautifulSoup
import csv

with open("w0509/join02_info_input.html","r",encoding="utf8") as f :
    soup = BeautifulSoup(f,"lxml")
    
