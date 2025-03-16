from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic
import sys

class MyApp(QWidget):  # Change QWidget
    def __init__(self):
        super().__init__()
        uic.loadUi('test_02.ui', self)  # Load the UI file
        self.setWindowTitle('Anatometal NFC Registeration')
        self.button.clicked.connect(self.sayHello)


    def sayHello(self):
        inputText = self.input.text()
        self.output.setText('Hello {0}'.format(inputText))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    try:
        sys.exit(app.exec())
    except SystemExit:
        print("Closing Window...")