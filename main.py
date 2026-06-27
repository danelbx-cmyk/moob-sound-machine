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
        self.sound = pygame.mixer.Sound("sounds/YoSoyMAMA.wav")

        # Central widget
        central = QWidget()
        self.setCentralWidget(central)

        layout = QGridLayout()
        central.setLayout(layout)

        # Title
        title = QLabel("🐮 The Herd")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title, 0, 0, 1, 3)

        # 3x3 button grid
        for row in range(3):
            for col in range(3):
                button = QPushButton(f"Moo {row * 3 + col + 1} 🐮")
                button.setMinimumHeight(80)
                button.clicked.connect(self.play_sound)
                layout.addWidget(button, row + 1, col)

    def play_sound(self):
        print("🐮 Moo!")
        self.sound.play()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())