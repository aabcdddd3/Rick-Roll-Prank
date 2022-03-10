from selenium import webdriver
import pyttsx3

driverroll = webdriver.Chrome(executable_path="") # <-- Enter the location of your webdriver and don't forget to add double backslashes.
speakroll = pyttsx3.init()
driverroll.minimize_window()
print("This is a prank made by Shubu909 and he's the respective owner of this file and coded this.")
speakroll.say("This is a prank made by francisco neto and he's the respective owner of this file and coded this.")
speakroll.runAndWait()
speakroll.say("BOMBA!")
driverroll.maximize_window()
driverroll.minimize_window()
driverroll.fullscreen_window()
driverroll.minimize_window()
driverroll.get("https://www.youtube.com/watch?v=enoiKZuvXk8")
element = driverroll.find_element_by_xpath("//*[@id='movie_player']/div[29]/div[2]/div[1]/button").click()
speakroll.say("Devagarinho até embaixo, embaixo, embaixo Devagarinho até em cima, em cima, em cima Devagarinho até embaixo, embaixo, embaixo Devagarinho até em cima, em cima, em cima Sensual, o movimento é sensual Sensual, o movimento é bem sexy Sexy, o movimento é bem sexy Sexy, já tá chegando o Bragaboys com essa dança que é uma Bomba, para dançar isso aqui é bomba Pra balançar isso aqui é bomba E a mulherada se joga bomba E os marmanjos dançando é bomba Tudo que a rádio já toca é bomba E na boate já rola bomba Toda galera já dança bomba Por isso pega na cintura e acaba acaba acaba acaba acaba logo E acaba, acaba, acaba acaba, acaba logo E acaba acaba acaba acaba acaba logo")
speakroll.runAndWait()
speakroll.say("fuck you")
speakroll.runAndWait()
print("Thanks for using the bomba Prank now it's ended so your free!")
speakroll.say("Thanks for using the bomba Prank now it's ended so your free!")
speakroll.runAndWait()
