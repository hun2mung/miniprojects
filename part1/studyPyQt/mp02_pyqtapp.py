# Qt Designer 디자인 사용
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

class qtApp(QWidget):
    count = 0   # 클릭횟수 카운트 변수

    def __init__(self):
        super().__init__()
        uic.loadUi('./studyPyQt/mainApp.ui', self)

        # Qt Designer에서 구성한 위젯시그널 만듬
        self.btnOk.clicked.connect(self.btnOkClicked)
        self.btnPOP.clicked.connect(self.btnPOPClicked)

    def btnOkClicked(self):     # 슬롯함수
        self.count += 1
        self.lblMessage.clear()
        self.lblMessage.setText(f'메세지: OK!!! + {self.count}')

    def btnPOPClicked(self):
        QMessageBox.about(self, 'popup', '까꿍!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())

