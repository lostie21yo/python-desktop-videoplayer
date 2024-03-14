# Form implementation generated from reading ui file 'ui\analize_window.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(400, 600))
        Form.setBaseSize(QtCore.QSize(400, 400))
        Form.setStyleSheet("background-color: #242424;")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.analizeCentralWidget = QtWidgets.QWidget(parent=Form)
        self.analizeCentralWidget.setStyleSheet("color: white;\n"
"font-size: 12px")
        self.analizeCentralWidget.setObjectName("analizeCentralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.analizeCentralWidget)
        self.verticalLayout.setContentsMargins(-1, 6, -1, -1)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalFrame = QtWidgets.QFrame(parent=self.analizeCentralWidget)
        self.horizontalFrame.setMinimumSize(QtCore.QSize(0, 60))
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label = QtWidgets.QLabel(parent=self.horizontalFrame)
        self.label.setMinimumSize(QtCore.QSize(0, 40))
        self.label.setBaseSize(QtCore.QSize(0, 40))
        self.label.setStyleSheet("font-size: 20px;\n"
"font: bold;")
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.areaNameLabel = QtWidgets.QLabel(parent=self.horizontalFrame)
        self.areaNameLabel.setStyleSheet("font-size: 20px;\n"
"font: bold;\n"
"color: green;")
        self.areaNameLabel.setObjectName("areaNameLabel")
        self.horizontalLayout_7.addWidget(self.areaNameLabel)
        self.verticalLayout.addWidget(self.horizontalFrame)
        self.horizontalFrame1 = QtWidgets.QFrame(parent=self.analizeCentralWidget)
        self.horizontalFrame1.setMinimumSize(QtCore.QSize(0, 60))
        self.horizontalFrame1.setObjectName("horizontalFrame1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalFrame1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.horizontalFrame1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.horizontalFrame1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.horizontalFrame1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.verticalLayout.addWidget(self.horizontalFrame1)
        self.horizontalFrame_2 = QtWidgets.QFrame(parent=self.analizeCentralWidget)
        self.horizontalFrame_2.setMinimumSize(QtCore.QSize(0, 60))
        self.horizontalFrame_2.setObjectName("horizontalFrame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(parent=self.horizontalFrame_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.objectComboBox = QtWidgets.QComboBox(parent=self.horizontalFrame_2)
        self.objectComboBox.setObjectName("objectComboBox")
        self.horizontalLayout_3.addWidget(self.objectComboBox)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout.addWidget(self.horizontalFrame_2)
        self.horizontalFrame_3 = QtWidgets.QFrame(parent=self.analizeCentralWidget)
        self.horizontalFrame_3.setMinimumSize(QtCore.QSize(0, 60))
        self.horizontalFrame_3.setObjectName("horizontalFrame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalFrame_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(parent=self.horizontalFrame_3)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.heightLineEdit = QtWidgets.QLineEdit(parent=self.horizontalFrame_3)
        self.heightLineEdit.setObjectName("heightLineEdit")
        self.horizontalLayout_4.addWidget(self.heightLineEdit)
        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 1)
        self.verticalLayout.addWidget(self.horizontalFrame_3)
        self.horizontalFrame_4 = QtWidgets.QFrame(parent=self.analizeCentralWidget)
        self.horizontalFrame_4.setMinimumSize(QtCore.QSize(0, 40))
        self.horizontalFrame_4.setObjectName("horizontalFrame_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalFrame_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(parent=self.horizontalFrame_4)
        self.label_4.setStyleSheet("font-size: 20px;\n"
"font: bold;")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.analizeButton = QtWidgets.QPushButton(parent=self.horizontalFrame_4)
        self.analizeButton.setObjectName("analizeButton")
        self.horizontalLayout_5.addWidget(self.analizeButton)
        self.verticalLayout.addWidget(self.horizontalFrame_4)
        self.verticalFrame = QtWidgets.QFrame(parent=self.analizeCentralWidget)
        self.verticalFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalFrame.setMaximumSize(QtCore.QSize(16777215, 70))
        self.verticalFrame.setBaseSize(QtCore.QSize(0, 70))
        self.verticalFrame.setStyleSheet("background-color: #323232;")
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(parent=self.verticalFrame)
        self.label_5.setStyleSheet("font-size: 20px;\n"
"font: bold;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(parent=self.verticalFrame)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.verticalLayout.addWidget(self.verticalFrame)
        self.gridFrame = QtWidgets.QFrame(parent=self.analizeCentralWidget)
        self.gridFrame.setStyleSheet("background-color: #323232;")
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(parent=self.gridFrame)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.gridFrame)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(parent=self.gridFrame)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(parent=self.gridFrame)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(parent=self.gridFrame)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 0, 1, 1)
        self.containerNameLabel = QtWidgets.QLabel(parent=self.gridFrame)
        self.containerNameLabel.setObjectName("containerNameLabel")
        self.gridLayout.addWidget(self.containerNameLabel, 0, 1, 1, 1)
        self.requiredLevelLabel = QtWidgets.QLabel(parent=self.gridFrame)
        self.requiredLevelLabel.setObjectName("requiredLevelLabel")
        self.gridLayout.addWidget(self.requiredLevelLabel, 1, 1, 1, 1)
        self.currentLevelLabel = QtWidgets.QLabel(parent=self.gridFrame)
        self.currentLevelLabel.setObjectName("currentLevelLabel")
        self.gridLayout.addWidget(self.currentLevelLabel, 2, 1, 1, 1)
        self.permissibleDeviationLabel = QtWidgets.QLabel(parent=self.gridFrame)
        self.permissibleDeviationLabel.setObjectName("permissibleDeviationLabel")
        self.gridLayout.addWidget(self.permissibleDeviationLabel, 3, 1, 1, 1)
        self.currentDeviationLabel = QtWidgets.QLabel(parent=self.gridFrame)
        self.currentDeviationLabel.setObjectName("currentDeviationLabel")
        self.gridLayout.addWidget(self.currentDeviationLabel, 4, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 1)
        self.verticalLayout.addWidget(self.gridFrame)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)
        self.horizontalLayout.addWidget(self.analizeCentralWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Анализ"))
        self.label.setText(_translate("Form", "Мониторинг уровня"))
        self.areaNameLabel.setText(_translate("Form", "..."))
        self.pushButton_2.setText(_translate("Form", "Подключить базу"))
        self.pushButton_3.setText(_translate("Form", "Посмотреть протокол"))
        self.pushButton_4.setText(_translate("Form", "Справка"))
        self.label_2.setText(_translate("Form", "Задайте объект интереса"))
        self.label_3.setText(_translate("Form", "Введите реальную высоту объекта интереса (см.)"))
        self.label_4.setText(_translate("Form", "Текущий отчет"))
        self.analizeButton.setText(_translate("Form", "Анализ"))
        self.label_5.setText(_translate("Form", "Сообщение системы"))
        self.label_6.setText(_translate("Form", "Уровень наполнения в норме"))
        self.label_8.setText(_translate("Form", "Требуемый уровень наполнения (см.)"))
        self.label_7.setText(_translate("Form", "Наименование ёмкости"))
        self.label_9.setText(_translate("Form", "Текущий уровень наполнения (см.)"))
        self.label_10.setText(_translate("Form", "Допустимое отклонение от нормы наполнения (см.)"))
        self.label_11.setText(_translate("Form", "Отклонение от нормы наполнения (см.)"))
        self.containerNameLabel.setText(_translate("Form", "-"))
        self.requiredLevelLabel.setText(_translate("Form", "-"))
        self.currentLevelLabel.setText(_translate("Form", "-"))
        self.permissibleDeviationLabel.setText(_translate("Form", "-"))
        self.currentDeviationLabel.setText(_translate("Form", "-"))
