from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLabel, QDialog, QDialogButtonBox, QVBoxLayout
from PyQt6.QtCore import Qt, QSize, QTimer
from random import randint
from time import sleep
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("El clicker")
        self.setFixedSize(700, 400)
        self.setStyleSheet("""
                            QMainWindow {
                                background-color: black;
                                }
                            
                            QPushButton {
                                background-color: white;
                                border-radius: 10px;
                            }

                            QLabel {
                                color: white;
                                }
                                """)

        self.layout = QGridLayout()
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

        self.segundos = 0
        self.botones = list()
        self.Todo()

    def Botones(self):
        for fila in range(5):
            for columna in range(5):
                numero = randint(1, 999)
                boton = QPushButton(str(numero))
                boton.clicked.connect(lambda y, x = boton: self.desactivar_boton(x))
                boton.setStyleSheet("""
                                    font-size: 20px;
                                    padding: 20px;
                                    """)
                                        
                self.botones.append(boton)
                self.layout.addWidget(boton, fila, columna)

    def Etiqueta(self):
        self.segundos += 1
        self.label = QLabel(f"Tiempo: 0")
        self.label.setStyleSheet("""
                            font-size: 14px;
                            padding: 20px;
                            margin: 0px;
                            border: 1px solid black;
                            """)
        self.layout.addWidget(self.label, 5, 2)

    def Todo(self):
        self.Botones()
        self.Etiqueta()

    def desactivar_boton(self, boton):
        menor = 1000
        for botonn in self.botones:
            if int(botonn.text()) < menor:
                menor = int(botonn.text())
        if int(boton.text()) == menor:
            boton.setEnabled(False)
            boton.setStyleSheet("""
                                background-color: gray;
                                font-size: 20px;
                                padding: 20px;
                                """)
            self.Contador()
            self.botones.remove(boton)

    def Contador(self):
        if len(self.botones) == 25:
            self.Temporizador()
            
        if len(self.botones) == 1:
            self.timer.stop()
            dlg = CustomDialog()
            dlg.exec()

    def Temporizador(self):
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.actualizar_etiqueta)
        self.timer.start()

    def actualizar_etiqueta(self):
        self.label.setText(f"Tiempo: {str(self.segundos)}")
        self.segundos+=1

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Logrado!!")

        etiqueta = QLabel("Lo Lograste!! 🥳🥳🥳🎉🎉")
        botones = (QDialogButtonBox.StandardButton.Ok)
        dialogo = QDialogButtonBox(botones)
        dialogo.accepted.connect(self.accept)

        layout = QVBoxLayout()
        layout.addWidget(etiqueta)
        layout.addWidget(dialogo)
        self.setLayout(layout)

app = QApplication(sys.argv)

w = MainWindow()
w.show()

sys.exit(app.exec())


