# -*- coding: utf-8 -*-
import sys, os
from pathlib import Path
resource_file_path = Path(os.getcwd()).joinpath(Path("./UI/Resources"))
sys.path.append(str(resource_file_path))

################################################################################
## Form generated from reading UI file 'AIMoveWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(329, 298)
        self.horizontalLayout = QHBoxLayout(Frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.AIMoveFrame = QGroupBox(Frame)
        self.AIMoveFrame.setObjectName(u"AIMoveFrame")
        self.AIMoveFrame.setEnabled(False)
        self.verticalLayout_5 = QVBoxLayout(self.AIMoveFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.AITypeBox = QGroupBox(self.AIMoveFrame)
        self.AITypeBox.setObjectName(u"AITypeBox")
        self.AITypeBox.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_4 = QHBoxLayout(self.AITypeBox)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.IterationsCheckBox = QCheckBox(self.AITypeBox)
        self.IterationsCheckBox.setObjectName(u"IterationsCheckBox")
        self.IterationsCheckBox.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IterationsCheckBox.sizePolicy().hasHeightForWidth())
        self.IterationsCheckBox.setSizePolicy(sizePolicy)
        self.IterationsCheckBox.setChecked(True)

        self.horizontalLayout_4.addWidget(self.IterationsCheckBox)

        self.TimeCheckBox = QCheckBox(self.AITypeBox)
        self.TimeCheckBox.setObjectName(u"TimeCheckBox")

        self.horizontalLayout_4.addWidget(self.TimeCheckBox)


        self.verticalLayout_5.addWidget(self.AITypeBox)

        self.LimitsFrame = QFrame(self.AIMoveFrame)
        self.LimitsFrame.setObjectName(u"LimitsFrame")
        self.LimitsFrame.setFrameShape(QFrame.StyledPanel)
        self.LimitsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.LimitsFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.L_LimitButton = QPushButton(self.LimitsFrame)
        self.L_LimitButton.setObjectName(u"L_LimitButton")

        self.horizontalLayout_5.addWidget(self.L_LimitButton)

        self.M_LimitButton = QPushButton(self.LimitsFrame)
        self.M_LimitButton.setObjectName(u"M_LimitButton")

        self.horizontalLayout_5.addWidget(self.M_LimitButton)

        self.H_LimitButton = QPushButton(self.LimitsFrame)
        self.H_LimitButton.setObjectName(u"H_LimitButton")

        self.horizontalLayout_5.addWidget(self.H_LimitButton)


        self.verticalLayout_5.addWidget(self.LimitsFrame)

        self.ManualEntryFrame = QFrame(self.AIMoveFrame)
        self.ManualEntryFrame.setObjectName(u"ManualEntryFrame")
        self.ManualEntryFrame.setFrameShape(QFrame.StyledPanel)
        self.ManualEntryFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.ManualEntryFrame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.LimitsLabel = QLabel(self.ManualEntryFrame)
        self.LimitsLabel.setObjectName(u"LimitsLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LimitsLabel.sizePolicy().hasHeightForWidth())
        self.LimitsLabel.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.LimitsLabel)

        self.AILimitsEdit = QLineEdit(self.ManualEntryFrame)
        self.AILimitsEdit.setObjectName(u"AILimitsEdit")
        sizePolicy.setHeightForWidth(self.AILimitsEdit.sizePolicy().hasHeightForWidth())
        self.AILimitsEdit.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.AILimitsEdit)


        self.verticalLayout_5.addWidget(self.ManualEntryFrame)

        self.AIBuildTreeButton = QPushButton(self.AIMoveFrame)
        self.AIBuildTreeButton.setObjectName(u"AIBuildTreeButton")

        self.verticalLayout_5.addWidget(self.AIBuildTreeButton)

        self.AIDisplayTreeButton = QPushButton(self.AIMoveFrame)
        self.AIDisplayTreeButton.setObjectName(u"AIDisplayTreeButton")

        self.verticalLayout_5.addWidget(self.AIDisplayTreeButton)

        self.AIMoveButton = QPushButton(self.AIMoveFrame)
        self.AIMoveButton.setObjectName(u"AIMoveButton")

        self.verticalLayout_5.addWidget(self.AIMoveButton)


        self.horizontalLayout.addWidget(self.AIMoveFrame)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.AIMoveFrame.setTitle(QCoreApplication.translate("Frame", u"AI Move Options", None))
        self.AITypeBox.setTitle(QCoreApplication.translate("Frame", u"Thinking Type", None))
        self.IterationsCheckBox.setText(QCoreApplication.translate("Frame", u"Iterations", None))
        self.TimeCheckBox.setText(QCoreApplication.translate("Frame", u"Time", None))
        self.L_LimitButton.setText(QCoreApplication.translate("Frame", u"1 Iteration", None))
        self.M_LimitButton.setText(QCoreApplication.translate("Frame", u"10 Iterations", None))
        self.H_LimitButton.setText(QCoreApplication.translate("Frame", u"100 Iterations", None))
        self.LimitsLabel.setText(QCoreApplication.translate("Frame", u"Enter the required limits: ", None))
        self.AILimitsEdit.setText("")
        self.AIBuildTreeButton.setText(QCoreApplication.translate("Frame", u"Build MCTS Tree", None))
        self.AIDisplayTreeButton.setText(QCoreApplication.translate("Frame", u"Display MCTS Tree", None))
        self.AIMoveButton.setText(QCoreApplication.translate("Frame", u"Make AI based Move", None))
    # retranslateUi

