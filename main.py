import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from tela import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Conectando os botões
        self.ui.startButton.clicked.connect(self.start_container)
        self.ui.stopButton.clicked.connect(self.stop_container)
        self.ui.removeButton.clicked.connect(self.remove_container)

    def start_container(self):
        print("START clicado")

    def stop_container(self):
        print("STOP clicado")

    def remove_container(self):
        print("REMOVE clicado")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
