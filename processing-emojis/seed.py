import urllib.request as r
from bs4 import BeautifulSoup
import csv
import os

EMOJI_URL = "https://unicode.org/emoji/charts/full-emoji-list.html"
EMOJI_HTML_FILE = "data.txt"
EMOJI_166_FILE = "smile.csv"

def read_and_write_smile():
  try:
    if (os.stat(f"./{EMOJI_166_FILE}").st_size == 0):
      print('vacio')
      # read html in data.txt
      html_doc = open(EMOJI_HTML_FILE, "r")
      soup = BeautifulSoup(html_doc, "html.parser")
      rows = soup.find_all("tr")
      emoji_array = []
      for row in rows:
        values = row.find_all(class_=["rchars", "code", "chars"])
        if len(values) < 3:
          continue
        index = values[0].string
        unicode = values[1].string
        emoji = values[2].string
        emoji_array.append([index, unicode, emoji])  
        if index == "166":
          break
      # save smile emojis in smile.csv
      smile_doc = open(EMOJI_166_FILE, "w", newline="")
      writer = csv.writer(smile_doc)
      writer.writerows(emoji_array)
      # close files
      smile_doc.close()
      html_doc.close()
  except Exception as e:
    print(e.args)

def request_and_write():
  try: 
    # if file is empty, request and fill it
    if (os.stat(f"./{EMOJI_HTML_FILE}").st_size == 0):
      # req emoji url
      data = r.urlopen(EMOJI_URL).read().decode()
      soup = BeautifulSoup(data, features="html.parser")
      # write html in file
      data_file = open(EMOJI_HTML_FILE, "w")
      data_file.write(str(soup))
  except Exception as e:
    print(e.args)
  
def main():
  request_and_write()
  read_and_write_smile()

if __name__ == "__main__":
  main()
