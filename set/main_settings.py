import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Создаем метку QLabel
        label = QLabel("Настройки")

        # Создаем выпадающий список с режимами игры
        game_modes = QComboBox()
        game_modes.addItem("Английский")
        game_modes.addItem("Игры")
        game_modes.addItem("История")
        game_modes.addItem("Рандомно")


        # Создаем кнопку для начала игры
        start_button = QPushButton("Продолжить")

        # Создаем горизонтальный макет для элементов настройки
        settings_layout = QVBoxLayout()
        settings_layout.addWidget(label)
        settings_layout.addWidget(game_modes)
        settings_layout.addWidget(start_button)

        # Создаем главный макет
        main_layout = QVBoxLayout()
        main_layout.addLayout(settings_layout)

        #основной макет для окна
        self.setLayout(main_layout)

        self.setWindowTitle("Настройки игры")
        self.setGeometry(100, 100, 400, 150)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
