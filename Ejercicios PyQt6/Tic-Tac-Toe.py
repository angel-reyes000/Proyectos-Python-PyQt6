from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QDialog, QDialogButtonBox, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt, QSize, pyqtSignal
from random import randint
import sys

#Juego de Tic-Tac-Toe

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-Tac-Toe")
        self.setFixedSize(QSize(500, 500))
        self.setStyleSheet("""
                            CustomLabel {
                                font-size: 60px;
                                text-align: right;
                                color: black;
                            }""")
        
        self.broke = False

        self.grid = QGridLayout()

        widget = QWidget()
        widget.setLayout(self.grid)
        self.setCentralWidget(widget)

        self.all()

    def Labels(self):
        for row in range(3):
            for column in range(3):
                label = CustomLabel()
                label.clicked.connect(lambda text = label: self.Circle(text))
                label.clicked.connect(lambda: self.win_or_lose("O"))
                label.clicked.connect(lambda: self.win_or_lose("X"))
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.grid.addWidget(label, row, column)
        center = self.grid.itemAtPosition(1, 1).widget()
        center.setText("X")

    def Circle(self, text):
        if len(text.text()) > 0:
            pass
        else:
            text.setText("O")
            text.setDisabled(True)
            self.cross_out()

    def cross_out(self):
        row = randint(0, 2)
        column = randint(0, 2)
        position = self.grid.itemAtPosition(row, column).widget()
        if len(position.text()) == 0:
            position.setText("X")
            return
        else:
            self.cross_out()

    def win_or_lose(self, text):
        if self.broke:
            pass
        else:
            lista = list()
            for row in range(3):
                for column in range(3):
                    position = self.grid.itemAtPosition(row, column).widget()
                    if position.text() == text:
                        lista.append(True)
                if len(lista) == 3:
                    if text == "O":
                        self.win_message()
                    else:
                        self.lose_message()
                    self.broke= True
                    return
                else:
                    lista = list()
                for column in range(3):
                    position = self.grid.itemAtPosition(column, row).widget()
                    if position.text() == text:
                        lista.append(True)
                if len(lista) == 3:
                    if text == "O":
                        self.win_message()
                    else:
                        self.lose_message()
                    self.broke = True
                    return
                else:
                    lista = list()
            if self.Position(0, 0) == text and self.Position(1, 1) == text and self.Position(2, 2) == text:
                self.lose_message()
                self.broke = True
                return
            elif self.Position(0, 2) == text and self.Position(1, 1) == text and self.Position(2, 0) == text:
                self.lose_message()
                self.broke = True
                return 
            else:
                lista = list()
                return

    def Position(self, row, column):
        position = self.grid.itemAtPosition(row, column).widget().text()
        return position

    def win_message(self):
        dlg = CustomDialog("Ganaste!!!", "Felicidades Ganaste!!!🥳🎉🎉")
        dlg.exec()

    def lose_message(self):
        dlg = CustomDialog("Perdiste:(", "Perdiste, Vuelve a intentarlo!😓")
        dlg.exec()

    def all(self):
        self.Labels()

class CustomLabel(QLabel):
    clicked = pyqtSignal()
    def __init__(self):
        super().__init__()

    def mousePressEvent(self, event):
        self.clicked.emit()

class CustomDialog(QDialog):
    def __init__(self, title, message):
        super().__init__()
        self.setWindowTitle(title)

        layout = QVBoxLayout()
        msg = QLabel(message)
        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok, )
        buttons.accepted.connect(self.accept)
        layout.addWidget(msg)
        layout.addWidget(buttons)
        self.setLayout(layout)

app = QApplication(sys.argv)

w = MainWindow()
w.show()

sys.exit(app.exec())