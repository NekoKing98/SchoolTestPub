import textwrap
from direct.showbase.ShowBaseGlobal import render2d
from ursina import *
from direct.gui.DirectGui import *
from panda3d.core import TransparencyAttrib, TextNode
from ursina import Ursina
import random

app = Ursina(fullscreen=True, borderless=True)
fnt = loader.loadFont('models/fnt.ttf')
bck = OnscreenImage("models/Image/bck.jpg", parent=render2d)
ani = Animation(name=('models/Animations/Anim1/'), fps=24, loop=True,
                parent=aspect2d,
                scale=(3.5, 2, 1))
ani2 = Animation(name=('models/Animations/Anim2/'), fps=24, loop=False, autoplay=False,
                 parent=aspect2d,
                 scale=(3.5, 2, 1))
ani3 = Animation(name=('models/Animations/Anim3/'), fps=24, loop=False, autoplay=False,
                 parent=aspect2d,
                 scale=(3.5, 2, 1))
ani4 = Animation(name=('models/Animations/Anim4/'), fps=24, loop=False, autoplay=False,
                 parent=aspect2d,
                 scale=(3.5, 2, 1))
ani5 = Animation(name=('models/Animations/Anim5/'), fps=24, loop=False, autoplay=False,
                 parent=aspect2d,
                 scale=(3.5, 2, 1))
ani2.disable()
ani3.disable()
ani4.disable()
ani5.disable()
vlm = 0.5
a = Audio(sound_file_name='models/Audio/fon.mp3', autoplay=False,
          auto_destroy=False, volume=vlm, loop=True)
truAu1 = Audio(sound_file_name=('models/Audio/True/Молодец_правильно.wav'),
               autoplay=False,
               auto_destroy=False, volume=vlm + 1)
truAu2 = Audio(sound_file_name=('models/Audio/True/ИменноТак.wav'),
               autoplay=False,
               auto_destroy=False, volume=vlm + 1)
truAu3 = Audio(sound_file_name=('models/Audio/True/Молодец.wav'),
               autoplay=False,
               auto_destroy=False, volume=vlm + 1)
truAu4 = Audio(sound_file_name=('models/Audio/True/ИСноваВерно.wav'),
               autoplay=False,
               auto_destroy=False, volume=vlm + 1)
falAu1 = Audio(sound_file_name=('models/Audio/False/1.mp3'),
               autoplay=False,
               auto_destroy=False, volume=vlm + 1)
falAu2 = Audio(sound_file_name=('models/Audio/False/2.mp3'),
               autoplay=False,
               auto_destroy=False, volume=vlm + 1)
resAu = Audio(sound_file_name=('models/Audio/rez.mp3'),
              autoplay=False,
              auto_destroy=False, volume=vlm + 1)
trueAu = [truAu1, truAu2, truAu3, truAu4]
falseAu = [falAu1, falAu2]
trueAni = [ani2, ani5]
ani.hide()
bck.hide()
countQst = 0
countWin = 0
countWrg = 0
scoreWrg = 0
scoreWin = 0


class MenuButton(Button):
    def __init__(self):
        super().__init__(disable=False, scale=(.0002, .0001), y=5)
        self.menuStart = Button(text="Начать тест", scale=(.2, .1), y=0.1, on_click=self.startGame)
        self.menuExit = Button(text="Выход", scale=(.2, .1), y=-0.005, on_click=application.quit)

    def startGame(self):
        self.menuStart.disable()
        self.menuExit.disable()
        bck.show()
        ani.show()
        a.play()
        s.show()
        MyApp()

    def input(self, key):
        if key == "escape" and self.menuStart.enabled == False:
            bck.hide()
            self.menuStart.enable()
            self.menuExit.enable()
        if key == "escape" and self.menuStart.enabled == True:
            application.quit()


class Aud(Slider):
    def _update_text(self):
        self.knob.text_entity.text = ''


def vol():
    global vlm
    vlm = s.value
    a.volume = s.value
    truAu1.volume = s.value + 1
    truAu2.volume = s.value + 1
    truAu3.volume = s.value + 1
    truAu4.volume = s.value + 1
    falAu1.volume = s.value + 1
    falAu2.volume = s.value + 1
    resAu.volume = s.value + 1


s = Aud(min=0, max=1, default=0.5, height=Text.size * 2, dynamic=True, radius=Text.size / 2,
        bar_color=color.black66, on_value_changed=vol, vertical=True, x=-.85, y=-.1)
s.knob.text_entity.text = ''
s.hide()
imgIcon = OnscreenImage("models/Image/snd.png", scale=0.03, parent=s, hpr=(0, 0, 90), pos=(0.55, -0.01, 0))
imgIcon.setTransparency(TransparencyAttrib.MAlpha)
MenuButton()


class GameButton:
    def __init__(self):
        self.setAnswer()

    countAnim = 0

    def setAnswer(self):
        x = 0
        y = 0
        if countQst < len(Question.quest):
            self.ans1 = Button(text=textwrap.fill(Question.quest[countQst].get(2), 17), scale=(.5, .1), y=-0.2,
                               x=-0.5, on_click=Func(self.ans, "2"))
            self.ans2 = Button(text=textwrap.fill(Question.quest[countQst].get(3), 17), scale=(.5, .1), y=-0.2,
                               x=0.5, on_click=Func(self.ans, "3"))
            self.ans3 = Button(text=textwrap.fill(Question.quest[countQst].get(4), 17), scale=(.5, .1), y=-0.4,
                               x=-0.5, on_click=Func(self.ans, "4"))
            self.ans4 = Button(text=textwrap.fill(Question.quest[countQst].get(5), 17), scale=(.5, .1), y=-0.4,
                               x=0.5, on_click=Func(self.ans, "5"))
            self.ans1.disable()
            self.ans2.disable()
            self.ans3.disable()
            self.ans4.disable()

            for i in range(0, 60, 5):
                invoke(self.anim1, i * 0.01, i * 0.002, delay=0.05 + i * 0.01)
                invoke(self.anim2, i * 0.01, i * 0.002, delay=0.05 + i * 0.01)
                invoke(self.anim3, i * 0.01, i * 0.002, delay=0.05 + i * 0.01)
                invoke(self.anim4, i * 0.01, i * 0.002, delay=0.05 + i * 0.01)

    def anim1(self, x, y):
        self.ans1.enable()
        self.ans1.scale = (x, y)

    def anim2(self, x, y):
        self.ans2.enable()
        self.ans2.scale = (x, y)

    def anim3(self, x, y):
        self.ans3.enable()
        self.ans3.scale = (x, y)

    def anim4(self, x, y):
        self.ans4.enable()
        self.ans4.scale = (x, y)

    def ans(self, me):
        global countWin
        global scoreWin
        global countWrg
        global countQst
        global scoreWrg
        global ani
        global truAu1
        global truAu2
        global truAu3
        global truAu4
        global falAu1
        global falAu2

        if me == Question.quest[countQst].get(6) and countQst != len(Question.quest) - 1:
            r = random.randint(0, 1)
            countWin += 1
            scoreWin += 1
            countWrg = 0
            ani.__setattr__('loop', False)
            invoke(ani.disable, delay=2)
            if countQst != len(Question.quest) - 1:
                invoke(ani.__setattr__, 'loop', True, delay=2.1)
                trueAni[r].__setattr__('loop', False)
                invoke(trueAni[r].__setattr__, 'loop', True, delay=3)
                if scoreWin > 1:
                    x = random.randint(0, 3)
                    if x == 0 or x == 2:
                        y = 1.5
                    else:
                        y = 1.8
                    invoke(trueAu[x].play, delay=y)
                else:
                    x = random.randint(0, 2)
                    if x == 0 or x == 2:
                        y = 1.5
                    else:
                        y = 1.8
                    invoke(trueAu[x].play, delay=y)

                invoke(trueAni[r].enable, delay=1.95)
                invoke(trueAni[r].start, delay=1.95)
                invoke(trueAni[r].disable, delay=1.94 + trueAni[r].sequence.duration)
                invoke(ani.enable, delay=1.93 + trueAni[r].sequence.duration)

        if me != Question.quest[countQst].get(6) and countQst != len(Question.quest) - 1:
            z = random.randint(0, 3)
            scoreWin = 0
            ani.__setattr__('loop', False)
            invoke(ani.disable, delay=2)
            if countQst != len(Question.quest):
                invoke(ani.__setattr__, 'loop', True, delay=2.1)
                ani3.__setattr__('loop', False)
                invoke(ani3.__setattr__, 'loop', True, delay=3)
                if countWrg < 1:
                    invoke(falAu1.play, delay=1.1)
                if countWrg >= 1:
                    if z == 2 or z == 3:
                        z = 1
                    invoke(falseAu[z].play, delay=1.2)
                invoke(ani3.enable, delay=1.95)
                invoke(ani3.start, delay=1.95)
                invoke(ani3.disable, delay=1.94 + ani3.sequence.duration)
                invoke(ani.enable, delay=1.93 + ani3.sequence.duration)
            countWrg += 1
            scoreWrg += 1

        MyApp.title.hide()
        for i in range(1, 50):
            invoke(self.ans1.__setattr__, 'scale', (.5 - i * 0.008, .1 - i * 0.003), delay=0.05 + i * 0.01)
            invoke(self.ans2.__setattr__, 'scale', (.5 - i * 0.008, .1 - i * 0.003), delay=0.05 + i * 0.01)
            invoke(self.ans3.__setattr__, 'scale', (.5 - i * 0.008, .1 - i * 0.003), delay=0.05 + i * 0.01)
            invoke(self.ans4.__setattr__, 'scale', (.5 - i * 0.008, .1 - i * 0.003), delay=0.05 + i * 0.01)

        invoke(self.ans1.disable, delay=1)
        invoke(self.ans2.disable, delay=1)
        invoke(self.ans3.disable, delay=1)
        invoke(self.ans4.disable, delay=1)

        if countQst == len(Question.quest) - 1:
            if me == Question.quest[countQst].get(6):
                countWin += 1
            else:
                scoreWrg += 1
            MyApp.score.setText(countWin.__str__())
            ani.__setattr__('loop', False)
            invoke(resAu.play, delay=1.95)
            invoke(ani.disable, delay=2)
            invoke(ani4.enable, delay=1.95)
            invoke(ani4.resume, delay=1.95)

            MyApp.title.configure(text="Конец теста.", pos=(-0.3, 0.85), scale=.09)

            image = OnscreenImage('models/Image/sck.jpg', parent=aspect2d, scale=(0.6, 0.3, 0), pos=(-1, 0.3, 0))

            if countWin == 1:
                txtt = 'вопрос'
            elif countWin == 2 or countWin == 3 or countWin == 4:
                txtt = 'вопроса'
            elif countWin == 0 or countWin == 5 or countWin == 6 or countWin == 7 or countWin == 8 or countWin == 9 or countWin == 10:
                txtt = 'вопросов'
            if scoreWrg == 1:
                txtw = 'ошибку'
            elif scoreWrg == 2 or scoreWrg == 3 or scoreWrg == 4:
                txtw = 'ошибки'
            elif scoreWrg == 0 or scoreWrg == 5 or scoreWrg == 6 or scoreWrg == 7 or scoreWrg == 8 or scoreWrg == 9 or scoreWrg == 10:
                txtw = 'ошибок'

            t = Text(f'Ты ответил правильно на {countWin} {txtt}!', scale=1, origin=(1.1, -8))
            t2 = Text(f'Допустил {scoreWrg} {txtw}!', scale=1, origin=(2, -6))
        invoke(self.setAnswer, delay=4)
        invoke(MyApp.title.show, delay=4.25)
        countQst += 1
        Question()


class Question:
    quest = [
        {1: "Что такое IP?", 2: "Интернет протокол", 3: "Уникальный идентификатор", 4: "Интернет порт",
         5: "Маршрутизатор", 6: "2"},
        {1: "Что необходимо для публикации Web- сайта?", 2: "Почтовый адрес пользователя", 3: "URL- адрес",
         4: "Адрес электронной почты пользователя", 5: "Имя пользователя и его пароль", 6: "3"},
        {1: "Модем- это ....", 2: "Почтовая программа", 3: "Сетевой протокол", 4: "Интернет сервер",
         5: "Техническое устройство", 6: "5"},
        {1: "Укажите синоним слова инсталляция.", 2: "Печатающее устройство", 3: "Щелчок", 4: "Установка",
         5: "Хард- диск", 6: "4"},
        {1: "Что происходит при сочетании клавиш Ctrl + X ?", 2: "Копирование текста", 3: "Вставка текста",
         4: "Отмена действия",
         5: "Вырезание текста", 6: "5"},
        {1: "Что происходит при сочетании клавиш Ctrl + Z ?", 2: "Копирование текста", 3: "Вставка текста",
         4: "Отмена действия",
         5: "Вырезание текста", 6: "4"},
        {1: "Что происходит при сочетании клавиш Alt + F4 ?", 2: "Сохранение игры", 3: "Включение чита",
         4: "Закрытие активного окна",
         5: "Закрытие пассивного окна", 6: "4"},
        {1: "Какая комбинация клавиш используется для быстрого перехода между открытыми окнами?", 2: "Alt + F1",
         3: "Alt + Caps Lock",
         4: "Alt + ~",
         5: "Alt + Tab", 6: "5"},
        {1: "Что означает файл с расширением .png?", 2: "Архив",
         3: "Изображение",
         4: "Исполняемый файл",
         5: "Текстовый файл", 6: "3"},
        {1: "Что означает файл с расширением .7z?", 2: "Архив",
         3: "Изображение",
         4: "Исполняемый файл",
         5: "Текстовый файл", 6: "2"},
    ]

    def __init__(self):
        if countQst == 0:
            MyApp.title.setText("1. " + self.quest[countQst].get(1))
        if countQst < len(self.quest):
            MyApp.title.setText((countQst + 1).__str__() + ". " + self.quest[countQst].get(1))
            MyApp.score.setText(countWin.__str__())


class MyApp:
    title = OnscreenText(
        align=TextNode.A_left, font=fnt, wordwrap=16,
        style=1, fg=(1, 1, 1, 1), pos=(-0.5, 0.85), scale=.07)
    score = OnscreenText(
        align=TextNode.A_left, font=fnt,
        style=1, fg=(1, 1, 1, 1), pos=(1.2, 0.85), scale=.07)

    def __init__(self):
        GameButton()
        Question()
