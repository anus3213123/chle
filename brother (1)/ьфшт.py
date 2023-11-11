from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from PIL import Image, ImageFilter

class ImageProcessingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('Редактор')
        self.setStyleSheet("background-color: black;")

        self.select_button = QPushButton('Выберите изображение', self)
        self.select_button.clicked.connect(self.select_image)
        self.select_button.setGeometry(10, 10, 180, 30)
        self.select_button.setStyleSheet("background-color: green;")

        self.bw_button = QPushButton('ЧБ', self)
        self.bw_button.clicked.connect(self.convert_to_bw)
        self.bw_button.setGeometry(200, 10, 100, 30)
        self.bw_button.setStyleSheet("background-color: red;")

        self.mirror_button = QPushButton('Отразить', self)
        self.mirror_button.clicked.connect(self.mirror_image)
        self.mirror_button.setGeometry(310, 10, 80, 30)
        self.mirror_button.setStyleSheet("background-color: red;")

        self.wtfisthat_button = QPushButton('Непонятный эффект', self)
        self.wtfisthat_button.clicked.connect(self.wtfisthat)
        self.wtfisthat_button.setGeometry(10, 50, 140, 30)
        self.wtfisthat_button.setStyleSheet("background-color: red;")

        self.blur_button = QPushButton('Блюр', self)
        self.blur_button.clicked.connect(self.blur_image)
        self.blur_button.setGeometry(160, 50, 100, 30)
        self.blur_button.setStyleSheet("background-color: red;")

        self.lasos_button = QPushButton('Перевёртышь', self)
        self.lasos_button.clicked.connect(self.lasos)
        self.lasos_button.setGeometry(270, 50, 100, 30)
        self.lasos_button.setStyleSheet("background-color: red;")

        self.save_button = QPushButton('Сохранить', self)
        self.save_button.clicked.connect(self.save_image)
        self.save_button.setGeometry(10, 90, 100, 30)
        self.save_button.setStyleSheet("background-color: green;")

        self.image_path = None
        self.processed_image = None

    def select_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Выберите изображение', '', 'Images(*.jpg *.png);; All Files(*)', options=options)
        if file_path:
            self.image_path = file_path
            self.processed_image = None  
        else:
            print('Вы отменили выбор файла')

    def convert_to_bw(self):
        if self.image_path:
            with Image.open(self.image_path) as img:
                bw_image = img.convert('L')
                self.processed_image = bw_image
                bw_image.show()
        else:
            print('Сначала выберите изображение')

    def mirror_image(self):
        if self.image_path:
            with Image.open(self.image_path) as img:
                mirrored_image = img.transpose(Image.FLIP_LEFT_RIGHT)
                self.processed_image = mirrored_image
                mirrored_image.show()
        else:
            print('Сначала выберите изображение')

    def wtfisthat(self):
        if self.image_path:
            with Image.open(self.image_path) as img:
                img_gray = img.convert("L")
                edges = img_gray.filter(ImageFilter.FIND_EDGES)
                self.processed_image = edges
                edges.show()
        else:
            print('Сначала выберите изображение')

    def blur_image(self):
        if self.image_path:
            with Image.open(self.image_path) as img:
                blur_im = img.filter(ImageFilter.BLUR)
                self.processed_image = blur_im
                blur_im.show()
        else:
            print('Сначала выберите изображение')
    
    def lasos(self):
        if self.image_path:
            with Image.open(self.image_path) as img:
                converted_img = img.transpose(Image.FLIP_TOP_BOTTOM)
                self.processed_image = converted_img
                converted_img.show()
        else:
            print('Сначала выберите изображение')

    def save_image(self):
        if self.processed_image:
            save_path, _ = QFileDialog.getSaveFileName(self, 'Сохранить изображение', 'fcki9f1le', 'Images(*.jpg *.png)')
            if save_path:
                self.processed_image.save(save_path)
        else:
            print('Сначала обработайте изображение и выберите, что сохранить.')

def main():
    app = QApplication([])
    window = ImageProcessingApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
