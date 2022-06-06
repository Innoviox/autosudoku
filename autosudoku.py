from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from string import ascii_uppercase, digits

import time
import cv2
import pytesseract
import base64

from PIL import Image

def traverse():
    for i in range(9):
        for j in range(9):
            yield (i, j)

difficulty = "facile"

driver = webdriver.Chrome(executable_path='/Users/simonchervenak/Desktop/chromedriver')

driver.set_page_load_timeout(10)
try:
    driver.get(f"https://sudoku.com/fr/{difficulty}/")
except:
    pass # hehe

# get board
canvas = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[3]/div[6]/canvas')

# https://stackoverflow.com/questions/38316402/how-to-save-a-canvas-as-png-in-selenium
canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)
canvas_png = base64.b64decode(canvas_base64)
with open(r"canvas.png", 'wb') as f:
    f.write(canvas_png)

img = cv2.imread('canvas.png')

size = 110
custom_config = r'--oem 3 --psm 6'

board = [['' for _ in range(9)] for _ in range(9)]

for i, j in iterate():
    cropped_image = img[i*size:(i+1)*size, j*size:(j+1)*size][20:100, 20:100]

    s = pytesseract.image_to_string(cropped_image, config=custom_config)

    c = input(s + '? ')
    if c.strip():
        s = c.strip()
    board[i][j] = s

for i, j in 
