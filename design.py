# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\design.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 385)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Main_frame = QtWidgets.QFrame(self.centralwidget)
        self.Main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Main_frame.setObjectName("Main_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Main_frame)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(9, -1, -1, 6)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_affiliation = QtWidgets.QLabel(self.Main_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_affiliation.setFont(font)
        self.label_affiliation.setObjectName("label_affiliation")
        self.verticalLayout_2.addWidget(self.label_affiliation)
        self.comboBox_affiliation = QtWidgets.QComboBox(self.Main_frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_affiliation.setFont(font)
        self.comboBox_affiliation.setObjectName("comboBox_affiliation")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\Army/Icons/Friendly.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_affiliation.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\Army/Icons/Enemy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_affiliation.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\Army/Icons/Neutral.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_affiliation.addItem(icon2, "")
        self.verticalLayout_2.addWidget(self.comboBox_affiliation)
        self.label_unit_modifier = QtWidgets.QLabel(self.Main_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_unit_modifier.setFont(font)
        self.label_unit_modifier.setObjectName("label_unit_modifier")
        self.verticalLayout_2.addWidget(self.label_unit_modifier)
        self.comboBox_unit_modifier = QtWidgets.QComboBox(self.Main_frame)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox_unit_modifier.setFont(font)
        self.comboBox_unit_modifier.setObjectName("comboBox_unit_modifier")
        self.comboBox_unit_modifier.addItem("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\Army/Icons/Light Infantry.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_unit_modifier.addItem(icon3, "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\Army/Icons/Infantry.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_unit_modifier.addItem(icon4, "")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(".\\Army/Icons/Motorized Infantry.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_unit_modifier.addItem(icon5, "")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(".\\Army/Icons/Mechanized Infantry.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_unit_modifier.addItem(icon6, "")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(".\\Army/Icons/Armor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_unit_modifier.addItem(icon7, "")
        self.comboBox_unit_modifier.addItem("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(".\\Army/Icons/Air Assault.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_unit_modifier.addItem(icon8, "")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(".\\Army/Icons/Airborne.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_unit_modifier.addItem(icon9, "")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(".\\Army/Icons/Naval Infantry.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_unit_modifier.addItem(icon10, "")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(".\\Army/Icons/Mountain Infantry.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_unit_modifier.addItem(icon11, "")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(".\\Army/Icons/Arctic Infantry.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_unit_modifier.addItem(icon12, "")
        self.comboBox_unit_modifier.addItem("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(".\\Army/Icons/Field Artillery.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_unit_modifier.addItem(icon13, "")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(".\\Army/Icons/Self-Propelled Artillery.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_unit_modifier.addItem(icon14, "")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(".\\Army/Icons/Rocket Artillery.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_unit_modifier.addItem(icon15, "")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(".\\Army/Icons/Tactical Missile Force.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_unit_modifier.addItem(icon16, "")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(".\\Army/Icons/Strategic Missile Force.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_unit_modifier.addItem(icon17, "")
        self.comboBox_unit_modifier.addItem("")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(".\\Army/Icons/Security Forces.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_unit_modifier.addItem(icon18, "")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(".\\Army/Icons/Police Forces.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_unit_modifier.addItem(icon19, "")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(".\\Army/Icons/Air-Defense.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_unit_modifier.addItem(icon20, "")
        self.verticalLayout_2.addWidget(self.comboBox_unit_modifier)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.label_battle_dimension = QtWidgets.QLabel(self.Main_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_battle_dimension.setFont(font)
        self.label_battle_dimension.setObjectName("label_battle_dimension")
        self.verticalLayout_3.addWidget(self.label_battle_dimension)
        self.comboBox_battle_dimension = QtWidgets.QComboBox(self.Main_frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_battle_dimension.setFont(font)
        self.comboBox_battle_dimension.setObjectName("comboBox_battle_dimension")
        self.comboBox_battle_dimension.addItem("")
        self.comboBox_battle_dimension.addItem("")
        self.comboBox_battle_dimension.addItem("")
        self.comboBox_battle_dimension.addItem("")
        self.comboBox_battle_dimension.addItem("")
        self.comboBox_battle_dimension.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_battle_dimension)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.Main_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.lineEdit_description = QtWidgets.QLineEdit(self.Main_frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_description.setFont(font)
        self.lineEdit_description.setObjectName("lineEdit_description")
        self.verticalLayout_3.addWidget(self.lineEdit_description)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.pushButton_Create = QtWidgets.QPushButton(self.Main_frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_Create.setFont(font)
        self.pushButton_Create.setObjectName("pushButton_Create")
        self.verticalLayout_7.addWidget(self.pushButton_Create)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.frame = QtWidgets.QFrame(self.Main_frame)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout.addWidget(self.frame)
        self.horizontalLayout.setStretch(1, 325)
        self.verticalLayout.addWidget(self.Main_frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_affiliation.setText(_translate("MainWindow", "Affiliation:"))
        self.comboBox_affiliation.setItemText(0, _translate("MainWindow", "Friendly"))
        self.comboBox_affiliation.setItemText(1, _translate("MainWindow", "Enemy"))
        self.comboBox_affiliation.setItemText(2, _translate("MainWindow", "Neutral"))
        self.label_unit_modifier.setText(_translate("MainWindow", "Unit modifier:"))
        self.comboBox_unit_modifier.setItemText(0, _translate("MainWindow", "---Main Units---"))
        self.comboBox_unit_modifier.setItemText(1, _translate("MainWindow", "Light Infantry"))
        self.comboBox_unit_modifier.setItemText(2, _translate("MainWindow", "Infantry"))
        self.comboBox_unit_modifier.setItemText(3, _translate("MainWindow", "Motorized Infantry"))
        self.comboBox_unit_modifier.setItemText(4, _translate("MainWindow", "Mechanized Infantry"))
        self.comboBox_unit_modifier.setItemText(5, _translate("MainWindow", "Armor"))
        self.comboBox_unit_modifier.setItemText(6, _translate("MainWindow", "---Elite Units---"))
        self.comboBox_unit_modifier.setItemText(7, _translate("MainWindow", "Air Assault"))
        self.comboBox_unit_modifier.setItemText(8, _translate("MainWindow", "Airborne"))
        self.comboBox_unit_modifier.setItemText(9, _translate("MainWindow", "Naval Infantry"))
        self.comboBox_unit_modifier.setItemText(10, _translate("MainWindow", "Mountain Infantry"))
        self.comboBox_unit_modifier.setItemText(11, _translate("MainWindow", "Arctic Infantry"))
        self.comboBox_unit_modifier.setItemText(12, _translate("MainWindow", "---Artillery Units---"))
        self.comboBox_unit_modifier.setItemText(13, _translate("MainWindow", "Field Artillery"))
        self.comboBox_unit_modifier.setItemText(14, _translate("MainWindow", "Self-Propelled Artillery"))
        self.comboBox_unit_modifier.setItemText(15, _translate("MainWindow", "Rocket Artillery"))
        self.comboBox_unit_modifier.setItemText(16, _translate("MainWindow", "Tactical Missile Force"))
        self.comboBox_unit_modifier.setItemText(17, _translate("MainWindow", "Strategic Missile Force"))
        self.comboBox_unit_modifier.setItemText(18, _translate("MainWindow", "---Others---"))
        self.comboBox_unit_modifier.setItemText(19, _translate("MainWindow", "Security Forces"))
        self.comboBox_unit_modifier.setItemText(20, _translate("MainWindow", "Police Forces"))
        self.comboBox_unit_modifier.setItemText(21, _translate("MainWindow", "Air-Defense"))
        self.label_battle_dimension.setText(_translate("MainWindow", "Battle dimension:"))
        self.comboBox_battle_dimension.setItemText(0, _translate("MainWindow", "Battalion (1,000)"))
        self.comboBox_battle_dimension.setItemText(1, _translate("MainWindow", "Regiment (1,500)"))
        self.comboBox_battle_dimension.setItemText(2, _translate("MainWindow", "Brigade (3,000)"))
        self.comboBox_battle_dimension.setItemText(3, _translate("MainWindow", "Division (12,000)"))
        self.comboBox_battle_dimension.setItemText(4, _translate("MainWindow", "Corps (36,000)"))
        self.comboBox_battle_dimension.setItemText(5, _translate("MainWindow", "Army (108,000)"))
        self.label.setText(_translate("MainWindow", "Country:"))
        self.pushButton_Create.setText(_translate("MainWindow", "Create"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
