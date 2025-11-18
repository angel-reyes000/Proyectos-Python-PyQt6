import sys
from random import randint
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QDialog, QDialogButtonBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Juego de atrapar el boton")
        self.setFixedSize(800, 600)
        self.setStyleSheet("QPushButton{background-color: black; color: white;}")

        self.boton = QPushButton("Atrapame!")
        self.boton.setFixedSize(QSize(100, 50))
        self.boton.enterEvent = self.Mover
        self.boton.clicked.connect(self.Ganador)

        layout = QVBoxLayout()
        layout.addWidget(self.boton, alignment=Qt.AlignmentFlag.AlignCenter)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def Mover(self, event):
        horizontal_x = randint(0, 700)
        vertical_y = randint(0, 500)
        self.boton.move(horizontal_x, vertical_y)

    def Ganador(self):
        dlg = CustomDialog()
        dlg.exec()

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ganaste!")

        label = QLabel("Has ganado!!! 🥳🥳🎉🎉🎉")
        botones = (QDialogButtonBox.StandardButton.Ok)
        dlg = QDialogButtonBox(botones)
        dlg.accepted.connect(self.accept)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(dlg)
        self.setLayout(layout)

app = QApplication(sys.argv)

w = MainWindow()
w.show()

sys.exit(app.exec())