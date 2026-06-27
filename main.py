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

        # Initialize pygame-ce mixer
        pygame.mixer.init()

        # Load our first sound
        self.sound = pygame.mixer.Sound("moob-sound-machine/sounds/YoSoyMAMA.wav")

        # UI
        central = QWidget()
        self.setCentralWidget(central)

        layout = QGridLayout()
        central.setLayout(layout)

        title = QLabel("🐮 First Moo Test")
        title.setAlignment(Qt.AlignCenter)

        button = QPushButton("🔊 Play Moo")
        button.clicked.connect(self.play_sound)

        layout.addWidget(title, 0, 0)
        layout.addWidget(button, 1, 0)

    def play_sound(self):
        print("🐮 Moo button pressed!")
        self.sound.play()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())
