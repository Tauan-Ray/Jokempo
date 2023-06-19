from tkinter import *
from PIL import Image, ImageTk
from os import getlogin
from random import choice

# Cores
white = '#FFFFFF'
black = '#404040'
draw = "#fff873"
lose = "#e85151"
win = "#34eb3d"

# Configurando janela
app = Tk()
app.title('Jokempo')
app.geometry('300x340')
app.config(bg=white)
app.resizable(False, False)

# Preparando icones
iconRock = Image.open('images/rock.png')
iconRock = ImageTk.PhotoImage(iconRock)

iconPaper = Image.open('images/paper.png')
iconPaper = ImageTk.PhotoImage(iconPaper)

iconScissor = Image.open('images/scissor.png')
iconScissor = ImageTk.PhotoImage(iconScissor)

# Criando frames
scoreboard = Frame(app, width=300, height=120, bg=black, relief='raised')
scoreboard.pack()

game = Frame(app, width=300, height=230, bg=white, relief='flat')
game.pack()

# Configurando Placar
username = Label(scoreboard, text=getlogin(), height=1,
                 anchor='center', font=('Ivy 12 bold'), bg=black, fg=white)
username.place(x=20, y=75)

pointUser = Label(scoreboard, text='0', height=1,
                  anchor='center', font=('Ivy 30 bold'), bg=black, fg=white)
pointUser.place(x=50, y=20)

separe = Label(scoreboard, text=':', height=1, anchor='center',
               font=('Ivy 30 bold'), bg=black, fg=white)
separe.place(x=139, y=20)

lineUser = Label(scoreboard, height=10, anchor='center',
                 font=('Ivy 10 bold'), bg=white)
lineUser.place(x=0, y=0)

userPc = Label(scoreboard, text='PC', height=1, anchor='center',
               font=('Ivy 12 bold'), bg=black, fg=white)
userPc.place(x=200, y=75)

pointPc = Label(scoreboard, text='0', height=1, anchor='center',
                font=('Ivy 30 bold'), bg=black, fg=white)
pointPc.place(x=230, y=20)

linePc = Label(scoreboard, height=10, anchor='center',
               font=('Ivy 10 bold'), bg=white)
linePc.place(x=295, y=0)

choicePc = Label(game, text='', height=1, anchor='center',
                 font=('Ivy 10 bold'), bg=white, fg=white)
choicePc.place(x=190, y=10)

lineDraw = Label(scoreboard, text='', width=294,
                 anchor='center', font=('Ivy 1 bold'), bg=white)
lineDraw.place(x=0, y=115)

# Declarando variaveis globais
global user
global pc
global rounds
global pointsUser
global pointsPc

pointsUser = 0
pointsPc = 0
rounds = 0

# Configurando parte interativa
def play(i):
    global rounds
    global pointsUser
    global pointsPc

    if rounds < 5:
        options = ['Pedra', 'Papel', 'Tesoura']
        user = i
        pc = choice(options)
        choicePc['text'] = pc
        choicePc['fg'] = black

        # Caso de empate
        if user == 'Pedra' and pc == 'Pedra':
            linePc['bg'] = white
            lineUser['bg'] = white
            lineDraw['bg'] = draw

        elif user == 'Papel' and pc == 'Papel':
            linePc['bg'] = white
            lineUser['bg'] = white
            lineDraw['bg'] = draw

        elif user == 'Tesoura' and pc == 'Tesoura':
            linePc['bg'] = white
            lineUser['bg'] = white
            lineDraw['bg'] = draw

        # Caso ganhe
        elif user == 'Pedra' and pc == 'Tesoura':
            linePc['bg'] = white
            lineUser['bg'] = win
            lineDraw['bg'] = white
            pointsUser += 10

        elif user == 'Papel' and pc == 'Pedra':
            linePc['bg'] = white
            lineUser['bg'] = win
            lineDraw['bg'] = white
            pointsUser += 10

        elif user == 'Tesoura' and pc == 'Papel':
            linePc['bg'] = white
            lineUser['bg'] = win
            lineDraw['bg'] = white
            pointsUser += 10

        # Caso perca
        elif user == 'Tesoura' and pc == 'Pedra':
            linePc['bg'] = win
            lineUser['bg'] = white
            lineDraw['bg'] = white
            pointsPc += 10

        elif user == 'Pedra' and pc == 'Papel':
            linePc['bg'] = win
            lineUser['bg'] = white
            lineDraw['bg'] = white
            pointsPc += 10

        elif user == 'Papel' and pc == 'Tesoura':
            linePc['bg'] = win
            lineUser['bg'] = white
            lineDraw['bg'] = white
            pointsPc += 10

        # Atualizando os pontos e as rodadas
        pointUser['text'] = pointsUser
        pointPc['text'] = pointsPc
        rounds += 1

    else:
        endgame()

# Função para inicar o jogo
def start():
    global rock_button
    global paper_button
    global scissor_button

    play_button.destroy()

    # Botões das opções de jogadas
    rock_button = Button(game, command=lambda: play('Pedra'), image=iconRock, width=50,
                         height=50, compound=CENTER, anchor=CENTER, bg=white, relief=FLAT, overrelief=SUNKEN)
    rock_button.place(x=10, y=40)

    paper_button = Button(game, command=lambda: play('Papel'), image=iconPaper, width=50,
                          height=50, compound=CENTER, anchor=CENTER, bg=white, relief=FLAT, overrelief=SUNKEN)
    paper_button.place(x=125, y=40)

    scissor_button = Button(game, command=lambda: play('Tesoura'), image=iconScissor, width=50,
                            height=50, compound=CENTER, anchor=CENTER, bg=white, relief=FLAT, overrelief=SUNKEN)
    scissor_button.place(x=240, y=40)

# Função de quando o jogo termina
def endgame():
    global rounds
    global pointsPc
    global pointsUser

    # Reniciando as variaveis
    rounds = 0
    pointsPc = 0
    pointsUser = 0

    # Apagando os botões
    rock_button.destroy()
    paper_button.destroy()
    scissor_button.destroy()

    # Vendo pontuações
    playerUser = int(pointUser['text'])
    playerPc = int(pointPc['text'])

    # Verificando vencedor
    if playerUser > playerPc:
        result = Label(game, text=f'Parabéns {getlogin()}, você ganhou!!!!',
                       height=1, anchor='center', font=('Ivy 10 bold'), bg=white, fg=win)
        result.place(x=10, y=60)

    elif playerUser < playerPc:
        result = Label(game, text='O PC ganhou :(', height=1,
                       anchor='center', font=('Ivy 10 bold'), bg=white, fg=lose)
        result.place(x=10, y=60)

    else:
        result = Label(game, text='Foi empate', height=1,
                       anchor='center', font=('Ivy 10 bold'), bg=white, fg=draw)
        result.place(x=10, y=60)

    # Função para reniciar o jogo
    def restart():
        result.destroy()
        restart_button.destroy()
        choicePc.destroy()
        lineDraw['bg'] = white
        lineUser['bg'] = white
        linePc['bg'] = white

        pointPc['text'] = '0'
        pointUser['text'] = '0'
        start()

    restart_button = Button(game, command=restart, text='Jogar novamente?', width=34, height=1,
                            padx=5, anchor='center', font=('Ivy 10'), bg=black, fg=white, relief=RAISED, overrelief=SUNKEN)
    restart_button.place(x=5, y=189)


# Botão para começar a jogar
play_button = Button(game, command=start, text='Jogar', width=34, height=1, padx=5,
                     anchor='center', font=('Ivy 10'), bg=black, fg=white, relief=RAISED, overrelief=SUNKEN)
play_button.place(x=5, y=189)


app.mainloop()
