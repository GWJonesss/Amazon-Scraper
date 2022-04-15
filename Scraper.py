# libraries
import os
from turtle import width
import urllib.request
from bs4 import BeautifulSoup
import csv
from tkinter import *
import tkinter
from PIL import ImageTk, Image
from tkinter import ttk

# Put your URL here
url = ''
# Fetching the html
request = urllib.request.Request(url)
content = urllib.request.urlopen(request)
# Parsing the html 
parse = BeautifulSoup(content, 'html.parser')
# Provide html elements' attributes to extract the data 
text1 = parse.find_all('a', attrs={'class': 'a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style'})
text2 = parse.find_all('span', attrs={'class': 'a-size-medium a-color-base a-text-normal'})
# Writing extracted data in a csv file
with open('index.csv', 'a') as csv_file:
  writer = csv.writer(csv_file,  quoting=csv.QUOTE_ALL)
  
  for col1,col2 in zip(text1, text2):
    writer.writerow([col1.get_text().strip(), col2.get_text().strip()])



#frame = tkinter.Tk()
#bg = ImageTk.PhotoImage(Image.open("im1.jpg"))


#canvas = Canvas()
#canvas.pack(fill = "both", expand = True)
#canvas.create_image( 0, 0, image = bg,
                     #anchor = "center")

#frame.mainloop()