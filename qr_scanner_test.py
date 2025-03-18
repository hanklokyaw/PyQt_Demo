### Test Work
# import evdev
#
# def capture_qr_code(device_path="/dev/input/event7"):
#     """Reads QR code input from the USB scanner event device."""
#     try:
#         device = evdev.InputDevice(device_path)
#         print(f"Listening for QR codes on {device_path}...")
#
#         qr_code = ""
#         for event in device.read_loop():
#             if event.type == evdev.ecodes.EV_KEY and event.value == 1:  # Key press event
#                 key = evdev.ecodes.KEY[event.code].replace("KEY_", "")
#
#                 if key == "ENTER":
#                     break  # End of QR code, return result
#                 elif len(key) == 1:  # Ignore special keys
#                     qr_code += key.lower()
#
#         return qr_code
#
#     except Exception as e:
#         print(f"Error: {e}")
#         return None
#
# # Example usage
# qr_result = capture_qr_code()
# print(f"Scanned QR Code: {qr_result}")


### Dynamic Scan work
# import os
#
#
# def find_event_device(device_name):
#     event_base_path = "/proc/bus/input/devices"
#     event_dir = "/dev/input/"
#
#     with open(event_base_path, "r") as f:
#         lines = f.readlines()
#
#     device_event = None
#     for i, line in enumerate(lines):
#         if f'N: Name="{device_name}"' in line:
#             for j in range(i, len(lines)):
#                 if lines[j].startswith("H: Handlers="):
#                     handlers = lines[j].split("=")[1].strip().split()
#                     for handler in handlers:
#                         if "event" in handler:
#                             device_event = handler
#                             break
#                 if device_event:
#                     break
#         if device_event:
#             break
#
#     if device_event:
#         return os.path.join(event_dir, device_event)
#     return None
#
#
# scanner_device = find_event_device("WCM HIDKeyBoard")  # Change to your scanner's name
# if scanner_device:
#     print(f"QR scanner is detected at: {scanner_device}")
# else:
#     print("QR scanner not found.")


# import os
# import evdev
#
#
# def find_qr_scanner():
#     event_base_path = "/proc/bus/input/devices"
#     event_dir = "/dev/input/"
#
#     with open(event_base_path, "r") as f:
#         lines = f.readlines()
#
#     device_event = None
#     for i, line in enumerate(lines):
#         if "Name=\"" in line:  # Adjust this if you know your scanner's exact name
#             for j in range(i, len(lines)):
#                 if lines[j].startswith("H: Handlers="):
#                     handlers = lines[j].split("=")[1].strip().split()
#                     for handler in handlers:
#                         if "event" in handler:
#                             device_event = handler
#                             break
#                 if device_event:
#                     break
#         if device_event:
#             break
#
#     if device_event:
#         return os.path.join(event_dir, device_event)
#     return None
#
#
# def capture_qr_code():
#     """Reads QR code input from the USB scanner event device."""
#     device_path = find_qr_scanner()
#     if not device_path:
#         print("QR scanner not found.")
#         return None
#
#     try:
#         device = evdev.InputDevice(device_path)
#         # print(f"Listening for QR codes on {device_path}...")
#
#         qr_code = ""
#         for event in device.read_loop():
#             if event.type == evdev.ecodes.EV_KEY and event.value == 1:  # Key press event
#                 key = evdev.ecodes.KEY[event.code].replace("KEY_", "")
#
#                 if key == "ENTER":
#                     break  # End of QR code, return result
#                 elif len(key) == 1:  # Ignore special keys
#                     qr_code += key.lower()
#
#         return qr_code
#
#     except Exception as e:
#         print(f"Error: {e}")
#         return None


# # Example usage
# qr_result = capture_qr_code()
# if qr_result:
#     print(f"Scanned QR Code: {qr_result}")


import os
import evdev

# Dictionary to keep track of scanned NFC tags
scanned_nfc = set()

def find_qr_scanner():
    event_base_path = "/proc/bus/input/devices"
    event_dir = "/dev/input/"

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
    return None


def capture_qr_code():
    """Reads QR code input from the USB scanner event device."""
    device_path = find_qr_scanner()
    if not device_path:
        print("QR scanner not found.")
        return None

    try:
        device = evdev.InputDevice(device_path)
        qr_code = ""
        for event in device.read_loop():
            if event.type == evdev.ecodes.EV_KEY and event.value == 1:  # Key press event
                key = evdev.ecodes.KEY[event.code].replace("KEY_", "")

                if key == "ENTER":
                    break  # End of QR code, return result
                elif len(key) == 1:  # Ignore special keys
                    qr_code += key.lower()

        return qr_code

    except Exception as e:
        print(f"Error: {e}")
        return None
