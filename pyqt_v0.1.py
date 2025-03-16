import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt6.QtGui import QIcon
from PyQt6 import uic

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('test_01.ui', self)
        # self.setWindowTitle('NFC Register App')
        # # self.setWindowIcon(QIcon('map.co'))
        # self.resize(500,350)
        #
        # layout = QVBoxLayout()
        # self.setLayout(layout)
        #
        # # Widgets
        # self.inputField = QLineEdit()
        # button = QPushButton()
        # self.output = QTextEdit()
        #
        # layout.addWidget(self.inputField)
        # layout.addWidget(button)
        # layout.addWidget(self.output)

if __name__ == '__main__':

    # app = QApplication([])
    app = QApplication(sys.argv)

    window = MyApp()
    window.show()

    try:
        sys.exit(app.exec())
    except:
        print('Closing Window...')


