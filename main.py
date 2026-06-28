import sys
import pygame

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QGridLayout,
    QLabel,
    QPushButton,
)
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Moob Sound Machine 🐮🎵")
        self.setMinimumSize(800, 500)

        # Initialize audio
        pygame.mixer.init()
        sound_data = [
            ("🐮 YSMAMA", "YoSoyMAMA.wav"),
            ("🐈‍⬛ Lamoroxitah", "lamoroxita.wav"),
            ("👮 Hot Damn!", "hot_damn.wav")
        ]

        self.sounds = {}

        for button_name, filename in sound_data:
            self.sounds[button_name] = pygame.mixer.Sound(f"sounds/{filename}")
            

        # Central widget
        central = QWidget()
        self.setCentralWidget(central)

        layout = QGridLayout()
        central.setLayout(layout)

        # Title
        title = QLabel("🐮 The Herd")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title, 0, 0, 1, 3)
        self.sounds = {}

        for button_name, filename in sound_data:
            self.sounds[button_name] = pygame.mixer.Sound(f"sounds/{filename}")

        # 3x3 button grid
        for index, (button_name, filename) in enumerate(sound_data):

            row = index // 3 + 1
            col = index % 3

            button = QPushButton(button_name)
            button.sound_name = button_name  # Store the sound name in the button

            button.setMinimumHeight(80)
            button.clicked.connect(self.play_sound)

            layout.addWidget(button, row, col)



    def play_sound(self):
        button = self.sender()
        print(button.sound_name)
        sound = self.sounds.get(button.sound_name)

        if sound:
            print(f"Playing: {button.sound_name}")
            sound.play()

        


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())