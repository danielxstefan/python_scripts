import tkinter as tk
import serial
import time

def close_application():
        window.destroy()


relay1_state = False



def read_com_port(filename):
    try:
        with open(filename, 'r') as file:
            line = file.readline().strip()
            if line.startswith('com:'):
                return int(line.split(':')[1])
            else:
                 raise ValueError("Invalid content in the file. Expected forma: 'com:<port_number>")
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found.")
    except Exception as e:
         raise e

def toggle_relay1():
    global relay1_state
    relay1_state = not relay1_state
    if relay1_state:
        print("Relay1 1 activated")
        button1.config(gb='red')
        # Activate relay 1
        ser.write(b'set1on')
        time.sleep(0.3)
        
    else:
        print("Relay1 deactivated")
        button1.config(gb=default_bg_color)
        # Dectivate relay 1
        ser.write(b'set1off')
        time.sleep(0.3)


# Read the COM port file

try:
    com_port = read_com_port('serial.txt')
    print(f"COM Port read from file: {com_port}")
except Exceprion as e:
    print(f"Error reading COM port {e}")
    com_port = None # Handle the case where the COM port is not properly read

# Create the main window
window = tk.Tk()
window.title("Relay Control Panel")

if com_port is not None:
    ser = serial.Serial(f'COM{com_port}', baudrate=9600, timeout=1)
    # Store default button color
    deafault_bg_color = .0.cget('bg')

    #Create buttons
    button1 = tk.Button(window, text="Realy 1", command=toggle_relay1)

    #Place buttons
    button1.pack(pady=10)

else:
    label = tk.Label(window, text="Invalid COM port configuration.\n Please check serial.txt")
    label.pack(pady=10)
    close_button = tk.Button(window, text="Close", command=close_application)
    close_button.pack(pady=10)

#Run the application
window.mainloop()










