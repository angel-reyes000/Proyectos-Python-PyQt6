#Calculadora simple con operaciones basicas

import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (QApplication, 
                            QWidget, 
                            QMainWindow, 
                            QLineEdit, 
                            QPushButton,
                            QLabel,  
                            QHBoxLayout, 
                            QVBoxLayout, 
                            QRadioButton, 
                            QButtonGroup,
                            QDialog,
                            QDialogButtonBox, 
                            QMessageBox, 
                            )

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora simple")
        self.setFixedSize(QSize(400, 150))

        boton_respuesta = QPushButton("Evaluar")
        boton_respuesta.clicked.connect(self.operaciones)
        boton_respuesta.setDefault(True)

        self.texto1 = QLineEdit()
        self.texto1.setPlaceholderText("Escribe un numero...")
        self.texto1.returnPressed.connect(boton_respuesta.click)
        self.texto2 = QLineEdit()
        self.texto2.setPlaceholderText("Escribe un numero...")
        self.texto2.returnPressed.connect(boton_respuesta.click)

        self.radio_suma = QRadioButton("+")
        self.radio_resta = QRadioButton("-")
        self.radio_multiplicacion = QRadioButton("*")
        self.radio_division = QRadioButton("/")

        grupo_botones = QButtonGroup()
        grupo_botones.addButton(self.radio_suma)
        grupo_botones.addButton(self.radio_resta)
        grupo_botones.addButton(self.radio_multiplicacion)
        grupo_botones.addButton(self.radio_division)

        layout_izquierdo = QVBoxLayout()
        layout_izquierdo.addWidget(self.texto1)

        layout_central = QVBoxLayout()
        layout_central.addWidget(self.radio_suma, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_central.addWidget(self.radio_resta, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_central.addWidget(self.radio_multiplicacion, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_central.addWidget(self.radio_division, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_central.addWidget(boton_respuesta)

        layout_derecho = QVBoxLayout()
        layout_derecho.addWidget(self.texto2)

        layout_principal = QHBoxLayout()
        layout_principal.addLayout(layout_izquierdo)
        layout_principal.addLayout(layout_central)
        layout_principal.addLayout(layout_derecho)

        widget = QWidget()
        widget.setLayout(layout_principal)
        self.setCentralWidget(widget)

    def operaciones(self):
        radios = (self.radio_suma, self.radio_resta, self.radio_multiplicacion, self.radio_division)
        try:
            valor1 = float(self.texto1.text())
            valor2 = float(self.texto2.text())
            for radio in radios:
                if radio.isChecked():
                    signo = radio.text()
                    match signo:
                        case "+":
                            resultado = valor1 + valor2
                            dlg = CustomDialog(self, resultado)
                            dlg.exec()
                        case "-":
                            resultado = valor1 - valor2
                            dlg = CustomDialog(self, resultado)
                            dlg.exec()
                        case "*":
                            resultado = valor1 * valor2
                            dlg = CustomDialog(self, resultado)
                            dlg.exec()
                        case "/":
                            resultado = valor1 / valor2
                            dlg = CustomDialog(self, resultado)
                            dlg.exec()
        except ValueError as e:
            QMessageBox.warning(self, "Error", "Solo numeros")

class CustomDialog(QDialog):
    def __init__(self, parent, resultado):
        super().__init__(parent)
        self.resultado = str(resultado)
        self.setWindowTitle("Resultado")

        boton = (QDialogButtonBox.StandardButton.Ok)
        mensaje = QLabel("Resultado: " + self.resultado)
        dlg = QDialogButtonBox()
        dlg.accepted.connect(self.accept)
        dlg.setStandardButtons(boton)
        layout = QVBoxLayout()
        layout.addWidget(mensaje)
        layout.addWidget(dlg)
        self.setLayout(layout)

app = QApplication(sys.argv)

w = MainWindow()
w.show()

sys.exit(app.exec())