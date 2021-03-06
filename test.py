from PyQt5 import QtCore, QtGui, QtWidgets


class TestWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.q_text_display = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.q_text_display.setFont(font)
        self.q_text_display.setText("")
        self.q_text_display.setAlignment(QtCore.Qt.AlignCenter)
        self.q_text_display.setObjectName("q_text_display")
        self.verticalLayout_3.addWidget(self.q_text_display)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pb_ans1 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_ans1.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pb_ans1.setFont(font)
        self.pb_ans1.setText("")
        self.pb_ans1.setObjectName("pb_ans1")
        self.verticalLayout.addWidget(self.pb_ans1)
        self.pb_ans2 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_ans2.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pb_ans2.setFont(font)
        self.pb_ans2.setText("")
        self.pb_ans2.setObjectName("pb_ans2")
        self.verticalLayout.addWidget(self.pb_ans2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pb_ans3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_ans3.sizePolicy().hasHeightForWidth())
        self.pb_ans3.setSizePolicy(sizePolicy)
        self.pb_ans3.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pb_ans3.setFont(font)
        self.pb_ans3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pb_ans3.setText("")
        self.pb_ans3.setAutoDefault(False)
        self.pb_ans3.setDefault(False)
        self.pb_ans3.setFlat(False)
        self.pb_ans3.setObjectName("pb_ans3")
        self.verticalLayout_2.addWidget(self.pb_ans3)
        self.pb_ans4 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_ans4.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pb_ans4.setFont(font)
        self.pb_ans4.setText("")
        self.pb_ans4.setObjectName("pb_ans4")
        self.verticalLayout_2.addWidget(self.pb_ans4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pb_test_exit = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pb_test_exit.setFont(font)
        self.pb_test_exit.setObjectName("pb_test_exit")
        self.horizontalLayout_2.addWidget(self.pb_test_exit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pb_complete = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pb_complete.setFont(font)
        self.pb_complete.setObjectName("pb_complete")
        self.horizontalLayout_2.addWidget(self.pb_complete)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Тест"))
        self.pb_test_exit.setText(_translate("MainWindow", "Выход"))
        self.pb_complete.setText(_translate("MainWindow", "Завершить"))
