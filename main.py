from guizero import App, Text, PushButton, Box, Picture, info
from random import randint
cuaso = App(title = "tro choi di tim gian diep", width = 580, height = 600)
chu = Text(cuaso, text = "truy tim gian diep")
box = Box(cuaso, layout = "grid")

hang = randint(0, 2)
cot = randint(0, 2)
def bamnut(h, c, n):
    global hang, cot
    if h == hang and c == cot:
        info("thong bao", "ban da tim thay gian diep!")
        n.text = ""
        n.image = "giandiep.png"
    else:
        info("thong bao", "sai roi, hay tim noi khac nao!")
for i in range(3):
    for j in range(3):
        button = PushButton(box, text = "?", grid = [i, j], width = 20, height = 10, command = bamnut, args = [i, j, None])
        button.update_command(bamnut, [i, j, button])
cuaso.display()
