import pyautogui
from time import sleep
pyautogui.PAUSE = 0.7 #PONDO INTERVALO DE TEMPO A CADA AÇÃO DO PYAUTOGUI
pyautogui.alert('Programa iniciando, tire suas mãos do mouse e teclado...')
print('-----Botando o musicão em qualquer navegador-----')
navegador = int(input(''' [1] - Mozilla Firefox
 [2] - Microsoft Edge
 [3] - Opera
 [4] - Opera GX
 [5] - Google Chrome
 Digite o navegador que você deseja utilizar: '''))
if navegador == 1:
    #Entrando no Firefox e entrando no youtube
    pyautogui.press('winleft')
    pyautogui.write('Firefox')
    pyautogui.press('enter')
    sleep(1)
    pyautogui.write('https://www.youtube.com')
    sleep(1)
    pyautogui.press('enter')
elif navegador == 2:
    #Entrando no Edge e entrando no youtube
    pyautogui.press('winleft')
    pyautogui.write('Edge')
    pyautogui.press('enter')
    sleep(1)
    pyautogui.write('https://www.youtube.com')
    sleep(1)
    pyautogui.press('enter')
elif navegador == 3:
    #Entrando no Opera e entrando no youtube
    pyautogui.press('winleft')
    pyautogui.write('Opera')
    pyautogui.press('enter')
    sleep(1)
    pyautogui.write('https://www.youtube.com')
    sleep(1)
    pyautogui.press('enter')
elif navegador == 4:
    #Entrando no Opera GX e entrando no youtube
    pyautogui.press('winleft')
    pyautogui.write('Opera GX')
    pyautogui.press('enter')
    sleep(1)
    pyautogui.write('https://www.youtube.com')
    sleep(1)
    pyautogui.press('enter')
elif navegador == 5:
    #Entrando no Chrome e entrando no youtube
    pyautogui.press('winleft')
    pyautogui.write('Chrome')
    pyautogui.press('enter')
    sleep(1)
    pyautogui.write('https://www.youtube.com')
    sleep(1)
    pyautogui.press('enter')
