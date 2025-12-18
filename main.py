import sys
import docker 
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from tela import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.client = docker.from_env()

        self.listar_containers()
        
        self.ui.startButton.clicked.connect(self.start_container)
        self.ui.stopButton.clicked.connect(self.stop_container)
        self.ui.removeButton.clicked.connect(self.remove_container)

    def listar_containers(self):
        containers = self.client.containers.list(all=True)
        self.ui.tableContainers.setRowCount(len(containers))

        for row, c in enumerate(containers):
            short_id = c.id[:12]
            name = c.name
            image = c.image.tags[0] if c.image.tags else "none"

            status = c.status
            
            self.ui.tableContainers.setItem(row, 0, QTableWidgetItem(short_id))
            self.ui.tableContainers.setItem(row, 1, QTableWidgetItem(name))
            self.ui.tableContainers.setItem(row, 2, QTableWidgetItem(image))
            self.ui.tableContainers.setItem(row, 3, QTableWidgetItem(status))


    def container_selecionado(self):
        row = self.ui.tableContainers.currentRow()
        if row == -1:
            return None
        return self.ui.tableContainers.item(row, 1).text()


    def start_container(self):
        nome = self.container_selecionado()
        if nome:
            self.client.containers.get(nome).start()
            self.listar_containers()


    def stop_container(self):
        nome = self.container_selecionado()
        if nome:
            self.client.containers.get(nome).stop()
            self.listar_containers()


    def remove_container(self):
        nome = self.container_selecionado()
        if nome:
            self.client.containers.get(nome).remove(force=True)
            self.listar_containers()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()   
    window.show()
    sys.exit(app.exec_())
