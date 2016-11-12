import sys
from PyQt4 import QtGui  # , QtCore
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class UI(QtGui.QWidget):

    def __init__(self):
        super(UI, self).__init__()
        self.initUI()
        self.drawFigure()

    def initUI(self):
        # window setting
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('Window title')

        # figure setting
        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)
        self.axes = self.fig.add_subplot(111)
        layoutFigure = QtGui.QGridLayout()
        layoutFigure.addWidget(self.canvas, 0, 0)

        self.setLayout(layoutFigure)

    def drawFigure(self):
        x = range(100)
        y = range(100)
        self.axes.plot(x, y)
        self.canvas.draw()


def main():
    app = QtGui.QApplication(sys.argv)
    ui = UI()
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
