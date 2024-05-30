################################################################################
## Form generated from reading UI file 'designer.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 700)
        MainWindow.setMinimumSize(QSize(400, 700))
        icon = QIcon()
        icon.addFile(u":/icons/icons/calc.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color: #474747;\n"
"	font-family: Rubik;\n"
"	font-size: 16pt;\n"
"	font-weight: 600;\n"
"}\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	font-size: 28pt;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #5c5a5a;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #888;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result = QLabel(self.centralwidget)
        self.result.setObjectName(u"result")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result.sizePolicy().hasHeightForWidth())
        self.result.setSizePolicy(sizePolicy)
        self.result.setStyleSheet(u"color: #acacac;")
        self.result.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.result)

        self.entry = QLineEdit(self.centralwidget)
        self.entry.setObjectName(u"entry")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.entry.sizePolicy().hasHeightForWidth())
        self.entry.setSizePolicy(sizePolicy1)
        self.entry.setStyleSheet(u"font-size: 50pt;\n"
"border: none;")
        self.entry.setMaxLength(16)
        self.entry.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.entry.setReadOnly(True)

        self.verticalLayout.addWidget(self.entry)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn1 = QPushButton(self.centralwidget)
        self.btn1.setObjectName(u"btn1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn1.sizePolicy().hasHeightForWidth())
        self.btn1.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btn1, 10, 0, 1, 1)

        self.btnsub = QPushButton(self.centralwidget)
        self.btnsub.setObjectName(u"btnsub")
        sizePolicy2.setHeightForWidth(self.btnsub.sizePolicy().hasHeightForWidth())
        self.btnsub.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btnsub, 9, 3, 1, 1)

        self.btn9 = QPushButton(self.centralwidget)
        self.btn9.setObjectName(u"btn9")
        sizePolicy2.setHeightForWidth(self.btn9.sizePolicy().hasHeightForWidth())
        self.btn9.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btn9, 8, 2, 1, 1)

        self.btnadd = QPushButton(self.centralwidget)
        self.btnadd.setObjectName(u"btnadd")
        sizePolicy2.setHeightForWidth(self.btnadd.sizePolicy().hasHeightForWidth())
        self.btnadd.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btnadd, 10, 3, 1, 1)

        self.btn2 = QPushButton(self.centralwidget)
        self.btn2.setObjectName(u"btn2")
        sizePolicy2.setHeightForWidth(self.btn2.sizePolicy().hasHeightForWidth())
        self.btn2.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btn2, 10, 1, 1, 1)

        self.btn8 = QPushButton(self.centralwidget)
        self.btn8.setObjectName(u"btn8")
        sizePolicy2.setHeightForWidth(self.btn8.sizePolicy().hasHeightForWidth())
        self.btn8.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btn8, 8, 1, 1, 1)

        self.btn4 = QPushButton(self.centralwidget)
        self.btn4.setObjectName(u"btn4")
        sizePolicy2.setHeightForWidth(self.btn4.sizePolicy().hasHeightForWidth())
        self.btn4.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btn4, 9, 0, 1, 1)

        self.btn6 = QPushButton(self.centralwidget)
        self.btn6.setObjectName(u"btn6")
        sizePolicy2.setHeightForWidth(self.btn6.sizePolicy().hasHeightForWidth())
        self.btn6.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btn6, 9, 2, 1, 1)

        self.btn7 = QPushButton(self.centralwidget)
        self.btn7.setObjectName(u"btn7")
        sizePolicy2.setHeightForWidth(self.btn7.sizePolicy().hasHeightForWidth())
        self.btn7.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btn7, 8, 0, 1, 1)

        self.btnmult = QPushButton(self.centralwidget)
        self.btnmult.setObjectName(u"btnmult")
        sizePolicy2.setHeightForWidth(self.btnmult.sizePolicy().hasHeightForWidth())
        self.btnmult.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btnmult, 8, 3, 1, 1)

        self.btn5 = QPushButton(self.centralwidget)
        self.btn5.setObjectName(u"btn5")
        sizePolicy2.setHeightForWidth(self.btn5.sizePolicy().hasHeightForWidth())
        self.btn5.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btn5, 9, 1, 1, 1)

        self.btn0 = QPushButton(self.centralwidget)
        self.btn0.setObjectName(u"btn0")
        sizePolicy2.setHeightForWidth(self.btn0.sizePolicy().hasHeightForWidth())
        self.btn0.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btn0, 11, 1, 1, 1)

        self.btncalc = QPushButton(self.centralwidget)
        self.btncalc.setObjectName(u"btncalc")
        sizePolicy2.setHeightForWidth(self.btncalc.sizePolicy().hasHeightForWidth())
        self.btncalc.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btncalc, 11, 3, 1, 1)

        self.btnneg = QPushButton(self.centralwidget)
        self.btnneg.setObjectName(u"btnneg")
        sizePolicy2.setHeightForWidth(self.btnneg.sizePolicy().hasHeightForWidth())
        self.btnneg.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btnneg, 11, 0, 1, 1)

        self.btn3 = QPushButton(self.centralwidget)
        self.btn3.setObjectName(u"btn3")
        sizePolicy2.setHeightForWidth(self.btn3.sizePolicy().hasHeightForWidth())
        self.btn3.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btn3, 10, 2, 1, 1)

        self.btnpoint = QPushButton(self.centralwidget)
        self.btnpoint.setObjectName(u"btnpoint")
        sizePolicy2.setHeightForWidth(self.btnpoint.sizePolicy().hasHeightForWidth())
        self.btnpoint.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btnpoint, 11, 2, 1, 1)

        self.btnback = QPushButton(self.centralwidget)
        self.btnback.setObjectName(u"btnback")
        sizePolicy2.setHeightForWidth(self.btnback.sizePolicy().hasHeightForWidth())
        self.btnback.setSizePolicy(sizePolicy2)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/backspace.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnback.setIcon(icon1)
        self.btnback.setIconSize(QSize(48, 48))

        self.gridLayout.addWidget(self.btnback, 2, 2, 1, 1)

        self.btnce = QPushButton(self.centralwidget)
        self.btnce.setObjectName(u"btnce")
        sizePolicy2.setHeightForWidth(self.btnce.sizePolicy().hasHeightForWidth())
        self.btnce.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btnce, 2, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_2, 6, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy2.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_3, 6, 2, 1, 1)

        self.btndiv = QPushButton(self.centralwidget)
        self.btndiv.setObjectName(u"btndiv")
        sizePolicy2.setHeightForWidth(self.btndiv.sizePolicy().hasHeightForWidth())
        self.btndiv.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btndiv, 6, 3, 1, 1)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy2.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_4, 2, 3, 1, 1)

        self.btnclear = QPushButton(self.centralwidget)
        self.btnclear.setObjectName(u"btnclear")
        sizePolicy2.setHeightForWidth(self.btnclear.sizePolicy().hasHeightForWidth())
        self.btnclear.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btnclear, 2, 0, 1, 1)

        self.btnexp = QPushButton(self.centralwidget)
        self.btnexp.setObjectName(u"btnexp")
        sizePolicy2.setHeightForWidth(self.btnexp.sizePolicy().hasHeightForWidth())
        self.btnexp.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btnexp, 6, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u043a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440", None))
        self.result.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.entry.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.btn1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.btnsub.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.btnsub.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.btn9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.btn9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.btnadd.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.btnadd.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.btn2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.btn2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.btn8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.btn8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.btn4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.btn4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.btn6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.btn6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.btn7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.btn7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.btnmult.setText(QCoreApplication.translate("MainWindow", u"x", None))
#if QT_CONFIG(shortcut)
        self.btnmult.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.btn5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.btn5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.btn0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.btn0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.btncalc.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)
        self.btncalc.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.btnneg.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.btn3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.btn3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.btnpoint.setText(QCoreApplication.translate("MainWindow", u",", None))
#if QT_CONFIG(shortcut)
        self.btnpoint.setShortcut(QCoreApplication.translate("MainWindow", u",", None))
#endif // QT_CONFIG(shortcut)
        self.btnback.setText("")
#if QT_CONFIG(shortcut)
        self.btnback.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.btnce.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u221ax", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"1/x", None))
        self.btndiv.setText(QCoreApplication.translate("MainWindow", u"/", None))
#if QT_CONFIG(shortcut)
        self.btndiv.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"x^y", None))
#if QT_CONFIG(shortcut)

#endif // QT_CONFIG(shortcut)
        self.btnclear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.btnexp.setText(QCoreApplication.translate("MainWindow", u"x\u00b2", None))
    # retranslateUi

