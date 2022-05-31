import pyautogui as pag
import time

ppl = input("Enter number of members:")
msg = input("Enter msg:")
time.sleep(10)

i = 0
n = 0

pag.typewrite(msg)

while i< int(ppl):
    pag.typewrite("@")
    
    for n in range(0,i):
        pag.press('Down')
        n+=1
    
    pag.press('Enter')
    i+=1

pag.press('Enter')
