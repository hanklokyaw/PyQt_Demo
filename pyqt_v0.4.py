from PyQt6.QtWidgets import QApplication, QWidget, QTabWidget
from PyQt6 import uic
import sys
from datetime import datetime

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
        self.tabWidget.currentChanged.connect(self.update_tab_content)

        # Initialize UI content
        self.update_tab_content(0)  # Load first tab content

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


    def update_tab_content(self, index):
        """Update UI elements based on the selected tab"""
        if index == 0:  # Main Overview
            self.display_current_datetime()
            self.display_total_cup(total_cup, cup_in_use)
            self.display_today_progress(today_scanned, today_updated, today_deleted)
            self.scan_display_current_cup(current_tag, current_cup_so, current_cup_sku, current_cup_gem1,
                                          current_cup_gem2, current_cup_set_id)
            self.scan_display_previous_cup(previous_tag, previous_cup_so, previous_cup_sku, previous_cup_gem1,
                                           previous_cup_gem2, previous_cup_set_id)

        elif index == 1:  # Today’s Progress
            self.display_current_datetime()
            self.update_display_current_cup(current_tag, current_status, current_cup_so, current_cup_so_2,
                                            current_cup_sku, current_cup_sku_2, current_cup_gem1, current_cup_gem1_2,
                                            current_cup_gem2, current_cup_gem2_2, current_cup_set_id, current_cup_set_id_2)
        elif index == 2:  # Current Cup
            self.display_current_datetime()
            self.complete_display_current_cup(current_tag, current_status, current_cup_so, current_cup_so_2,
                                            current_cup_sku, current_cup_sku_2, current_cup_gem1, current_cup_gem1_2,
                                            current_cup_gem2, current_cup_gem2_2, current_cup_set_id, current_cup_set_id_2)

        elif index == 3:  # Previous Cup
            self.display_current_datetime()
            self.check_display_current_cup(current_tag, current_cup_so, current_cup_sku, current_cup_gem1,
                                          current_cup_gem2, current_cup_set_id)

    def display_current_datetime(self):
        """Get the current date and time and display it in self.date."""
        now = datetime.now().strftime("%m/%d/%Y %I:%M %p")  # Format: MM/DD/YYYY HH:MM AM/PM
        self.find_and_set_text("date", now)
        self.find_and_set_text("date_2", now)
        self.find_and_set_text("date_3", now)
        self.find_and_set_text("date_4", now)

    def display_total_cup(self, available, inuse):
        """Display total available and in-use cups."""
        self.find_and_set_text("totalAvailable", available)
        self.find_and_set_text("totalInUse", inuse)

    def display_today_progress(self, scanned, updated, deleted):
        """Display today's scanning progress."""
        self.find_and_set_text("todayScanned", scanned)
        self.find_and_set_text("todayUpdated", updated)
        self.find_and_set_text("todayDeleted", deleted)

    def scan_display_current_cup(self, tag, so, item, gem1, gem2, set_id):
        """Display current cup details."""
        self.find_and_set_text("curr_tag", tag)
        self.find_and_set_text("curr_so", so)
        self.find_and_set_text("curr_sku", item)
        self.find_and_set_text("curr_gem1", gem1)
        self.find_and_set_text("curr_gem2", gem2)
        self.find_and_set_text("curr_set_id", set_id)

    def update_display_current_cup(self, tag, status, so_2a, so_2b, item_2a, item_2b,
                                   gem1_2a, gem1_2b, gem2_2a, gem2_2b, set_id_2a, set_id_2b):
        """Display current cup details."""
        self.find_and_set_text("curr_tag_2a", tag)
        self.find_and_set_text("curr_status_2a", status)
        self.find_and_set_text("curr_so_2a", so_2a)
        self.find_and_set_text("curr_so_2b", so_2b)
        self.find_and_set_text("curr_sku_2a", item_2a)
        self.find_and_set_text("curr_sku_2b", item_2b)
        self.find_and_set_text("curr_gem1_2a", gem1_2a)
        self.find_and_set_text("curr_gem1_2b", gem1_2b)
        self.find_and_set_text("curr_gem2_2a", gem2_2a)
        self.find_and_set_text("curr_gem2_2b", gem2_2b)
        self.find_and_set_text("curr_set_id_2a", set_id_2a)
        self.find_and_set_text("curr_set_id_2b", set_id_2b)

    def complete_display_current_cup(self, tag, status, so_2a, so_2b, item_2a, item_2b,
                                   gem1_2a, gem1_2b, gem2_2a, gem2_2b, set_id_2a, set_id_2b):
        """Display current cup details."""
        self.find_and_set_text("curr_tag_3a", tag)
        self.find_and_set_text("curr_status_3a", status)
        self.find_and_set_text("curr_so_3a", so_2a)
        self.find_and_set_text("curr_so_3b", so_2b)
        self.find_and_set_text("curr_sku_3a", item_2a)
        self.find_and_set_text("curr_sku_3b", item_2b)
        self.find_and_set_text("curr_gem1_3a", gem1_2a)
        self.find_and_set_text("curr_gem1_3b", gem1_2b)
        self.find_and_set_text("curr_gem2_3a", gem2_2a)
        self.find_and_set_text("curr_gem2_3b", gem2_2b)
        self.find_and_set_text("curr_set_id_3a", set_id_2a)
        self.find_and_set_text("curr_set_id_3b", set_id_2b)

    def scan_display_previous_cup(self, tag, so, item, gem1, gem2, set_id):
        """Display previous cup details."""
        self.find_and_set_text("pre_tag", tag)
        self.find_and_set_text("pre_so", so)
        self.find_and_set_text("pre_sku", item)
        self.find_and_set_text("pre_gem1", gem1)
        self.find_and_set_text("pre_gem2", gem2)
        self.find_and_set_text("pre_set_id", set_id)

    def check_display_current_cup(self, tag, so, item, gem1, gem2, set_id):
        """Display current cup details."""
        self.find_and_set_text("curr_tag_4", tag)
        self.find_and_set_text("curr_so_4", so)
        self.find_and_set_text("curr_sku_4", item)
        self.find_and_set_text("curr_gem1_4", gem1)
        self.find_and_set_text("curr_gem2_4", gem2)
        self.find_and_set_text("curr_set_id_4", set_id)

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
    window.scan_curr_cup_color()
    window.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print("Closing Window...")
