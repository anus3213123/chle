from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox
from random import randint
import sys
import pyglet
app = QApplication([])


#Создание главного окна
screen = QWidget()
screen.setWindowTitle('Викторина')

screen.move(800, 300)
screen.resize(400, 400)

#Создание виджетов

qs = QLabel('Когда был разработан автомат Калашникова?')

btn_1 = QRadioButton('1942')
btn_2 = QRadioButton('1939')
btn_3 = QRadioButton('1947')
btn_4 = QRadioButton('1945')

#Расстановка виджетов

main_container = QVBoxLayout()
l1 = QHBoxLayout()
l2 = QHBoxLayout()
l3 = QHBoxLayout()

l1.addWidget(qs, alignment= Qt.AlignCenter)

l2.addWidget(btn_1, alignment= Qt.AlignCenter)
l2.addWidget(btn_2, alignment= Qt.AlignCenter)

l3.addWidget(btn_3, alignment= Qt.AlignCenter)
l3.addWidget(btn_4, alignment= Qt.AlignCenter)

main_container.addLayout(l1)
main_container.addLayout(l2)
main_container.addLayout(l3)

screen.setLayout(main_container)

#Функция генерации победителя
count = 0
def yes():
    screen_win = QMessageBox()
    screen_win.setText('Ты угадал')
    screen_win.exec_()
def no():
    global count
    print(count)
    screen_lose = QMessageBox()
    screen_lose.setText('Ты не угадал')
    screen_lose.exec_()
    count+=1
    if count >=2:
        sys.exit()



btn_1.clicked.connect(no)
btn_2.clicked.connect(no)
btn_4.clicked.connect(no)
btn_3.clicked.connect(yes)



#Отображения нашего приложения

screen.show()
app.exec_()


