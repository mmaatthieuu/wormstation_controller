# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qontroller.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(2436, 1460)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.scrollArea = QtWidgets.QScrollArea(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 2112, 1365))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_6.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_6.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelDisplay = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.labelDisplay.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.labelDisplay.setText("")
        self.labelDisplay.setPixmap(QtGui.QPixmap("../../.designer/backup/blank.jpg"))
        self.labelDisplay.setScaledContents(False)
        self.labelDisplay.setObjectName("labelDisplay")
        self.gridLayout_2.addWidget(self.labelDisplay, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_6)
        self.frame = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame.setBaseSize(QtCore.QSize(300, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.frame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_9 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 278, 1345))
        self.scrollAreaWidgetContents_9.setMaximumSize(QtCore.QSize(278, 1364))
        self.scrollAreaWidgetContents_9.setObjectName("scrollAreaWidgetContents_9")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_9)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_6.addWidget(self.label_15, 6, 0, 1, 2)
        self.btnOriginalView = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        icon = QtGui.QIcon.fromTheme("zoom-draw")
        self.btnOriginalView.setIcon(icon)
        self.btnOriginalView.setObjectName("btnOriginalView")
        self.gridLayout_6.addWidget(self.btnOriginalView, 8, 1, 1, 1)
        self.btnRefresh = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        icon = QtGui.QIcon.fromTheme("view-refresh")
        self.btnRefresh.setIcon(icon)
        self.btnRefresh.setObjectName("btnRefresh")
        self.gridLayout_6.addWidget(self.btnRefresh, 7, 0, 1, 1)
        self.btnLiveView = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        icon = QtGui.QIcon.fromTheme("media-playback-start")
        self.btnLiveView.setIcon(icon)
        self.btnLiveView.setCheckable(True)
        self.btnLiveView.setObjectName("btnLiveView")
        self.gridLayout_6.addWidget(self.btnLiveView, 7, 1, 1, 1)
        self.LayoutSwitchBlue = QtWidgets.QHBoxLayout()
        self.LayoutSwitchBlue.setObjectName("LayoutSwitchBlue")
        self.label_28 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_28.setObjectName("label_28")
        self.LayoutSwitchBlue.addWidget(self.label_28)
        self.slider_switch_led_blue = QtWidgets.QSlider(self.scrollAreaWidgetContents_9)
        self.slider_switch_led_blue.setMaximum(1)
        self.slider_switch_led_blue.setPageStep(1)
        self.slider_switch_led_blue.setOrientation(QtCore.Qt.Horizontal)
        self.slider_switch_led_blue.setObjectName("slider_switch_led_blue")
        self.LayoutSwitchBlue.addWidget(self.slider_switch_led_blue)
        self.label_27 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_27.setObjectName("label_27")
        self.LayoutSwitchBlue.addWidget(self.label_27)
        self.gridLayout_6.addLayout(self.LayoutSwitchBlue, 2, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_26.setObjectName("label_26")
        self.gridLayout_6.addWidget(self.label_26, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_7.setObjectName("label_7")
        self.gridLayout_6.addWidget(self.label_7, 1, 0, 1, 1)
        self.LayoutSwitchIR = QtWidgets.QGridLayout()
        self.LayoutSwitchIR.setObjectName("LayoutSwitchIR")
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_18.setObjectName("label_18")
        self.LayoutSwitchIR.addWidget(self.label_18, 0, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_19.setObjectName("label_19")
        self.LayoutSwitchIR.addWidget(self.label_19, 0, 2, 1, 1)
        self.slider_switch_led = QtWidgets.QSlider(self.scrollAreaWidgetContents_9)
        self.slider_switch_led.setAutoFillBackground(False)
        self.slider_switch_led.setMaximum(1)
        self.slider_switch_led.setPageStep(1)
        self.slider_switch_led.setOrientation(QtCore.Qt.Horizontal)
        self.slider_switch_led.setInvertedAppearance(False)
        self.slider_switch_led.setObjectName("slider_switch_led")
        self.LayoutSwitchIR.addWidget(self.slider_switch_led, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.LayoutSwitchIR, 0, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_6.addWidget(self.label_17, 0, 0, 1, 1)
        self.btnFitView = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        icon = QtGui.QIcon.fromTheme("gtk-zoom-fit")
        self.btnFitView.setIcon(icon)
        self.btnFitView.setCheckable(True)
        self.btnFitView.setObjectName("btnFitView")
        self.gridLayout_6.addWidget(self.btnFitView, 8, 0, 1, 1)
        self.LayoutSwitchOrange = QtWidgets.QHBoxLayout()
        self.LayoutSwitchOrange.setObjectName("LayoutSwitchOrange")
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_12.setObjectName("label_12")
        self.LayoutSwitchOrange.addWidget(self.label_12)
        self.slider_switch_led_OG = QtWidgets.QSlider(self.scrollAreaWidgetContents_9)
        self.slider_switch_led_OG.setMaximum(1)
        self.slider_switch_led_OG.setPageStep(1)
        self.slider_switch_led_OG.setOrientation(QtCore.Qt.Horizontal)
        self.slider_switch_led_OG.setObjectName("slider_switch_led_OG")
        self.LayoutSwitchOrange.addWidget(self.slider_switch_led_OG)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_11.setObjectName("label_11")
        self.LayoutSwitchOrange.addWidget(self.label_11)
        self.gridLayout_6.addLayout(self.LayoutSwitchOrange, 1, 1, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_29.setObjectName("label_29")
        self.gridLayout_6.addWidget(self.label_29, 3, 0, 1, 1)
        self.comboCurrent = QtWidgets.QComboBox(self.scrollAreaWidgetContents_9)
        self.comboCurrent.setObjectName("comboCurrent")
        self.gridLayout_6.addWidget(self.comboCurrent, 3, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_6)
        self.sliderZoom = QtWidgets.QSlider(self.scrollAreaWidgetContents_9)
        self.sliderZoom.setMinimum(100)
        self.sliderZoom.setMaximum(500)
        self.sliderZoom.setSingleStep(1)
        self.sliderZoom.setOrientation(QtCore.Qt.Horizontal)
        self.sliderZoom.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.sliderZoom.setTickInterval(100)
        self.sliderZoom.setObjectName("sliderZoom")
        self.verticalLayout_2.addWidget(self.sliderZoom)
        spacerItem = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.spinShutterSpeed = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_9)
        self.spinShutterSpeed.setMaximum(1000000)
        self.spinShutterSpeed.setProperty("value", 50000)
        self.spinShutterSpeed.setObjectName("spinShutterSpeed")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinShutterSpeed)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.comboTimeoutUnit = QtWidgets.QComboBox(self.scrollAreaWidgetContents_9)
        self.comboTimeoutUnit.setObjectName("comboTimeoutUnit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboTimeoutUnit)
        self.labelTimeout = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.labelTimeout.setObjectName("labelTimeout")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelTimeout)
        self.spinTimeout = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_9)
        self.spinTimeout.setMaximum(1000000000)
        self.spinTimeout.setProperty("value", 0)
        self.spinTimeout.setObjectName("spinTimeout")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinTimeout)
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_22.setObjectName("label_22")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.spinBoxRecForS = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_9)
        self.spinBoxRecForS.setMaximum(999999)
        self.spinBoxRecForS.setObjectName("spinBoxRecForS")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBoxRecForS)
        self.label_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_23.setObjectName("label_23")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.spinBoxEveryH = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_9)
        self.spinBoxEveryH.setObjectName("spinBoxEveryH")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spinBoxEveryH)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.spinTimeInterval = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_9)
        self.spinTimeInterval.setEnabled(False)
        self.spinTimeInterval.setProperty("value", 2)
        self.spinTimeInterval.setObjectName("spinTimeInterval")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.spinTimeInterval)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.spinArchiveSize = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_9)
        self.spinArchiveSize.setMaximum(50000)
        self.spinArchiveSize.setProperty("value", 1800)
        self.spinArchiveSize.setObjectName("spinArchiveSize")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.spinArchiveSize)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.spinStartingFrame = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_9)
        self.spinStartingFrame.setEnabled(False)
        self.spinStartingFrame.setMaximum(1000000000)
        self.spinStartingFrame.setObjectName("spinStartingFrame")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.spinStartingFrame)
        self.label_64 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_64.setObjectName("label_64")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_64)
        self.spinIlluminationPulse = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_9)
        self.spinIlluminationPulse.setMaximum(2000)
        self.spinIlluminationPulse.setProperty("value", 500)
        self.spinIlluminationPulse.setObjectName("spinIlluminationPulse")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.spinIlluminationPulse)
        spacerItem1 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setItem(9, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(224, 27, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(224, 27, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.label_20.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.checkBoxOptogen = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_9)
        self.checkBoxOptogen.setText("")
        self.checkBoxOptogen.setChecked(False)
        self.checkBoxOptogen.setObjectName("checkBoxOptogen")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.checkBoxOptogen)
        self.label_25 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_25.setObjectName("label_25")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.comboOptoColor = QtWidgets.QComboBox(self.scrollAreaWidgetContents_9)
        self.comboOptoColor.setObjectName("comboOptoColor")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.comboOptoColor)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.spinPulseDuration = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_9)
        self.spinPulseDuration.setMaximum(120)
        self.spinPulseDuration.setProperty("value", 30)
        self.spinPulseDuration.setObjectName("spinPulseDuration")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.spinPulseDuration)
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_21.setObjectName("label_21")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.spinPulseInterval = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_9)
        self.spinPulseInterval.setMaximum(999999999)
        self.spinPulseInterval.setProperty("value", 3600)
        self.spinPulseInterval.setObjectName("spinPulseInterval")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.spinPulseInterval)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setItem(14, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        self.label_24 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_24.setObjectName("label_24")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.checkBoxComputeChemotax = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_9)
        self.checkBoxComputeChemotax.setText("")
        self.checkBoxComputeChemotax.setChecked(False)
        self.checkBoxComputeChemotax.setObjectName("checkBoxComputeChemotax")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.checkBoxComputeChemotax)
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.checkBoxLog = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_9)
        self.checkBoxLog.setText("")
        self.checkBoxLog.setChecked(True)
        self.checkBoxLog.setObjectName("checkBoxLog")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.checkBoxLog)
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.spinBoxVerbosity = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_9)
        self.spinBoxVerbosity.setObjectName("spinBoxVerbosity")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.spinBoxVerbosity)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_timeRecord = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_timeRecord.setText("")
        self.label_timeRecord.setObjectName("label_timeRecord")
        self.gridLayout_10.addWidget(self.label_timeRecord, 5, 0, 1, 1)
        self.label_frame = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_frame.setText("")
        self.label_frame.setObjectName("label_frame")
        self.gridLayout_10.addWidget(self.label_frame, 5, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_10.addItem(spacerItem3, 0, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout_10.addWidget(self.label_16, 1, 0, 1, 1)
        self.btnRecord = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        icon = QtGui.QIcon.fromTheme("camera-on")
        self.btnRecord.setIcon(icon)
        self.btnRecord.setObjectName("btnRecord")
        self.gridLayout_10.addWidget(self.btnRecord, 4, 0, 1, 1)
        self.btnStopRecord = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        icon = QtGui.QIcon.fromTheme("media-playback-stop")
        self.btnStopRecord.setIcon(icon)
        self.btnStopRecord.setObjectName("btnStopRecord")
        self.gridLayout_10.addWidget(self.btnStopRecord, 4, 1, 1, 1)
        self.textRecordName = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textRecordName.sizePolicy().hasHeightForWidth())
        self.textRecordName.setSizePolicy(sizePolicy)
        self.textRecordName.setMaximumSize(QtCore.QSize(16777215, 25))
        self.textRecordName.setInputMethodHints(QtCore.Qt.ImhLatinOnly)
        self.textRecordName.setFrameShape(QtWidgets.QFrame.HLine)
        self.textRecordName.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textRecordName.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textRecordName.setAcceptRichText(False)
        self.textRecordName.setObjectName("textRecordName")
        self.gridLayout_10.addWidget(self.textRecordName, 2, 0, 1, 2)
        self.verticalLayout_2.addLayout(self.gridLayout_10)
        self.btnDestDir = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.btnDestDir.setObjectName("btnDestDir")
        self.verticalLayout_2.addWidget(self.btnDestDir)
        spacerItem4 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem4)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.listBoxDevices = QtWidgets.QListWidget(self.scrollAreaWidgetContents_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listBoxDevices.sizePolicy().hasHeightForWidth())
        self.listBoxDevices.setSizePolicy(sizePolicy)
        self.listBoxDevices.setObjectName("listBoxDevices")
        self.verticalLayout_2.addWidget(self.listBoxDevices)
        self.btnRescanDevices = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.btnRescanDevices.setObjectName("btnRescanDevices")
        self.verticalLayout_2.addWidget(self.btnRescanDevices)
        self.btnCheckUpdates = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.btnCheckUpdates.setObjectName("btnCheckUpdates")
        self.verticalLayout_2.addWidget(self.btnCheckUpdates)
        self.btnUpdateAll = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.btnUpdateAll.setObjectName("btnUpdateAll")
        self.verticalLayout_2.addWidget(self.btnUpdateAll)
        self.btnClearTmpFolder = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.btnClearTmpFolder.setObjectName("btnClearTmpFolder")
        self.verticalLayout_2.addWidget(self.btnClearTmpFolder)
        self.btnSelfDiagnosis = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.btnSelfDiagnosis.setObjectName("btnSelfDiagnosis")
        self.verticalLayout_2.addWidget(self.btnSelfDiagnosis)
        self.btnRunInstall = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.btnRunInstall.setObjectName("btnRunInstall")
        self.verticalLayout_2.addWidget(self.btnRunInstall)
        self.btnReboot = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        icon = QtGui.QIcon.fromTheme("system-reboot")
        self.btnReboot.setIcon(icon)
        self.btnReboot.setObjectName("btnReboot")
        self.verticalLayout_2.addWidget(self.btnReboot)
        self.btnShutdown = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        icon = QtGui.QIcon.fromTheme("system-shutdown")
        self.btnShutdown.setIcon(icon)
        self.btnShutdown.setObjectName("btnShutdown")
        self.verticalLayout_2.addWidget(self.btnShutdown)
        self.gridLayout_9.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_9)
        self.verticalLayout_3.addWidget(self.scrollArea_2)
        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)
        self.label_help = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_help.sizePolicy().hasHeightForWidth())
        self.label_help.setSizePolicy(sizePolicy)
        self.label_help.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_help.setObjectName("label_help")
        self.gridLayout.addWidget(self.label_help, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2436, 22))
        self.menubar.setObjectName("menubar")
        self.menutype_here = QtWidgets.QMenu(self.menubar)
        self.menutype_here.setObjectName("menutype_here")
        self.menumenu = QtWidgets.QMenu(self.menutype_here)
        self.menumenu.setObjectName("menumenu")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionin_menu = QtWidgets.QAction(MainWindow)
        self.actionin_menu.setObjectName("actionin_menu")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionMosaic = QtWidgets.QAction(MainWindow)
        self.actionMosaic.setObjectName("actionMosaic")
        self.menumenu.addAction(self.actionin_menu)
        self.menutype_here.addAction(self.menumenu.menuAction())
        self.menutype_here.addAction(self.actionOpen)
        self.menutype_here.addAction(self.actionSave)
        self.menuView.addAction(self.actionMosaic)
        self.menubar.addAction(self.menutype_here.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Qontroller"))
        self.label_15.setText(_translate("MainWindow", "View"))
        self.btnOriginalView.setText(_translate("MainWindow", "Reset"))
        self.btnRefresh.setText(_translate("MainWindow", "Refresh"))
        self.btnLiveView.setText(_translate("MainWindow", "Live"))
        self.label_28.setText(_translate("MainWindow", "OFF"))
        self.label_27.setText(_translate("MainWindow", "ON"))
        self.label_26.setText(_translate("MainWindow", "Blue LED"))
        self.label_7.setText(_translate("MainWindow", "Orange LED"))
        self.label_18.setText(_translate("MainWindow", "OFF"))
        self.label_19.setText(_translate("MainWindow", "ON"))
        self.label_17.setText(_translate("MainWindow", "IR LED"))
        self.btnFitView.setText(_translate("MainWindow", "Adjust"))
        self.label_12.setText(_translate("MainWindow", "OFF"))
        self.label_11.setText(_translate("MainWindow", "ON"))
        self.label_29.setText(_translate("MainWindow", "Current [mA]"))
        self.label.setText(_translate("MainWindow", "Parameters"))
        self.label_4.setText(_translate("MainWindow", "Shutter Speed (µs)"))
        self.label_10.setText(_translate("MainWindow", "Timeout Unit"))
        self.labelTimeout.setText(_translate("MainWindow", "Timeout"))
        self.label_22.setText(_translate("MainWindow", "Record for (s)"))
        self.label_23.setText(_translate("MainWindow", "Every (h)"))
        self.label_8.setText(_translate("MainWindow", "Time Interval (s)"))
        self.label_9.setText(_translate("MainWindow", "Archives Size"))
        self.label_6.setText(_translate("MainWindow", "Starting Frame"))
        self.label_64.setText(_translate("MainWindow", "Illumination dur."))
        self.label_20.setText(_translate("MainWindow", "Optogenetic"))
        self.label_25.setText(_translate("MainWindow", "Color"))
        self.label_3.setText(_translate("MainWindow", "Pulse  duration (s)"))
        self.label_21.setText(_translate("MainWindow", "Interval (s)"))
        self.label_24.setText(_translate("MainWindow", "Auto  Analysis"))
        self.label_14.setText(_translate("MainWindow", "Log output"))
        self.label_13.setText(_translate("MainWindow", "Verbosity"))
        self.label_16.setText(_translate("MainWindow", "Record"))
        self.btnRecord.setText(_translate("MainWindow", "Start"))
        self.btnStopRecord.setText(_translate("MainWindow", "Stop"))
        self.btnDestDir.setText(_translate("MainWindow", "Open Dest. Dir"))
        self.label_2.setText(_translate("MainWindow", "Devices"))
        self.btnRescanDevices.setText(_translate("MainWindow", "Rescan Devices"))
        self.btnCheckUpdates.setText(_translate("MainWindow", "Check for updates"))
        self.btnUpdateAll.setText(_translate("MainWindow", "Update All"))
        self.btnClearTmpFolder.setText(_translate("MainWindow", "Clear Tmp Folder"))
        self.btnSelfDiagnosis.setText(_translate("MainWindow", "Run Self-Diagnosis"))
        self.btnRunInstall.setText(_translate("MainWindow", "Run Install Script"))
        self.btnReboot.setText(_translate("MainWindow", "Reboot"))
        self.btnShutdown.setText(_translate("MainWindow", "Shutdown All"))
        self.label_help.setText(_translate("MainWindow", "Help: Hover any item to display help"))
        self.menutype_here.setTitle(_translate("MainWindow", "File"))
        self.menumenu.setTitle(_translate("MainWindow", "New recording"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionin_menu.setText(_translate("MainWindow", "in menu"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionMosaic.setText(_translate("MainWindow", "Mosaic"))
