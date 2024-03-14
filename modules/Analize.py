from PyQt6.QtWidgets import (QWidget, QInputDialog, QHBoxLayout, QVBoxLayout, 
                             QGridLayout, QFileDialog,
                             QComboBox, QCheckBox, QPushButton, QFrame, QLabel, 
                             QLineEdit, QRadioButton)
from PyQt6.QtCore import QSize, Qt
from PyQt6 import uic
import os
from modules.messages import get_msg_result
from modules.AnalizeWindow import AnalizeWindow

class Analize(QWidget):
    """ Класс отвечающий за инициализацию и работу окна выбора модулей """
    def __init__(self, parent):
        super().__init__() 
        uic.loadUi('ui/analize_modules.ui', self)
        self.parent = parent
        self.move(self.parent.x()+740, self.parent.y()+75)
        self.btnAddModule.clicked.connect(self.addModule)
        self.btnModuleSelection.clicked.connect(self.selectModule)
        self.parent.openDataBaseButton.clicked.connect(self.parent.openDataBase)
        self.parent.heightSpinBox.valueChanged.connect(self.spinBoxChange)
        self.parent.analizeButton.clicked.connect(self.analizator)
        self.modules = dict()
        self.unitsPath = "./units/"
        self.loadPrevModules()
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)

    def spinBoxChange(self):
        self.parent.h = self.parent.heightSpinBox.value()
    
    def analizator(self):
        if self.parent.h is not None and self.parent.source is not None and not self.parent.isOriginal:
            h = self.parent.transformedImage.shape[0]
            w = self.parent.transformedImage.shape[1]
            print(w, h, 'cost: ', self.parent.h/h)
            print(self.parent.cutImage)

    def loadPrevModules(self):
        if os.path.exists(self.unitsPath):
            for dir in os.listdir(self.unitsPath):
                self.addModuleLine(dir)
        else:
            os.mkdir("units")

    def addModule(self):
        """ Добавление модуля """
        dialog = QInputDialog(self)
        dialog.setWindowTitle("HELLO!")
        dialog.setStyleSheet("* { color: white }")
        name, ok = dialog.getText(self, "Добавление модуля", "Введите название прикладного модуля:")
        if ok:
            os.mkdir(self.unitsPath+"/"+name)
            self.addModuleLine(name)
            
    def addModuleLine(self, name):
        moduleName = f'module-{name}'
        self.modules[moduleName] = QHBoxLayout()
        self.modules[moduleName].setObjectName(moduleName)
        self.moduleRadioButton = QRadioButton(parent=self.verticalLayoutWidget)
        self.moduleRadioButton.setObjectName(f"moduleRadioButton-{name}")
        self.moduleRadioButton.setText(name)
        self.modules[moduleName].addWidget(self.moduleRadioButton)
        self.comboBoxModules = QComboBox(parent=self.verticalLayoutWidget)
        self.comboBoxModules.setMaximumSize(QSize(80, 16777215))
        self.comboBoxModules.setObjectName(f"comboBox-{name}")
        self.comboBoxModules.addItem("на форме")
        self.comboBoxModules.addItem("в окне")
        self.modules[moduleName].addWidget(self.comboBoxModules)
        self.deleteModuleButton = QPushButton(parent=self.verticalLayoutWidget)
        self.deleteModuleButton.setMinimumSize(QSize(20, 20))
        self.deleteModuleButton.setMaximumSize(QSize(20, 20))
        self.deleteModuleButton.setObjectName(f"deleteModuleButton-{name}")
        self.deleteModuleButton.setText("-")
        self.deleteModuleButton.clicked.connect(lambda: self.deleteModule(name))
        self.modules[moduleName].addWidget(self.deleteModuleButton)
        self.verticalModulesListLayout.insertLayout(len(self.modules)-1, self.modules[moduleName])
    
    def deleteModule(self, name):
        """ Удаление модуля """
        moduleName = f'module-{name}'
        result = get_msg_result("Удаление","Удалить модуль?")
        if result:
            module = self.modules.pop(moduleName)
            module.setParent(None)
            self.deleteItemsOfLayout(module)
            os.rmdir(self.unitsPath+"/"+name)

    def deleteItemsOfLayout(self, layout):
        """ Удаление содержимого и самого Layout'а"""
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)
                else:
                    self.deleteItemsOfLayout(item.layout())
    
    def selectModule(self):
        for m in self.modules.keys():
            name = m.split('module-')[1]
            moduleRadioButtonName = f'moduleRadioButton-{name}'
            comboBoxName = f'comboBox-{name}'
            radioButton = self.findChild(QRadioButton, moduleRadioButtonName)
            if radioButton.isChecked():
                print(moduleRadioButtonName)
                comboBoxSelection = self.findChild(QComboBox, comboBoxName).currentIndex()
                if comboBoxSelection == 0:
                    self.openAnalizeFrame()
                    self.parent.areaNameLabel.setText(name)
                if comboBoxSelection == 1:
                    AnalizeWindow.openAnalizeWindow(self, name)
                    self.parent.frameAnalizing.hide()
        self.hideAnalizeSelectWindow()

    def openAnalizeFrame(self):
        self.parent.frameProcessing.hide()
        self.parent.frameAnalizing.show()

    def openAnalize(self):
        self.analize_choosing_window = Analize(self)

    def showAnalizeSelectWindow(self):
        self.analize_choosing_window.show()

    def hideAnalizeSelectWindow(self):
        self.hide()


            