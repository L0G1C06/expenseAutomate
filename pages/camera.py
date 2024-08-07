import flet as ft
import os
import cv2
import time
from components.container import create_base_container

def camera_page(page, home_page, go_to_camera_page, go_to_table_page, switch_to_login):
    myimage = ft.Image(
        src=False,
        width=300,
        height=300,
        fit='cover'
    )

    def remove_all_photos():
        folder_path = "images/"
        files = os.listdir(folder_path)
        for file in files:
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"File successfully removed: {file_path}")
        page.update()

    def take_picture(e):
        remove_all_photos()
        cap = cv2.VideoCapture(0)
        cv2.namedWindow("Webcam", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Webcam", 400, 600)
        timestamp = str(int(time.time()))
        myfileface = f"myPhoto_{timestamp}.jpg"
        try:
            ret, frame = cap.read()
            if ret:
                cv2.imwrite(f"images/{myfileface}", frame)
                cv2.putText(frame, "Capture successful!", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                myimage.src = "images/" + myfileface
                page.update()
            cap.release()
            cv2.destroyAllWindows()
        except Exception as e:
            print(e)
            print("Error during capture")

    return ft.Column([
        ft.Text("Tire a foto da nota", size=30, weight="bold"),
        ft.ElevatedButton("Tirar foto", bgcolor="blue", color="white", on_click=take_picture),
        myimage,
        ft.ElevatedButton(
            text="Voltar para Home", 
            on_click=lambda e: page.controls.clear() or page.add(create_base_container(home_page("", go_to_camera_page, go_to_table_page, switch_to_login))))
    ])