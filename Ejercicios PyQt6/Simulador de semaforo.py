from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt, QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-Tac-Toe")
        self.setFixedSize(QSize(250, 600))
        self.count = 0
        self.setStyleSheet("""
                            QMainWindow {
                            background-color: black;}

                            QLabel {
                                background-color:gray;
                                border-radius: 70px;
                                margin-bottom: 10px;
                                color: white;}

                            QPushButton {
                            margin: 10px 0px 0px 0px 
                            padding: 0px;
                            width: 10px;
                            }
                                """)

        self.layout = QVBoxLayout()
        self.All()

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)
        
    def Labels(self):
        self.list = list()
        for label in range(3):
            label = QLabel()
            self.layout.addWidget(label)
            self.list.append(label)

    def Buttons(self):
        button_next = QPushButton("Next")
        button_next.clicked.connect(self.Colors)
        button_quit = QPushButton("Quit")
        button_quit.clicked.connect(self.Quit)
        self.layout.addWidget(button_next)
        self.layout.addWidget(button_quit)

    def All(self):
        self.Labels()
        self.Buttons()

    def Colors(self):
        self.count+=1
        if self.count == 1:
            self.list[0].setStyleSheet("background-color: red;")
            self.list[1].setStyleSheet("background-color: gray;")
            self.list[2].setStyleSheet("background-color: gray;")
        elif self.count == 2:
            self.list[0].setStyleSheet("background-color: gray;")
            self.list[1].setStyleSheet("background-color: yellow;")
            self.list[2].setStyleSheet("background-color: gray;")
        else:
            self.list[0].setStyleSheet("background-color: gray;")
            self.list[1].setStyleSheet("background-color: gray;")
            self.list[2].setStyleSheet("background-color: green;")
            self.count = 0

    def Quit(self):
        sys.exit()
        
app = QApplication(sys.argv)

w = MainWindow()
w.show()

sys.exit(app.exec())