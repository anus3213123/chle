import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QComboBox, QPushButton, QRadioButton
import pyglet   
import time

class Option1Window(QWidget):
    def __init__(self):
        super().__init__()

        label = QLabel("Папич")
        papa1 = QRadioButton("Топ 10")
        papa2 = QRadioButton("Легкая")
        papa3 = QRadioButton("Быть нищем в реале")
        papa4 = QRadioButton("синку зачекай")
        back_button = QPushButton("Назад")
        back_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(papa1)
        layout.addWidget(papa2)
        layout.addWidget(papa3)
        layout.addWidget(papa4)
        layout.addWidget(back_button)

        self.setLayout(layout)
        self.setWindowTitle("Окно для Папич")
        def top1():
            mus = pyglet.media.load("ja-samyj-adekvatnyj-v-mire.mp3")
            mus.play()
            

        def top2():
            mus = pyglet.media.load("pap.mp3")
            mus.play()
            
            
            
        def top3():
            mus = pyglet.media.load("real.mp3")
            mus.play()
            
        def top4():
            mus = pyglet.media.load("son.mp3")
            mus.play()
            
            
        
            

        papa1.clicked.connect(top1)
        papa2.clicked.connect(top2)
        papa3.clicked.connect(top3)
        papa4.clicked.connect(top4)

           

class Option2Window(QWidget):
    def __init__(self):
        super().__init__()

        label = QLabel("Это окно для Дота")
        d1 = QRadioButton("12 танго")
        d2 = QRadioButton("встань мид")
        d3 = QRadioButton("БАУНТИ ХАНТЕР")
        d4 = QRadioButton("Серега пират матерится на китайском")
        back_button = QPushButton("Назад")
        back_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(d1)
        layout.addWidget(d2)
        layout.addWidget(d3)
        layout.addWidget(d4)
        layout.addWidget(back_button)

        def top1():
            mus = pyglet.media.load("12.mp3")
            mus.play()
            

        def top2():
            mus = pyglet.media.load("stand.mp3")
            mus.play()
            
            
            
        def top3():
            mus = pyglet.media.load("bounty.mp3")
            mus.play()
            
        def top4():
            mus = pyglet.media.load("sergay.mp3")
            mus.play()
            
            
        
            

        d1.clicked.connect(top1)
        d2.clicked.connect(top2)
        d3.clicked.connect(top3)
        d4.clicked.connect(top4)

        self.setLayout(layout)
        self.setWindowTitle("Срота")

class Option3Window(QWidget):
    def __init__(self):
        super().__init__()

        label = QLabel("Это окно для Стендоффчик")
        st1 = QRadioButton("Стендоффчик")
        st2 = QRadioButton("Голда не на балике")
        back_button = QPushButton("Назад")
        back_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(st1)
        layout.addWidget(st2)
        layout.addWidget(back_button)

        def a1():
            mus = pyglet.media.load("standoff.mp3")
            mus.play()
            

        def a2():
            mus = pyglet.media.load("gold.mp3")
            mus.play()         
            
        
            

        st1.clicked.connect(a1)
        st2.clicked.connect(a2)

        self.setLayout(layout)
        self.setWindowTitle("Стендоффчик")

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        label = QLabel("soundpad")

        self.game_modes = QComboBox()
        self.game_modes.addItem("Папич")
        self.game_modes.addItem("Дота")
        self.game_modes.addItem("Стендоффчик")

        start_button = QPushButton("Продолжить")
        start_button.clicked.connect(self.show_selected_option_window)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.game_modes)
        layout.addWidget(start_button)

        self.setLayout(layout)
        self.setWindowTitle("Настройки игры")
        self.setGeometry(100, 100, 400, 150)

    def show_selected_option_window(self):
        selected_option = self.game_modes.currentText()
        if selected_option == "Папич":
            self.option1_window = Option1Window()
            self.option1_window.show()
        elif selected_option == "Дота":
            self.option2_window = Option2Window()
            self.option2_window.show()
        elif selected_option == "Стендоффчик":
            self.option3_window = Option3Window()
            self.option3_window.show()
count = 0






if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
