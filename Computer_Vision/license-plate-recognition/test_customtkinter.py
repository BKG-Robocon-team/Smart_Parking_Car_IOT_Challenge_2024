import tkinter as tk
from tkinter import messagebox, ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import cv2
import torch
import function.utils_rotate as utils_rotate
import function.helper as helper
import time
import pandas as pd
from datetime import datetime
import requests
import math

import mysql.connector
import winsound

# MySQL database information
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = ""
DB_NAME = "bai-do-xe-db"

# URL của API
OPEN_BARRIER_URL = "http://192.168.1.192/open-barrier.php"
CLOSE_BARRIER_URL = "http://192.168.1.192/close-barrier.php"

# Function to open the barrier
def open_barrier():
    response = requests.get(OPEN_BARRIER_URL)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'success':
            print("Barrier opened successfully")
        else:
            print("Failed to open the barrier")
    else:
        print("Failed to open the barrier")

# Function to close the barrier
def close_barrier():
    response = requests.get(CLOSE_BARRIER_URL)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'success':
            print("Barrier closed successfully")
        else:
            print("Failed to close the barrier")
    else:
        print("Failed to close the barrier")
        
def calculate_days_parked(license_plate):
    # Connect to the database
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = conn.cursor()
        
    query = """
        SELECT parking_time FROM thong_tin_ve_xe
        WHERE licence_plate = %s
    """
    cursor.execute(query, (license_plate,))
    result = cursor.fetchone()
    
    if result and result[0] and str(result[0]) != '0000-00-00 00:00:00':
        parking_time = result[0]
        current_time = datetime.now()
        days_parked = math.ceil((current_time - parking_time).days)
        return days_parked
    return 0
# Load model
yolo_LP_detect = torch.hub.load('yolov5', 'custom', path='model/LP_detector_nano_61.pt', force_reload=True, source='local')
yolo_license_plate = torch.hub.load('yolov5', 'custom', path='model/LP_ocr_nano_62.pt', force_reload=True, source='local')
yolo_license_plate.conf = 0.60

class SmartParkingBarrierApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Smart Parking Barrier System")
        self.geometry("1200x800")

        # Create tabs
        self.tab_view = ctk.CTkTabview(self)
        self.tab_view.pack(expand=1, fill="both")

        # Create a tab for the main functionality
        self.main_tab = self.tab_view.add("Main")
        self.create_main_tab(self.main_tab)

        # Create a tab for history and statistics
        self.history_tab = self.tab_view.add("History & Statistics")
        self.create_history_tab(self.history_tab)

        self.vid = cv2.VideoCapture(0)
        self.prev_frame_time = 0

        self.update()

    def create_main_tab(self, tab):
        # Create a frame for video
        self.video_frame = ctk.CTkFrame(tab)
        self.video_frame.pack(pady=20)

        self.label = ctk.CTkLabel(self.video_frame, text="")
        self.label.pack()

        # Create a frame for detected plates and controls
        self.controls_frame = ctk.CTkFrame(tab)
        self.controls_frame.pack(pady=20)

        self.plates_label = ctk.CTkLabel(self.controls_frame, text="Detected Plates:", font=("Arial", 16))
        self.plates_label.grid(row=0, column=0, padx=10, pady=10)

        self.plates_text = ctk.CTkTextbox(self.controls_frame, width=300, height=100)
        self.plates_text.grid(row=1, column=0, padx=10, pady=10)

        self.allow_entry_button = ctk.CTkButton(self.controls_frame, text="Allow Entry", command=self.allow_entry, state="disabled")
        self.allow_entry_button.grid(row=2, column=0, padx=10, pady=10)

        self.allow_exit_button = ctk.CTkButton(self.controls_frame, text="Allow Exit", command=self.allow_exit, state="disabled")
        self.allow_exit_button.grid(row=2, column=1, padx=10, pady=10)

    def create_history_tab(self, tab):
        self.history_frame = ctk.CTkFrame(tab)
        self.history_frame.pack(pady=20, fill="both", expand=True)

        self.tree = ttk.Treeview(self.history_frame, columns=("Timestamp", "Plate", "Action"), show='headings')
        self.tree.heading("Timestamp", text="Timestamp")
        self.tree.heading("Plate", text="Plate")
        self.tree.heading("Action", text="Action")
        self.tree.pack(pady=10, fill="both", expand=True)

        self.load_history_button = ctk.CTkButton(tab, text="Load History", command=self.load_history)
        self.load_history_button.pack(pady=10)

        self.delete_button = ctk.CTkButton(tab, text="Delete Selected", command=self.delete_selected)
        self.delete_button.pack(pady=10)

        self.stats_button = ctk.CTkButton(tab, text="Show Statistics", command=self.show_statistics)
        self.stats_button.pack(pady=10)

    def update(self):
        ret, frame = self.vid.read()
        if ret:
            frame = self.process_frame(frame)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.label.imgtk = imgtk
            self.label.configure(image=imgtk)

        self.after(10, self.update)

    def process_frame(self, frame):
        plates = yolo_LP_detect(frame, size=640)
        list_plates = plates.pandas().xyxy[0].values.tolist()
        list_read_plates = set()

        for plate in list_plates:
            flag = 0
            x = int(plate[0])  # xmin
            y = int(plate[1])  # ymin
            w = int(plate[2] - plate[0])  # xmax - xmin
            h = int(plate[3] - plate[1])  # ymax - ymin  
            crop_img = frame[y:y+h, x:x+w]
            cv2.rectangle(frame, (int(plate[0]), int(plate[1])), (int(plate[2]), int(plate[3])), color=(0, 0, 225), thickness=2)
            lp = ""

            for cc in range(0, 2):
                for ct in range(0, 2):
                    lp = helper.read_plate(yolo_license_plate, utils_rotate.deskew(crop_img, cc, ct))
                    if lp != "unknown":
                        list_read_plates.add(lp)
                        cv2.putText(frame, lp, (int(plate[0]), int(plate[1]-10)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
                        flag = 1
                        break
                if flag == 1:
                    break

        new_frame_time = time.time()
        fps = 1/(new_frame_time - self.prev_frame_time)
        self.prev_frame_time = new_frame_time
        fps = int(fps)
        cv2.putText(frame, str(fps), (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (100, 255, 0), 3, cv2.LINE_AA)

        self.plates_text.delete("1.0", tk.END)
        if list_read_plates:
            self.allow_entry_button.configure(state="normal")
            self.allow_exit_button.configure(state="normal")
            for plate in list_read_plates:
                self.plates_text.insert(tk.END, f"{plate}\n")
        else:
            self.allow_entry_button.configure(state="disabled")
            self.allow_exit_button.configure(state="disabled")

        return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    def allow_entry(self):
        plates = self.plates_text.get("1.0", tk.END).strip().split('\n')
        if plates:
            self.check_and_log(plates[0], "entry")

    def allow_exit(self):
        plates = self.plates_text.get("1.0", tk.END).strip().split('\n')
        if plates:
            self.check_and_log(plates[0], "exit")
    def check_and_log(self, plate, action):
        # Connect to the database
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor()

        # Query to check the licence plate and its status
        query = "SELECT is_parking FROM thong_tin_ve_xe WHERE licence_plate = %s"
        cursor.execute(query, (plate,))
        result = cursor.fetchone()

        if result:
            status = result[0]
            if action == "entry" and status == 0:
                messagebox.showinfo("Thông báo", f"Xe biển số {plate} đã vào bãi. Cho phép vào.")
                parking_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                winsound.Beep(1000, 500)  # Beep sound
                # Update the status to 1 (in the parking lot)
                update_query = "UPDATE thong_tin_ve_xe SET parking_time = %s, is_parking = 1 WHERE licence_plate = %s"
                cursor.execute(update_query, (parking_time, plate,))
                conn.commit()
                self.log_entry_exit(plate, action)
                open_barrier()
                time.sleep(5)
                close_barrier()
            elif action == "exit" and status == 1:
                day_parking = calculate_days_parked(plate)
                messagebox.showinfo("Thông báo", f"Xe biển số {plate} đã đỗ xe trong {day_parking} ngày. Cho phép ra.")
                winsound.Beep(1000, 500)  # Beep sound
                # Update the status to 0 (out of the parking lot)
                update_query = "UPDATE thong_tin_ve_xe SET parking_time = '0000-00-00 00:00:00', is_parking = 0 WHERE licence_plate = %s"
                cursor.execute(update_query, (plate,))
                conn.commit()
                self.log_entry_exit(plate, action)
                open_barrier()
                time.sleep(5)
                close_barrier()
            else:
                messagebox.showwarning("Cảnh báo", f"Xe biển số {plate} không có trong cơ sở dữ liệu hoặc trạng thái không đúng.")
                winsound.Beep(500, 500)  # Different beep sound
        else:
            messagebox.showwarning("Cảnh báo", f"Xe biển số {plate} không có trong cơ sở dữ liệu.")
            winsound.Beep(500, 500)  # Different beep sound

        cursor.close()
        conn.close()

    def log_entry_exit(self, plate, action):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Insert log into the MySQL database
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor()
        log_query = "INSERT INTO history_log (licence_plate, timestamp, action) VALUES (%s, %s, %s)"
        cursor.execute(log_query, (plate, timestamp, action))
        conn.commit()
        cursor.close()
        conn.close()

        messagebox.showinfo("Success", f"Logged {action} for {plate}")
        self.load_history()

    def load_history(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        try:
            # Load history from the MySQL database
            conn = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
            )
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM history_log")
            rows = cursor.fetchall()
            for row in rows:
                self.tree.insert("", tk.END, values=(row[2], row[1], row[3]))  # Assuming the order of columns is id, licence_plate, timestamp, action
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            messagebox.showwarning("Warning", f"Error: {err}")

    def delete_selected(self):
        selected_item = self.tree.selection()[0]
        licence_plate = self.tree.item(selected_item)['values'][1]
        timestamp = self.tree.item(selected_item)['values'][0]
        self.tree.delete(selected_item)
        # Delete the selected entry from the MySQL database
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor()
        delete_query = "DELETE FROM history_log WHERE licence_plate = %s AND timestamp = %s"
        cursor.execute(delete_query, (licence_plate, timestamp))
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Success", "Deleted selected entry")

    def show_statistics(self):
        try:
            # Load statistics from the MySQL database
            conn = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
            )
            cursor = conn.cursor()
            cursor.execute("SELECT DATE(timestamp) as date, action, COUNT(*) as count FROM history_log GROUP BY date, action")
            rows = cursor.fetchall()
            stats_message = ""
            for row in rows:
                stats_message += f"Date: {row[0]}\n"
                stats_message += f"Entries: {row[2] if row[1] == 'entry' else 0}\n"
                stats_message += f"Exits: {row[2] if row[1] == 'exit' else 0}\n"
                stats_message += "\n"
            cursor.close()
            conn.close()
            messagebox.showinfo("Statistics", stats_message)
        except mysql.connector.Error as err:
            messagebox.showwarning("Warning", f"Error: {err}")

if __name__ == "__main__":
    app = SmartParkingBarrierApp()
    app.mainloop()
