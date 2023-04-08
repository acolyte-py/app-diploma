import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QComboBox, QLineEdit, QFileDialog, QMessageBox
from PyQt5.QtGui import QIntValidator

"""File Creator test app_gui for my infr"""


class FileCreator(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 480, 180)
        self.setWindowTitle('Генератор файлов')
        self.setStyleSheet('background-color: grey')

        self.file_ext_label = QLabel('Расширение файла:', self)
        self.file_ext_label.move(20, 20)

        self.file_ext_combo = QComboBox(self)
        self.file_ext_combo.addItems(['.txt', '.bin', '.zip'])
        self.file_ext_combo.move(140, 20)
        self.file_ext_combo.setStyleSheet("background-color: #D3D3D3;")

        self.file_size_label = QLabel('Размер файла:', self)
        self.file_size_label.move(20, 70)

        self.file_size_input = QLineEdit(self)
        self.file_size_input.move(120, 70)
        self.file_size_input.setValidator(QIntValidator())
        self.file_size_input.setStyleSheet("background-color: #Dн3D3D3;")

        self.file_size_combo = QComboBox(self)
        self.file_size_combo.addItems(['KB', 'MB', 'GB'])
        self.file_size_combo.move(260, 70)
        self.file_size_combo.setStyleSheet("background-color: #D3D3D3;")

        self.create_file_button = QPushButton('Создать файл', self)
        self.create_file_button.move(200, 120)
        self.create_file_button.clicked.connect(self.create_file)
        self.create_file_button.setStyleSheet("background-color: #696969;")

    def create_file(self):
        file_ext = self.file_ext_combo.currentText()
        file_size = int(self.file_size_input.text())
        file_unit = self.file_size_combo.currentText()

        if file_unit == 'KB':
            file_size *= 1024
        elif file_unit == 'MB':
            file_size *= 1024 * 1024
        elif file_unit == 'GB':
            file_size *= 1024 * 1024 * 1024

        save_location, _ = QFileDialog.getSaveFileName(self, 'Сохранить файл', '', f'{file_ext} (*{file_ext})')

        if save_location:
            with open(save_location, 'wb') as f:
                f.write(b'\0' * file_size)

            QMessageBox.information(self, 'Успех', 'Файл успешно создан!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    file_creator = FileCreator()
    file_creator.show()
    sys.exit(app.exec_())
