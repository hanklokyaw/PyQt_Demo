from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic
import sys


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('test_02.ui', self)  # Load the UI file
        self.setWindowTitle('Anatometal NFC Registration')

        # Ensure self.output exists before using it
        if not hasattr(self, "output") or self.output is None:
            print("Error: QTextEdit with objectName 'output' not found!")

    def keyPressEvent(self, event):
        """ Capture key presses and display them in the output box. """
        key = event.text()  # Get the key that was pressed
        if key:
            current_text = self.output.toPlainText()  # Get existing text
            self.output.setPlainText(current_text + key)  # Append the new key


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    try:
        sys.exit(app.exec())
    except SystemExit:
        print("Closing Window...")
