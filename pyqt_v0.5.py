from PyQt6.QtWidgets import QApplication, QWidget, QTabWidget
from PyQt6 import uic
import sys
from datetime import datetime
from nfc_functions import continuous_tag_detection
from PyQt6.QtCore import QThread, pyqtSignal
from qr_scanner_test import capture_qr_code
import time

# Define the total cups and cups in use
total_cup = 5000
cup_in_use = 2850

today_scanned = 580
today_updated = 35
today_deleted = 420

current_status = "Done!"

current_tag = "125-6829-336-333"
current_cup_so = "12568296"
current_cup_sku = "ED-TIFFNY-YG-25g-L9l16"
current_cup_gem1 = "faceted-2.0CZ"
current_cup_gem2 = "faceted-1.5x3CZ-Mq"
current_cup_set_id = "9233rr3r:33r23t23t3r2t4234gtq34:2fq243f342:33r23t23t3r2t4234gtq34"

previous_tag = "234-993-333-930"
previous_cup_so = "845954565"
previous_cup_sku = "ED-ZIAFACET-RG-25g-L9l16"
previous_cup_gem1 = "faceted-2.0GN-ge"
previous_cup_gem2 = "faceted-1.5x3CZ-Mq"
previous_cup_set_id = "9233rr3r:33r23t23t3r2t4234gtq34:2fq243f342:33r23t23t3r2t4234gtq34"

current_cup_so_2 = "783992872"
current_cup_sku_2 = "RN-SEAM-TI-17g-L3l8"
current_cup_gem1_2 = "cab-2.0TQ"
current_cup_gem2_2 = "faceted-4x2DIA-Mq"
current_cup_set_id_2 = "eawf43wg:33r23t23t3r2t4234gtq34:2fq2asdfaweft23t3r2t4234gtq34"


class NFCScannerThread(QThread):
    tag_detected = pyqtSignal(str)  # Signal to send detected tag to UI

    def run(self):
        """Simulated NFC scanning loop running in the background."""
        last_tag = None
        while True:
            time.sleep(2)  # Simulating NFC tag scanning delay
            tag_id = "TAG123456"  # Simulated tag ID

            if tag_id != last_tag:  # Only emit if tag is new
                last_tag = tag_id
                self.tag_detected.emit(tag_id)  # Send signal to update UI

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('test_05.ui', self)  # Load the UI file
        self.setWindowTitle('Anatometal NFC Registration')

        # Get tab widget
        self.tabWidget = self.findChild(QTabWidget, "tabWidget")
        if self.tabWidget is None:
            print("Error: QTabWidget 'tabWidget' not found in UI!")

        self.scan.setStyleSheet("background-color: #9CD3FF; color: black;")
        self.update.setStyleSheet("background-color: #FEFF9B; color: black;")
        self.delete.setStyleSheet("background-color: #FFA79B; color: black;")
        self.check.setStyleSheet("background-color: #9DFF9F; color: black;")

        # Connect tab change signal to update method
        self.tabWidget.currentChanged.connect(self.init_window)

        # Initialize UI content
        self.init_window(0)  # Load first tab content


    def scan_curr_cup_color(self):
        """Apply styles to the curr_tag element in the scan tab."""
        curr_so = self.findChild(QWidget, "curr_so")  # Adjust QWidget if needed (e.g., QTextEdit)
        if curr_so:
            curr_so.setStyleSheet("background-color: #012C57; color: white;")
        else:
            print("Error: curr_so element not found in scan tab!")

        curr_sku = self.findChild(QWidget, "curr_sku")  # Adjust QWidget if needed (e.g., QTextEdit)
        if curr_sku:
            curr_sku.setStyleSheet("background-color: #012C57; color: white;")
        else:
            print("Error: curr_sku element not found in scan tab!")

        curr_gem1 = self.findChild(QWidget, "curr_gem1")  # Adjust QWidget if needed (e.g., QTextEdit)
        if curr_gem1:
            curr_gem1.setStyleSheet("background-color: #012C57; color: white;")
        else:
            print("Error: curr_gem1 element not found in scan tab!")

        curr_gem2 = self.findChild(QWidget, "curr_gem2")  # Adjust QWidget if needed (e.g., QTextEdit)
        if curr_gem2:
            curr_gem2.setStyleSheet("background-color: #012C57; color: white;")
        else:
            print("Error: curr_gem2 element not found in scan tab!")

        curr_tag_2a = self.findChild(QWidget, "curr_tag_2a")  # Adjust QWidget if needed (e.g., QTextEdit)
        if curr_tag_2a:
            curr_tag_2a.setStyleSheet("background-color: #363101; color: white;")
        else:
            print("Error: curr_tag_2a element not found in scan tab!")

        curr_so_2b = self.findChild(QWidget, "curr_so_2b")  # Adjust QWidget if needed (e.g., QTextEdit)
        if curr_so_2b:
            curr_so_2b.setStyleSheet("background-color: #363101; color: white;")
        else:
            print("Error: curr_so_2b element not found in scan tab!")

        curr_sku_2b = self.findChild(QWidget, "curr_sku_2b")  # Adjust QWidget if needed (e.g., QTextEdit)
        if curr_sku_2b:
            curr_sku_2b.setStyleSheet("background-color: #363101; color: white;")
        else:
            print("Error: curr_sku_2b element not found in scan tab!")

        curr_gem1_2b = self.findChild(QWidget, "curr_gem1_2b")  # Adjust QWidget if needed (e.g., QTextEdit)
        if curr_gem1_2b:
            curr_gem1_2b.setStyleSheet("background-color: #363101; color: white;")
        else:
            print("Error: curr_gem1_2b element not found in scan tab!")

        curr_gem2_2b = self.findChild(QWidget, "curr_gem2_2b")  # Adjust QWidget if needed (e.g., QTextEdit)
        if curr_gem2_2b:
            curr_gem2_2b.setStyleSheet("background-color: #363101; color: white;")
        else:
            print("Error: curr_gem2_2b element not found in scan tab!")

        curr_tag_3a = self.findChild(QWidget, "curr_tag_3a")  # Adjust QWidget if needed (e.g., QTextEdit)
        if curr_tag_3a:
            curr_tag_3a.setStyleSheet("background-color: #360600; color: white;")
        else:
            print("Error: curr_tag_3a element not found in scan tab!")

        curr_so_3b = self.findChild(QWidget, "curr_so_3b")  # Adjust QWidget if needed (e.g., QTextEdit)
        if curr_so_3b:
            curr_so_3b.setStyleSheet("background-color: #360600; color: white;")
        else:
            print("Error: curr_so_3b element not found in scan tab!")

        curr_sku_3b = self.findChild(QWidget, "curr_sku_3b")  # Adjust QWidget if needed (e.g., QTextEdit)
        if curr_sku_3b:
            curr_sku_3b.setStyleSheet("background-color: #360600; color: white;")
        else:
            print("Error: curr_sku_3b element not found in scan tab!")

        curr_gem1_3b = self.findChild(QWidget, "curr_gem1_3b")  # Adjust QWidget if needed (e.g., QTextEdit)
        if curr_gem1_3b:
            curr_gem1_3b.setStyleSheet("background-color: #360600; color: white;")
        else:
            print("Error: curr_gem1_3b element not found in scan tab!")

        curr_gem2_3b = self.findChild(QWidget, "curr_gem2_3b")  # Adjust QWidget if needed (e.g., QTextEdit)
        if curr_gem2_3b:
            curr_gem2_3b.setStyleSheet("background-color: #360600; color: white;")
        else:
            print("Error: curr_gem2_3b element not found in scan tab!")


    def init_window(self, index):

        """Update UI elements based on the selected tab"""
        if index == 0:  # Main Overview
            self.display_current_datetime()

        elif index == 1:  # Today’s Progress
            self.display_current_datetime()

        elif index == 2:  # Current Cup
            self.display_current_datetime()

        elif index == 3:  # Previous Cup
            self.display_current_datetime()

    def update_tab_content(self, tag_id, index):

        """Update UI elements based on the selected tab"""
        if index == 0:  # Main Overview
            self.display_current_datetime()
            self.scan_display_current_cup(tag_id, current_cup_so, current_cup_sku, current_cup_gem1,
                                          current_cup_gem2, current_cup_set_id)

        elif index == 1:  # Today’s Progress
            self.display_current_datetime()
        elif index == 2:  # Current Cup
            self.display_current_datetime()

        elif index == 3:  # Previous Cup
            self.display_current_datetime()

    def display_current_datetime(self):
        """Get the current date and time and display it in self.date."""
        now = datetime.now().strftime("%m/%d/%Y %I:%M %p")  # Format: MM/DD/YYYY HH:MM AM/PM
        self.find_and_set_text("date", now)
        self.find_and_set_text("date_2", now)
        self.find_and_set_text("date_3", now)
        self.find_and_set_text("date_4", now)

    def find_and_set_text(self, widget_name, text):
        """Find a QTextEdit by objectName and set its text."""
        widget = self.findChild(QWidget, widget_name)
        if widget is not None:
            widget.setPlainText(str(text))
        else:
            print(f"Warning: QTextEdit '{widget_name}' not found!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()

    while True:
        # highlight value applied below
        window.scan_curr_cup_color()
        window.show()

        try:
            sys.exit(app.exec())
            # display_text_line(disp, "Scan the cup...", "", "")
            tag_id = continuous_tag_detection()
        except SystemExit:
            print("Closing Window...")
