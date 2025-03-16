from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic
import sys
from datetime import datetime

# Define the total cups and cups in use
total_cup = 5000
cup_in_use = 2850

today_scanned = 580
today_updated = 35
today_deleted = 420

current_cup_so = "12568296"
current_cup_sku = "ED-TIFFNY-YG-25g-L9l16"
current_cup_gem1 = "faceted-2.0CZ"
current_cup_gem2 = "faceted-1.5x3CZ-Mq"
current_cup_set_id = "9233rr3r:33r23t23t3r2t4234gtq34:2fq243f342:33r23t23t3r2t4234gtq34"

previous_cup_so = "845954565"
previous_cup_sku = "ED-ZIAFACET-RG-25g-L9l16"
previous_cup_gem1 = "faceted-2.0GN-ge"
previous_cup_gem2 = "faceted-1.5x3CZ-Mq"
previous_cup_set_id = "9233rr3r:33r23t23t3r2t4234gtq34:2fq243f342:33r23t23t3r2t4234gtq34"

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('test_03.ui', self)  # Load the UI file
        self.setWindowTitle('Anatometal NFC Registration')

        # Validate UI elements before using them
        if getattr(self, "date", None) is None:
            print("Error: QTextEdit with objectName 'date' not found!")

        if getattr(self, "totalAvailable", None) is None:
            print("Error: QTextEdit with objectName 'totalAvailable' not found!")

        if getattr(self, "totalInUse", None) is None:
            print("Error: QTextEdit with objectName 'totalInUse' not found!")

        if getattr(self, "todayScanned", None) is None:
            print("Error: QTextEdit with objectName 'todayScanned' not found!")

        if getattr(self, "todayUpdated", None) is None:
            print("Error: QTextEdit with objectName 'todayUpdated' not found!")

        if getattr(self, "todayDeleted", None) is None:
            print("Error: QTextEdit with objectName 'todayDeleted' not found!")

        if getattr(self, "curr_so", None) is None:
            print("Error: QTextEdit with objectName 'curr_so' not found!")

        if getattr(self, "curr_sku", None) is None:
            print("Error: QTextEdit with objectName 'curr_sku' not found!")

        if getattr(self, "curr_gem1", None) is None:
            print("Error: QTextEdit with objectName 'curr_gem1' not found!")

        if getattr(self, "curr_gem2", None) is None:
            print("Error: QTextEdit with objectName 'curr_gem2' not found!")

        if getattr(self, "curr_set_id", None) is None:
            print("Error: QTextEdit with objectName 'curr_set_id' not found!")

    def display_current_datetime(self):
        """Get the current date and time and display it in self.date."""
        now = datetime.now().strftime("%m/%d/%Y %I:%M %p")  # Format: MM/DD/YYYY HH:MM AM/PM
        self.date.setPlainText(now)  # Set the text

    def display_total_cup(self, available, inuse):
        """Display total available and in-use cups."""
        self.totalAvailable.setPlainText(str(available))  # Convert to string before setting
        self.totalInUse.setPlainText(str(inuse))  # Convert to string before setting

    def display_today_progress(self, scanned, updated, deleted):
        """Display total available and in-use cups."""
        self.todayScanned.setPlainText(str(scanned))  # Convert to string before setting
        self.todayUpdated.setPlainText(str(updated))  # Convert to string before setting
        self.todayDeleted.setPlainText(str(deleted))  # Convert to string before setting

    def display_current_cup(self, so, item, gem1, gem2, set_id):
        """Display total available and in-use cups."""
        self.curr_so.setPlainText(str(so))  # Convert to string before setting
        self.curr_sku.setPlainText(str(item))  # Convert to string before setting
        self.curr_gem1.setPlainText(str(gem1))  # Convert to string before setting
        self.curr_gem2.setPlainText(str(gem2))  # Convert to string before setting
        self.curr_set_id.setPlainText(str(set_id))  # Convert to string before setting

    def display_previous_cup(self, so, item, gem1, gem2, set_id):
        """Display total available and in-use cups."""
        self.pre_so.setPlainText(str(so))  # Convert to string before setting
        self.pre_sku.setPlainText(str(item))  # Convert to string before setting
        self.pre_gem1.setPlainText(str(gem1))  # Convert to string before setting
        self.pre_gem2.setPlainText(str(gem2))  # Convert to string before setting
        self.pre_set_id.setPlainText(str(set_id))  # Convert to string before setting


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()

    # Display the current date/time
    window.display_current_datetime()

    # Display the cup counts
    window.display_total_cup(total_cup, cup_in_use)

    # Display the today progress
    window.display_today_progress(today_scanned, today_updated, today_deleted)

    # Display current cup
    window.display_current_cup(current_cup_so, current_cup_sku, current_cup_gem1, current_cup_gem2, current_cup_set_id)

    # Display previous cup
    window.display_previous_cup(previous_cup_so, previous_cup_sku, previous_cup_gem1, previous_cup_gem2, previous_cup_set_id)

    try:
        sys.exit(app.exec())
    except SystemExit:
        print("Closing Window...")
