
from PyQt5.QtWidgets import QApplication, QMainWindow
import Qt_GUI_Designer_Stock_UI,Qt_Designer_StockPrice,sys


if __name__ == '__main__':
###################################################初始化爬虫程序###########################################
    GUIstockPrice = Qt_Designer_StockPrice.stockPrice()
    def showNintendoPrice():
        ui1.label_4.setText('%s'%(GUIstockPrice.getNintendoStockPrice()))
    def showLGPrice():
        ui1.label_5.setText('%s'%(GUIstockPrice.getLGStockPrice1()))
    def showTencentPrice():
        ui1.label_6.setText('%s'%(GUIstockPrice.getTencentStockPrice()))
#############################################################################################################

 ##################################################初始化窗口界面#############################################
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui1 = Qt_GUI_Designer_Stock_UI.Ui_MainWindow()
    ui1.setupUi(MainWindow)
    ui1.pushButton.clicked.connect(showNintendoPrice)
    ui1.pushButton.clicked.connect(showLGPrice)
    ui1.pushButton.clicked.connect(showTencentPrice)##################    Button 链接代码需要放在show之前来加载执行,添加click事件#################


    MainWindow.show()
    sys.exit(app.exec_())
###########################收工################################################################################





