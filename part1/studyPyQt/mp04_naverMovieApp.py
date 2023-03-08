# Qt Designer 디자인 사용
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from NaverApi import *
import webbrowser   # 웹브라우저 모듈

class qtApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./studyPyQt/naverApiMovie.ui', self)
        self.setWindowIcon(QIcon('./studyPyQt/newpaper.png'))

        # 검색 버튼 클릭시그널 / 슬롯함수
        self.btnSearch.clicked.connect(self.btnSearchClicked)
        # 검색어 입력 후 엔터 치면 처리
        self.txtSearch.returnPressed.connect(self.txtSearchReturned)
        self.tblResult.doubleClicked.connect(self.tblResultDoubleClicked)

    def txtSearchReturned(self):
        self.btnSearchClicked()

    def tblResultDoubleClicked(self):
        # row = self.tblResult.currentIndex().row()
        # column = self.tblResult.currentIndex().column()
        # print(row, column)
        selected = self.tblResult.currentRow()
        url = self.tblResult.item(selected,5).text()
        webbrowser.open(url)    # 네이버 영화 웹사이트 오픈

    def btnSearchClicked(self):
        search = self.txtSearch.text()

        if search == '':
            QMessageBox.warning(self, '경고', '영화명을 입력하세요!')
            return 
        else:
            api = NaverApi()    # NaverApi 클래스 객체 생성
            node = 'movie'       # movie로 변경하면 영화검색
            display = 100

            result = api.get_naver_search(node, search, 1, display)
            print(result)
            # 테이블위젯에 출력 기능
            items = result['items']     # json 결과 중 items 아래 배열만 추출
            self.makeTable(items)       

    # 테이블 위젯에 데이터 표시 -- 네이버 영화 결과 변경
    def makeTable(self, items) -> None:
        self.tblResult.setSelectionMode(QAbstractItemView.SingleSelection)      # 단일선택
        self.tblResult.setColumnCount(7)    # 컬럼갯수 변경
        self.tblResult.setRowCount(len(items))      # 현재 100개 행 생성
        self.tblResult.setHorizontalHeaderLabels(['영화제목','개봉년도','감독', '배우진', '평점', '링크', '포스터'])
        self.tblResult.setColumnWidth(0,150)    # 영화제목 넓이
        self.tblResult.setColumnWidth(1,60)     # 개봉년도 넓이
        self.tblResult.setColumnWidth(4,45)     # 평점 넓이
        # 컬럼 데이터를 수정금지
        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers)

        for i, post in enumerate(items):     # 0, 뉴스...
            title = self.replaceHtmlTag(post['title'])      # HTML특수문자 변환
            pubDate = post['pubDate']
            director = post['director']
            actor = post['actor']
            userRating = post['userRating']
            link = post['link']
            
            # image = QImage(requests.get(post['image'], stream=True))
            # imageUrl = urlopen(post['image']).read()
            # image = QPixmap()
            # image.loadFromData(imageUrl)
            # imgLabel = QLabel()
            # imgLabel.setPixmap(QPixmap.fromImage(image))
            # imgLabel.setGeometry(0, 0, 60, 100)
            # imgLabel.resize(60, 100)

            # setItem(행, 열, 넣을데이터)
            self.tblResult.setItem(i, 0, QTableWidgetItem(title))
            self.tblResult.setItem(i, 1, QTableWidgetItem(pubDate))
            self.tblResult.setItem(i, 2, QTableWidgetItem(director))
            self.tblResult.setItem(i, 3, QTableWidgetItem(actor))
            self.tblResult.setItem(i, 4, QTableWidgetItem(userRating))
            self.tblResult.setItem(i, 5, QTableWidgetItem(link))
            self.tblResult.setCellWidget(i, 6, imgLabel)

    def replaceHtmlTag(self, sentence) -> str:
        result = sentence.replace('&lt;', '<')  # lesser than 작다
        result = result.replace('&gt;', '>')   # greater than 크다
        result = result.replace('<b>','')      #bold
        result = result.replace('</b>','')     #bold
        result = result.replace('&apos;',"'")   # apostopy 홀따옴표
        result = result.replace('&quot;','"')   # quotation mark 쌍따옴표
        # 변환 안된 특수문자가 나타나면 여기 추가

        return result


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())


