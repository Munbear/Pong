import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle("For Cuppang") # 타이틀을 정하는 코드 
        self.setGeometry(300,300,1000,700) # 창의 크기 설정하는 코드 
        btn = QPushButton("실행", self) #버튼 코드
        btn.resize(btn.sizeHint()) #버튼 크기
        btn.move(20, 30) #버튼 위치
        self.show() #창 띄우기


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

    