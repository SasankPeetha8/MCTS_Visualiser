# This Python file uses the following encoding: utf-8
import sys, os
from pathlib import Path
# Appending the path
# Specifying the path
CustomizedWindow_Path = os.path.join('UI','Functions')
sys.path.append(CustomizedWindow_Path)
from CustomizedWindow import CustomMainWindow

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from CustomizedWindow import CustomMainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = CustomMainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = CustomMainWindow()
    widget.show()
    sys.exit(app.exec())
