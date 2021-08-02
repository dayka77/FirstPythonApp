from tkinter import *


# boutton deuxieme page

def open_second_page():
    open(file='main.py')


window = Tk()
# paramètre window

window.geometry('720x480')
window.config(background="black")
window.title('AlphaProject BETA')
window.iconbitmap('img/logo.ico')
window.minsize(480, 360)

# component

label_title = Label(window, text="Alpha Project", font=("Arial", 80), background="black", fg="white")
label_title.pack(expand=YES)

# button

bouton_test = Button(window, text="test", font=("arial", 40), command=open_second_page)
bouton_test.pack()
# menu nav

menu_nav = Menu(window)

file_menu = Menu(menu_nav, tearoff=0)
file_menu.add_command(label="Quitter", command=window.quit)
menu_nav.add_cascade(label="Fichier", menu=file_menu)

# config pour afficher le menu dans la window

window.config(menu=menu_nav)

# afficher la fenetre
print("Démarré avec succès")
window.mainloop()
