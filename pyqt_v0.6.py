from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6 import uic
from py532lib.i2c import *
from py532lib.frame import *
from py532lib.constants import *
import RPi.GPIO as GPIO
import sys
import time
import evdev
import os

# Worker thread for NFC detection
class NFCScannerThread(QThread):
    tag_detected = pyqtSignal(str)  # Signal to send detected tag data

    def run(self):
        pn532 = Pn532_i2c()
        pn532.SAMconfigure()

        last_tag_id = None

        while True:  # Continuous scanning loop
            try:
                card_data = pn532.read_mifare()
                if card_data:
                    raw_tag_id = card_data.get_data()
                    tag_id = extract_uid_from_frame(raw_tag_id)

                    if tag_id and tag_id != last_tag_id:
                        self.tag_detected.emit(tag_id)  # Emit signal with tag data
                        last_tag_id = tag_id

                time.sleep(0.5)  # Prevent CPU overload

            except Exception as e:
                print(f"Error reading tag: {e}")


# Worker thread for QR code scanning
class QRScannerThread(QThread):
    qr_detected = pyqtSignal(str)  # Signal to send detected QR data

    def run(self):
        device_path = find_qr_scanner()
        if not device_path:
            print("QR scanner not found.")
            return

        try:
            device = evdev.InputDevice(device_path)
            qr_code = ""

            for event in device.read_loop():
                if event.type == evdev.ecodes.EV_KEY and event.value == 1:  # Key press event
                    key = evdev.ecodes.KEY[event.code].replace("KEY_", "")

                    if key == "ENTER":
                        self.qr_detected.emit(qr_code)  # Send the captured QR code
                        qr_code = ""  # Reset for the next scan
                    elif len(key) == 1:  # Ignore special keys
                        qr_code += key.lower()

        except Exception as e:
            print(f"Error: {e}")

def extract_uid_from_frame(frame_data):
    if len(frame_data) >= 4:
        numbers = [i for i in frame_data[:4]]  # Take first 4 bytes as UID
        return '{}-{}-{}-{}'.format(*numbers)
    return None


def find_qr_scanner():
    """Finds the event device for the QR scanner."""
    event_base_path = "/proc/bus/input/devices"
    event_dir = "/dev/input/"

    try:
        with open(event_base_path, "r") as f:
            lines = f.readlines()

        device_event = None
        for i, line in enumerate(lines):
            if "Name=\"" in line:  # Adjust this if you know your scanner's exact name
                for j in range(i, len(lines)):
                    if lines[j].startswith("H: Handlers="):
                        handlers = lines[j].split("=")[1].strip().split()
                        for handler in handlers:
                            if "event" in handler:
                                device_event = handler
                                break
                    if device_event:
                        break
            if device_event:
                break

        if device_event:
            return os.path.join(event_dir, device_event)
    except Exception as e:
        print(f"Error finding QR scanner: {e}")

    return None

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('test_06.ui', self)
        self.setWindowTitle('Anatometal NFC & QR Registration')

        # Start the NFC scanner thread
        self.nfc_thread = NFCScannerThread()
        self.nfc_thread.tag_detected.connect(self.update_nfc)  # Connect NFC signal to UI update function
        self.nfc_thread.start()

        # Start the QR scanner thread
        self.qr_thread = QRScannerThread()
        self.qr_thread.qr_detected.connect(self.update_qr)  # Connect QR signal to UI update function
        self.qr_thread.start()

    def update_nfc(self, tag_id):
        """Update the UI labels when an NFC tag is detected."""
        self.nfc.setText(tag_id)  # Update the NFC field

    def update_qr(self, qr_code):
        """Update the UI labels when a QR code is detected."""
        self.qr.setText(qr_code)  # Update the QR field

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print("Closing Window...")
