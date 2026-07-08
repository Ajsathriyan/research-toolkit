import sys
from PySide6.QtWidgets import QApplication
from gui.main_window import MainWindow

app = QApplication.instance()

if app is None:
    app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()