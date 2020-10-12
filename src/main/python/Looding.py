from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
from PyQt5 import QtCore


class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(200, 200)
        self.setWindowFlags(
           Qt.SplashScreen
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowModality(Qt.ApplicationModal)

        self.label_animation = QLabel(self)
        self.label_animation.setStyleSheet("background: transparent;")
        self.movie = QMovie('images/fluid-loader.gif')
        self.movie.setScaledSize(QtCore.QSize(200, 200))
        self.label_animation.setMovie(self.movie)
        self.label_animation.setStyleSheet("background-color: rgba(0,0,0,0%)")

    def startAnimation(self):
        self.movie.start()
        self.show()

    def stopAnimotion(self):
        self.movie.stop()
        self.close()

