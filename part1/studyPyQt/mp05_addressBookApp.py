# 주소록 GUI 프로그램 - MySQL 연동
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *   # QIcon은 여기 있음
import pymysql

class qtApp(QMainWindow):
    conn = None
    curIdx = 0      # 현재 데이터 PK
    
    def __init__(self):
        super().__init__()
        uic.loadUi('./studyPyQt/addressBook.ui', self)
        self.setWindowIcon(QIcon('./studyPyQt/addressBook.png'))
        self.setWindowTitle('주소록 v.0.5')

        self.initDB()   # DB 초기화

        # 버튼 시그널/슬롯함수 지정
        self.btnNew.clicked.connect(self.btnNewClicked)
        self.btnSave.clicked.connect(self.btnSaveClicked)
        self.tblAddress.doubleClicked.connect(self.tblAddressDoubleClicked)
        self.btnDel.clicked.connect(self.btnDelClicked)

    def btnDelClicked(self):
        pass

    def btnNewClicked(self):    # 신규버튼 누르면
        # 라인에디트 내용 삭제 후 이름에 포커스
        self.txtName.setText('')
        self.txtPhone.setText('')
        self.txtEmail.setText('')
        self.txtAddress.setText('')
        self.txtName.setFocus()
        self.curIdx = 0 # 0은 진짜 신규!

    def tblAddressDoubleClicked(self):  #
        rowIndex = self.tblAddress.currentRow()
        self.txtName.setText(self.tblAddress.item(rowIndex, 1).text())
        self.txtPhone.setText(self.tblAddress.item(rowIndex, 2).text())
        self.txtEmail.setText(self.tblAddress.item(rowIndex, 3).text())
        self.txtAddress.setText(self.tblAddress.item(rowIndex, 4).text())
        self.curIdx = int(self.tblAddress.item(rowIndex, 0).text())
        print(self.curIdx)
        
    def btnSaveClicked(self):   # 저장
        fullName = self.txtName.text()
        phoneNum = self.txtPhone.text()
        email = self.txtEmail.text()
        address = self.txtAddress.text()

        # print(fullName, phoneNum, email, address)
        # 이름과 전화번호를 입력하지 않으면 알람
        if fullName == '' or phoneNum == '':
            QMessageBox.warning(self, '주의', '이름과 핸드폰번호 입력하세요!')
            return  # 진행불가
        else:
            self.conn = pymysql.connect(host='localhost', user='root', password = '12345',
                                        db = 'miniproject', charset = 'utf8')
            if self.curIdx == 0 : # 신규이면
            # 4개 변수값 받아서 INSERT 쿼리문 만들기
                query = '''INSERT INTO addressbook(FullName, PhoneNum, Email, address)
                            VALUES (%s, %s, %s, %s)'''
            else:       # UPDATE 쿼리문
                query = '''UPDATE addressbook
                              SET FullName = %s
                                , PhoneNum = %s
                                , Email = %s
                                , address = %s
                            WHERE Idx = %s'''
                
            cur = self.conn.cursor()
            if self.curIdx == 0:
                cur.execute(query, (fullName, phoneNum, email, address))
            else:   # 업데이트
                cur.execute(query, (fullName, phoneNum, email, address, self.curIdx))

            self.conn.commit()
            self.conn.close()
            
            if self.curIdx == 0:    # 저장성공 메시지
                QMessageBox.about(self, '성공', '저장 성공')
            else:   # 업데이트
                QMessageBox.about(self, '성공', '변경 성공')

            self.initDB()   # QTableWidget 새 데이터가출력되도록 
            self.btnNewClicked()    # 입력창 내용 없어져

    def initDB(self):
        self.conn = pymysql.connect(host='localhost', user='root', password = '12345',
                                    db = 'miniproject', charset = 'utf8')
        cur = self.conn.cursor()
        query = '''SELECT Idx
                        , FullName
                        , PhoneNum
                        , Email
                        , address
                    FROM addressbook'''     # 멀티라인 문자열 편함!
        cur.execute(query)
        rows = cur.fetchall()

        self.makeTable(rows)
        self.conn.close()       # 프로그램 종료할 때
    
    def makeTable(self, rows):
        self.tblAddress.setColumnCount(5)       # 0. 열갯수
        self.tblAddress.setRowCount(len(rows))       # 0. 행갯수
        self.tblAddress.setSelectionMode(QAbstractItemView.SingleSelection)     # 1. 단일선택
        self.tblAddress.setHorizontalHeaderLabels(['번호', '이름', '핸드폰', '이메일', '주소'])     # 1. 열제목
        self.tblAddress.setColumnWidth(0,0)   # 1. 번호는 숨김
        self.tblAddress.setColumnWidth(1,70)   # 이름 열 70
        self.tblAddress.setColumnWidth(2,105)   # 핸드폰 열 105
        self.tblAddress.setColumnWidth(3,175)   # 이메일 열 175
        self.tblAddress.setColumnWidth(4,200)   # 주소 열 200
        self.tblAddress.setEditTriggers(QAbstractItemView.NoEditTriggers)   # 1. 컬럼 수정 금지

        for i, row in enumerate(rows):
            # row[0] ~ row[4]
            idx = row[0]
            fullName = row[1]
            phoneNumber = row[2]
            email = row[3]
            address = row[4]

            self.tblAddress.setItem(i, 0, QTableWidgetItem(str(idx)))
            self.tblAddress.setItem(i, 1, QTableWidgetItem(fullName))
            self.tblAddress.setItem(i, 2, QTableWidgetItem(phoneNumber))
            self.tblAddress.setItem(i, 3, QTableWidgetItem(email))
            self.tblAddress.setItem(i, 4, QTableWidgetItem(address))

        self.stbCurrent.showMessage(f'전체 주소록 : {len(rows)}개')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())