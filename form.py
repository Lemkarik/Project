from PyQt5 import QtCore, QtGui, QtWidgets


class FormWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 360)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.get_q_text = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.get_q_text.setFont(font)
        self.get_q_text.setObjectName("get_q_text")
        self.verticalLayout.addWidget(self.get_q_text)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.get_corr_ans = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.get_corr_ans.setFont(font)
        self.get_corr_ans.setObjectName("get_corr_ans")
        self.verticalLayout.addWidget(self.get_corr_ans)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.get_incorr_ans_1 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.get_incorr_ans_1.setFont(font)
        self.get_incorr_ans_1.setObjectName("get_incorr_ans_1")
        self.verticalLayout.addWidget(self.get_incorr_ans_1)
        self.get_incorr_ans_2 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.get_incorr_ans_2.setFont(font)
        self.get_incorr_ans_2.setObjectName("get_incorr_ans_2")
        self.verticalLayout.addWidget(self.get_incorr_ans_2)
        self.get_incorr_ans_3 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.get_incorr_ans_3.setFont(font)
        self.get_incorr_ans_3.setObjectName("get_incorr_ans_3")
        self.verticalLayout.addWidget(self.get_incorr_ans_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.status_bar = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.status_bar.setFont(font)
        self.status_bar.setText("")
        self.status_bar.setObjectName("status_bar")
        self.verticalLayout.addWidget(self.status_bar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pb_form_exit = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pb_form_exit.setFont(font)
        self.pb_form_exit.setObjectName("pb_form_exit")
        self.horizontalLayout.addWidget(self.pb_form_exit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pb_form_add_question = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pb_form_add_question.setFont(font)
        self.pb_form_add_question.setObjectName("pb_form_add_question")
        self.horizontalLayout.addWidget(self.pb_form_add_question)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Добавить вопрос"))
        self.label.setText(_translate("MainWindow", "Текст вопроса:"))
        self.label_2.setText(_translate("MainWindow", "Правильный ответ:"))
        self.label_3.setText(_translate("MainWindow", "Неправильные ответы:"))
        self.pb_form_exit.setText(_translate("MainWindow", "Отмена"))
        self.pb_form_add_question.setText(_translate("MainWindow", "Добавить"))
