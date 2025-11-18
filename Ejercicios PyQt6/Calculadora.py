from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QVBoxLayout, QLineEdit, QPushButton, QLabel, QDialog, QDialogButtonBox, QMessageBox
from PyQt6.QtCore import Qt, QSize
import sys

#Calculadora simple

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.setFixedSize(QSize(300, 460))
        self.setMouseTracking(True)
        self.setStyleSheet("""
                            QLineEdit {
                                font-size: 40px;
                                font-weight: 600;
                                height: 70px;
                            }

                            QPushButton {
                                height: 70px;
                                font-size: 20px;
                            }
                            """)

        self.layout = QGridLayout()

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

        self.all()

    def Input(self):
        self.input = QLineEdit(alignment = Qt.AlignmentFlag.AlignRight)
        self.layout.addWidget(self.input, 0, 0, 1, 4)

    def Buttons(self):
        buttons = (
                ("+/-", "="),
            ("7", "8", "9", "+"), 
            ("4", "5", "6", "-"), 
            ("1", "2", "3", "x"),
            ("0", "C", ".", "/")
        )

        for row in range(len(buttons)):
            for column in range(len(buttons[row])):
                button = QPushButton(buttons[row][column])
                if button.text().isdigit() or button.text() == ".":
                     button.clicked.connect(lambda e, text = button.text(): self.Text(text))
                     self.layout.addWidget(button, (row + 1), column)
                elif button.text() == "+/-":
                    self.layout.addWidget(button, (row + 1), column, 1, 2)
                    button.clicked.connect(self.sign_change)
                elif button.text() == "=":
                    self.layout.addWidget(button, (row + 1), (column + 1), 1, 2)
                    button.clicked.connect(self.Equal)
                else:
                    self.layout.addWidget(button, (row + 1), column)
                    button.clicked.connect(lambda e, sign = button.text(): self.Operations(sign))

    def Text(self, text):
        if len(self.input.text()) <= 10:
            concatenation = self.input.text() + text
            self.input.setText(concatenation)
        else:
            dlg = CustomDialog("Longitud maxima", "No puedes exceder de diez numeros.")
            dlg.exec()

    def Operations(self, sign):
        self.sign = sign
        self.input_2 = self.input.text()
        self.input.setText("")

    def Equal(self):
        try:
            if len(self.input.text()) <= 10:
                match self.sign:
                    case "+":
                        self.input.setText(str(float(self.input_2) + float(self.input.text())))
                    case "-":
                        self.input.setText(str(float(self.input_2) - float(self.input.text())))
                    case "x":
                        self.input.setText(str(float(self.input_2) * float(self.input.text())))
                    case "/":
                        self.input.setText(str(float(self.input_2) / float(self.input.text())))
                    case "C":
                        self.input.setText("")
            else:
                dlg = CustomDialog("Longitud maxima", "No puedes exceder de diez numeros.")
                dlg.exec()
        except ZeroDivisionError as e:
            dlg = self.warning("Error", "No es posible dividir entre cero.")
            self.input.setText("")
        except Exception as e:
            dlg = self.warning("Error", "Solo se permiten teclas de la interfaz.")
            self.input.setText("")

    def sign_change(self):
        if not "-" in self.input.text():
            add_sign = "-" + self.input.text()
            self.input.setText(add_sign)
        else:
            text = self.input.text()[1::]
            self.input.setText(text)

    def all(self):
        self.Input()
        self.Buttons()

    def keyMoveEvent(self, event):
        event.accept()

    def warning(self, title, message):
        messagebox = QMessageBox.warning(self, title, message, QMessageBox.StandardButton.Ok)

class CustomDialog(QDialog):
    def __init__(self, title, message):
        super().__init__()
        self.setWindowTitle(title)

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        buttons.accepted.connect(self.accept)
        label = QLabel(message)
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(buttons)
        self.setLayout(layout)

app = QApplication(sys.argv)

w = MainWindow()
w.show()

sys.exit(app.exec())
