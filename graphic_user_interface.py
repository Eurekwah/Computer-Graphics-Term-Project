import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, QMessageBox, QDesktopWidget, QAction, QLabel, QInputDialog
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import digital_differential_analyzer as dda
import Bresenham as bre
import mid_point_circle as mpc
import mid_point_ellipse as mpe

WIDTH = 900
HEIGHT = 600


class gui(QWidget):
    x_c, y_c = 300, 300
    points = []
    pra_dda = []
    pra_bre = []
    pra_mpc = []
    pra_mpe = []

    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)

    def initUI(self):
        self.initWindow()
        self.setColor()
        self.text = ["Digital Differential \nAnalyzer", "画线",
                     "Bresenham", "画线", "Mid Point Circle", "中点圆", "Mid PointnEllipse", "中点椭圆", "Export", "Exit"]
        self.pos = None
        self.show()

    def initWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowOpacity(0.8)
        self.resize(WIDTH, HEIGHT)
        self.center()
        self.setWindowTitle("计算机图形学大作业")
        self.setWindowIcon(QIcon('icon.jpg'))

    def setColor(self):
        palette1 = QPalette()
        palette1.setColor(self.backgroundRole(), QColor(192, 162, 199))
        self.setPalette(palette1)
        self.setAutoFillBackground(True)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def paintEvent(self, event):
        if self.pos:
            if self.pos.x() < HEIGHT and self.pos.x() > 0:
                self.setCursor(Qt.CrossCursor)
            else:
                self.setCursor(Qt.ArrowCursor)
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        self.drawText(event, qp)
        self.coordinate(qp)
        self.drawPoint(self.points)
        qp.end()

    def mousePressEvent(self, event):
        self.pos = event.pos()
        x, y = self.pos.x(), self.pos.y()
        if event.buttons() == Qt.LeftButton:
            if x > HEIGHT:
                if y > HEIGHT/5*4 and y < HEIGHT:
                    QApplication.instance().quit()
                elif y > HEIGHT/5*3 and y < HEIGHT/5*4:
                    self.get_mpe()
                elif y > HEIGHT/5*2 and y < HEIGHT/5*3:
                    self.get_mpc()
                elif y > HEIGHT/5*1 and y < HEIGHT/5*2:
                    self.get_bre()
                elif y > 0 and y < HEIGHT/5*1:
                    self.get_dda()

    def get_mpe(self):
        self.points = []
        r_x, ok = QInputDialog.getInt(
            self, '设置中点椭圆算法参数（请勿点击cancel）', '请输入x半轴长', 8)
        if ok:
            r_y, ok = QInputDialog.getInt(self, '设置中点椭圆算法参数', '请输入y半轴长', 6)
            if ok:
                x_c, ok = QInputDialog.getInt(
                    self, '设置中点椭圆算法参数', '请输入中心横坐标', 0)
                if ok:
                    y_c, ok = QInputDialog.getInt(
                        self, '设置中点椭圆算法参数', '请输入中心纵坐标', 0)
        self.points = mpe.mpe(r_x, r_y, x_c, y_c)

    def get_mpc(self):
        self.points = []
        r, ok = QInputDialog.getInt(self, '设置中点圆算法参数', '请输入半径', 10)
        if ok:
            x_c, ok = QInputDialog.getInt(
                self, '设置中点圆算法参数', '请输入中心横坐标', 0)
            if ok:
                y_c, ok = QInputDialog.getInt(
                    self, '设置中点圆算法参数', '请输入中心纵坐标', 0)
        self.points = mpc.mpc(r, x_c, y_c)

    def get_bre(self):
        self.points = []
        x_1, ok = QInputDialog.getInt(
            self, '设置Bresenham算法参数', '请输入端点一横坐标', 20)
        if ok:
            y_1, ok = QInputDialog.getInt(
                self, '设置Bresenham算法参数', '请输入端点一纵坐标', 10)
            if ok:
                x_2, ok = QInputDialog.getInt(
                    self, '设置Bresenham算法参数', '请输入端点二横坐标', 30)
                if ok:
                    y_2, ok = QInputDialog.getInt(
                        self, '设置Bresenham算法参数', '请输入端点二纵坐标', 18)
        self.points = bre.bresenham(x_1, y_1, x_2, y_2)

    def get_dda(self):
        self.points = []
        x_1, ok = QInputDialog.getInt(
            self, '设置DDA算法参数', '请输入端点一横坐标', 20)
        if ok:
            y_1, ok = QInputDialog.getInt(
                self, '设置DDA算法参数', '请输入端点一纵坐标', 10)
            if ok:
                x_2, ok = QInputDialog.getInt(
                    self, '设置DDA算法参数', '请输入端点二横坐标', 30)
                if ok:
                    y_2, ok = QInputDialog.getInt(
                        self, '设置DDA算法参数', '请输入端点二纵坐标', 18)
        self.points = dda.dda(x_1, y_1, x_2, y_2)

    def drawLines(self, qp):
        pen = QPen(Qt.black, 3, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(HEIGHT, 0, HEIGHT, HEIGHT)
        qp.drawLine(HEIGHT, HEIGHT/5*1, WIDTH, HEIGHT/5*1)
        qp.drawLine(HEIGHT, HEIGHT/5*2, WIDTH, HEIGHT/5*2)
        qp.drawLine(HEIGHT, HEIGHT/5*3, WIDTH, HEIGHT/5*3)
        qp.drawLine(HEIGHT, HEIGHT/5*4, WIDTH, HEIGHT/5*4)

        #pen = QPen(Qt.black, 1.5, Qt.SolidLine)
        # pen.setStyle(Qt.DashDotDotLine)
        # qp.setPen(pen)
        #qp.drawLine(HEIGHT, HEIGHT/10*9, WIDTH, HEIGHT/10*9)

    def drawText(self, event, qp):
        qp.setPen(QColor(0, 0, 0))
        qp.setFont(QFont('Bradley Hand ITC', 18))
        qp.drawText(QRect(HEIGHT, 0, WIDTH - HEIGHT, HEIGHT/10),
                    Qt.AlignCenter, self.text[0])
        qp.drawText(QRect(HEIGHT, HEIGHT/5*1, WIDTH - HEIGHT, HEIGHT/10),
                    Qt.AlignCenter, self.text[2])
        qp.drawText(QRect(HEIGHT, HEIGHT/5*2, WIDTH - HEIGHT, HEIGHT/10),
                    Qt.AlignCenter, self.text[4])
        qp.drawText(QRect(HEIGHT, HEIGHT/5*3, WIDTH - HEIGHT, HEIGHT/10),
                    Qt.AlignCenter, self.text[6])
        # qp.drawText(QRect(HEIGHT, HEIGHT/5*4, WIDTH - HEIGHT, HEIGHT/10),
        # Qt.AlignCenter, self.text[8])
        # qp.drawText(QRect(HEIGHT, HEIGHT/10*9, WIDTH - HEIGHT, HEIGHT/10),
        # Qt.AlignCenter, self.text[9])
        qp.drawText(QRect(HEIGHT, HEIGHT/5*4, WIDTH - HEIGHT, HEIGHT/5),
                    Qt.AlignCenter, self.text[9])

        qp.setFont(QFont('FangSong', 18))
        qp.drawText(QRect(HEIGHT, HEIGHT/10*1, WIDTH - HEIGHT, HEIGHT/10),
                    Qt.AlignCenter, self.text[1])
        qp.drawText(QRect(HEIGHT, HEIGHT/10*3, WIDTH - HEIGHT, HEIGHT/10),
                    Qt.AlignCenter, self.text[3])
        qp.drawText(QRect(HEIGHT, HEIGHT/10*5, WIDTH - HEIGHT, HEIGHT/10),
                    Qt.AlignCenter, self.text[5])
        qp.drawText(QRect(HEIGHT, HEIGHT/10*7, WIDTH - HEIGHT, HEIGHT/10),
                    Qt.AlignCenter, self.text[7])

    def coordinate(self, qp):
        pen = QPen(QColor(0, 0, 0, 100), 0.5, Qt.SolidLine)
        qp.setPen(pen)
        num = 100
        temp = HEIGHT/num
        for i in range(num):
            qp.drawLine(0, temp * (i + 1), HEIGHT, temp * (i + 1))
            qp.drawLine(temp * (i + 1), 0, temp * (i + 1), HEIGHT)

    def drawPoint(self, points: list):
        scale = HEIGHT/100
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(0, 0, 0))
        for i in points:
            qp.drawRect(i[0] * scale + self.x_c, HEIGHT - i[1] *
                        scale - self.y_c, scale, scale)
        qp.end()

    def mouseMoveEvent(self, event):
        self.pos = event.pos()
        self.update()


def run_gui():
    app = QApplication(sys.argv)
    run = gui()
    sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    run = gui()
    sys.exit(app.exec_())
