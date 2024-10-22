import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QGroupBox, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel
from PySide2.QtGui import QFont
from PySide2 import QtGui, QtCore, QtWidgets
from shiboken2 import wrapInstance
from maya import cmds
import maya.OpenMayaUI as omui


def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QWidget)

class UT_UV_Manager(QMainWindow):
    
    window_title = "UT Renamer v2.0"
    
    def __init__(self, parent=None):
        super(UT_UV_Manager, self).__init__(parent)
        
        length = 470
        width = 300
        
        self.setWindowTitle(self.window_title)
        self.setFixedSize(width, length)
        self.setStyleSheet("background-color: rgb(33, 33, 33);")
        
        icon_path = "D:/DEV/Useful Tools PROJECTS/ICONS/RENAMER.png"
        self.setWindowIcon(QtGui.QIcon(icon_path))
        
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowCloseButtonHint)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        main_layout = QVBoxLayout(self.central_widget)
        
        #########################################################################################
        
        name_layout = QGroupBox()
        name_layout.setMaximumSize(width, 100) 
        name_layout.setStyleSheet("""
            QGroupBox {
                background-color: rgb(53, 53, 53);
                border: 2px solid rgb(10, 114, 114);
                border-radius: 5px;
                margin-top: 10px;
            }
        """)     
    
        font01 = QFont()
        font01.setPointSize(9)
        font02 = QFont()
        font02.setPointSize(7)
        font03 = QFont()
        font03.setPointSize(8)
        name_layout.setFont(font01)

        name_title = QLabel("Name")
        name_font = QFont()
        name_font.setPointSize(10)
        name_title.setFont(name_font)
        name_title.setStyleSheet("""
            QLabel {
                background-color: rgb(53, 53, 53);
                color: rgb(10, 114, 114);
                subcontrol-origin: margin;
                subcontrol-position: top center;
                font-weight: 550;
            }
        """)
        
        title_name_layout = QHBoxLayout()
        title_name_layout.addWidget(name_title, 0, QtCore.Qt.AlignCenter)
        
        content_name_layout = QHBoxLayout()
        content_name_layout.setContentsMargins(0, 0, 0, 0)
        
        self.name_line = QLineEdit()
        self.name_line.setPlaceholderText("Name") 
        self.name_line.setFixedSize(220, 30)
        self.name_line.setFont(font03)
        self.name_line.setStyleSheet("""
            QLineEdit {
                padding-left: 8px;
                font-style: italic;
            }
        """)
        
        self.name_btn = QPushButton("N")
        self.name_btn.setStyleSheet("""
            QPushButton {
                background-color: rgb(33, 33, 33);
                color: rgb(10, 114, 114);
                font-weight: 550;
            }
        """)
        self.name_btn.setFixedSize(34, 34)
        self.name_btn.setFont(font01)
        
        content_name_layout.addWidget(self.name_line)
        content_name_layout.addWidget(self.name_btn)
        
        vbox_name_layout = QVBoxLayout(name_layout)
        vbox_name_layout.addLayout(title_name_layout)
        vbox_name_layout.addLayout(content_name_layout)
        
        self.name_btn.clicked.connect(self.rename_Command)
        
        #########################################################################################
        
        prefix_layout = QGroupBox()
        prefix_layout.setMaximumSize(width, 140) 
        prefix_layout.setStyleSheet("""
            QGroupBox {
                background-color: rgb(53, 53, 53);
                border: 2px solid rgb(10, 114, 114);
                border-radius: 5px;
                margin-top: 10px;
            }
        """)
        
        prefix_title = QLabel("Prefix")
        prefix_font = QFont()
        prefix_font.setPointSize(10)
        prefix_title.setFont(prefix_font)
        prefix_title.setStyleSheet("""
            QLabel {
                background-color: rgb(53, 53, 53);
                color: rgb(10, 114, 114);
                subcontrol-origin: margin;
                subcontrol-position: top center;
                font-weight: 550;
            }
        """)
        
        self.radio_prefix_btn_1 = QtWidgets.QRadioButton("Input")
        self.radio_prefix_btn_1.setStyleSheet("""QRadioButton {
                background-color: rgb(53, 53, 53);
                color: rgb(10, 114, 114);
                margin-top: 5px;
                font-weight: 550;
            }
        """) 
        self.radio_prefix_btn_2 = QtWidgets.QRadioButton("C_")
        self.radio_prefix_btn_2.setStyleSheet("""QRadioButton {
                background-color: rgb(53, 53, 53);
                color: rgb(10, 114, 114);
                margin-top: 5px;
                font-weight: 550;
            }
        """) 
        self.radio_prefix_btn_3 = QtWidgets.QRadioButton("L_")
        self.radio_prefix_btn_3.setStyleSheet("""QRadioButton {
                background-color: rgb(53, 53, 53);
                color: rgb(10, 114, 114);
                margin-top: 5px;
                font-weight: 550;
            }
        """) 
        self.radio_prefix_btn_4 = QtWidgets.QRadioButton("R_")
        self.radio_prefix_btn_4.setStyleSheet("""QRadioButton {
                background-color: rgb(53, 53, 53);
                color: rgb(10, 114, 114);
                margin-top: 5px;
                font-weight: 550;
            }
        """) 
        
        
        self.radio_prefix_btn_1.setChecked(True)
        
        title_prefix_layout = QHBoxLayout()
        title_prefix_layout.addWidget(prefix_title, 0, QtCore.Qt.AlignCenter)
        
        radio_btns_prefix_layout = QHBoxLayout()
        radio_btns_prefix_layout.addWidget(self.radio_prefix_btn_1)
        radio_btns_prefix_layout.addWidget(self.radio_prefix_btn_2)
        radio_btns_prefix_layout.addWidget(self.radio_prefix_btn_3)
        radio_btns_prefix_layout.addWidget(self.radio_prefix_btn_4)
        
        content_prefix_layout = QHBoxLayout()
        content_prefix_layout.setContentsMargins(0, 0, 0, 0)
        
        self.prefix_line = QLineEdit()
        self.prefix_line.setPlaceholderText("Prefix")
        self.prefix_line.setFixedSize(220, 30)
        self.prefix_line.setFont(font03)
        self.prefix_line.setStyleSheet("""
            QLineEdit {
                padding-left: 8px;
                font-style: italic;
            }
        """)
        
        self.prefix_btn = QPushButton("P")
        self.prefix_btn.setStyleSheet("""
            QPushButton {
                background-color: rgb(33, 33, 33);
                color: rgb(10, 114, 114);
                font-weight: 550;
            }
        """)
        self.prefix_btn.setFixedSize(34, 34)
        self.prefix_btn.setFont(font01)
        
        content_prefix_layout.addWidget(self.prefix_line)
        content_prefix_layout.addWidget(self.prefix_btn)
        
        vbox_prefix_layout = QVBoxLayout(prefix_layout)
        vbox_prefix_layout.addLayout(title_prefix_layout)
        vbox_prefix_layout.addLayout(radio_btns_prefix_layout)
        vbox_prefix_layout.addLayout(content_prefix_layout)
        
        self.prefix_btn.clicked.connect(self.prefix_Command)
        
        #########################################################################################
        
        suffix_layout = QGroupBox()
        suffix_layout.setMaximumSize(width, 140) 
        suffix_layout.setStyleSheet("""
            QGroupBox {
                background-color: rgb(53, 53, 53);
                border: 2px solid rgb(10, 114, 114);
                border-radius: 5px;
                margin-top: 10px;
            }
        """)
        
        suffix_title = QLabel("Suffix")
        suffix_font = QFont()
        suffix_font.setPointSize(10)
        suffix_title.setFont(suffix_font)
        suffix_title.setStyleSheet("""
            QLabel {
                background-color: rgb(53, 53, 53);
                color: rgb(10, 114, 114);
                subcontrol-origin: margin;
                subcontrol-position: top center;
                font-weight: 550;
            }
        """)
        
        self.radio_suffix_btn_1 = QtWidgets.QRadioButton("Input")
        self.radio_suffix_btn_1.setStyleSheet("""QRadioButton {
                background-color: rgb(53, 53, 53);
                color: rgb(10, 114, 114);
                margin-top: 5px;
                font-weight: 550;
            }
        """) 
        self.radio_suffix_btn_2 = QtWidgets.QRadioButton("_GRP")
        self.radio_suffix_btn_2.setStyleSheet("""QRadioButton {
                background-color: rgb(53, 53, 53);
                color: rgb(10, 114, 114);
                margin-top: 5px;
                font-weight: 550;
            }
        """) 
        self.radio_suffix_btn_3 = QtWidgets.QRadioButton("_CON")
        self.radio_suffix_btn_3.setStyleSheet("""QRadioButton {
                background-color: rgb(53, 53, 53);
                color: rgb(10, 114, 114);
                margin-top: 5px;
                font-weight: 550;
            }
        """) 
        self.radio_suffix_btn_4 = QtWidgets.QRadioButton("_MSH")
        self.radio_suffix_btn_4.setStyleSheet("""QRadioButton {
                background-color: rgb(53, 53, 53);
                color: rgb(10, 114, 114);
                margin-top: 5px;
                font-weight: 550;
            }
        """) 
        
        
        self.radio_suffix_btn_1.setChecked(True)
        
        title_suffix_layout = QHBoxLayout()
        title_suffix_layout.addWidget(suffix_title, 0, QtCore.Qt.AlignCenter)
        
        radio_btns_suffix_layout = QHBoxLayout()
        radio_btns_suffix_layout.addWidget(self.radio_suffix_btn_1)
        radio_btns_suffix_layout.addWidget(self.radio_suffix_btn_2)
        radio_btns_suffix_layout.addWidget(self.radio_suffix_btn_3)
        radio_btns_suffix_layout.addWidget(self.radio_suffix_btn_4)
        
        content_suffix_layout = QHBoxLayout()
        content_suffix_layout.setContentsMargins(0, 0, 0, 0)
        
        self.suffix_line = QLineEdit()
        self.suffix_line.setPlaceholderText("Suffix")
        self.suffix_line.setFixedSize(220, 30)
        self.suffix_line.setFont(font03)
        self.suffix_line.setStyleSheet("""
            QLineEdit {
                padding-left: 8px;
                font-style: italic;
            }
        """)
        
        self.suffix_btn = QPushButton("S")
        self.suffix_btn.setStyleSheet("""
            QPushButton {
                background-color: rgb(33, 33, 33);
                color: rgb(10, 114, 114);
                font-weight: 550;
            }
        """)
        self.suffix_btn.setFixedSize(34, 34)
        self.suffix_btn.setFont(font01)
        
        content_suffix_layout.addWidget(self.suffix_line)
        content_suffix_layout.addWidget(self.suffix_btn)
        
        vbox_suffix_layout = QVBoxLayout(suffix_layout)
        vbox_suffix_layout.addLayout(title_suffix_layout)
        vbox_suffix_layout.addLayout(radio_btns_suffix_layout)
        vbox_suffix_layout.addLayout(content_suffix_layout)
        
        self.suffix_btn.clicked.connect(self.suffix_Command)
        
        #########################################################################################
        
        search_replace_layout = QGroupBox()
        search_replace_layout.setMaximumSize(width, 130) 
        search_replace_layout.setStyleSheet("""
            QGroupBox {
                background-color: rgb(53, 53, 53);
                border: 2px solid rgb(10, 114, 114);
                border-radius: 5px;
                margin-top: 10px;
            }
        """)     
    
        font01 = QFont()
        font01.setPointSize(9)
        font02 = QFont()
        font02.setPointSize(7)
        font03 = QFont()
        font03.setPointSize(8)
        search_replace_layout.setFont(font01)

        search_replace_title = QLabel("Search / Replace")
        search_replace_font = QFont()
        search_replace_font.setPointSize(10)
        search_replace_title.setFont(search_replace_font)
        search_replace_title.setStyleSheet("""
            QLabel {
                background-color: rgb(53, 53, 53);
                color: rgb(10, 114, 114);
                subcontrol-origin: margin;
                subcontrol-position: top center;
                font-weight: 550;
            }
        """)
        
        title_search_replace_layout = QHBoxLayout()
        title_search_replace_layout.addWidget(search_replace_title, 0, QtCore.Qt.AlignCenter)
        
        content_search_layout = QHBoxLayout()
        content_search_layout.setContentsMargins(0, 5, 0, 0)
        
        self.search_line = QLineEdit()
        self.search_line.setPlaceholderText("Search") 
        self.search_line.setFixedSize(260, 30)
        self.search_line.setFont(font03)
        self.search_line.setStyleSheet("""
            QLineEdit {
                padding-left: 8px;
                font-style: italic;
            }
        """)
        
        content_replace_layout = QHBoxLayout()
        content_replace_layout.setContentsMargins(0, 0, 0, 0)
        
        self.replace_line = QLineEdit()
        self.replace_line.setPlaceholderText("Replace") 
        self.replace_line.setFixedSize(220, 30)
        self.replace_line.setFont(font03)
        self.replace_line.setStyleSheet("""
            QLineEdit {
                padding-left: 8px;
                font-style: italic;
            }
        """)
        
        self.replace_btn = QPushButton("R")
        self.replace_btn.setStyleSheet("""
            QPushButton {
                background-color: rgb(33, 33, 33);
                color: rgb(10, 114, 114);
                font-weight: 550;
            }
        """)
        self.replace_btn.setFixedSize(34, 34)
        self.replace_btn.setFont(font01)
        
        content_search_layout.addWidget(self.search_line)
        
        content_replace_layout.addWidget(self.replace_line)
        content_replace_layout.addWidget(self.replace_btn)
        
        vbox_search_replace_layout = QVBoxLayout(search_replace_layout)
        vbox_search_replace_layout.addLayout(title_search_replace_layout)
        vbox_search_replace_layout.addLayout(content_search_layout)
        vbox_search_replace_layout.addLayout(content_replace_layout)
        
        self.replace_btn.clicked.connect(self.search_Replace_Command)
        
        #########################################################################################
        
        main_layout.setSpacing(1)
        main_layout.setContentsMargins(10, 5, 10, 5)
        
        main_layout.addWidget(name_layout)
        main_layout.addWidget(prefix_layout)
        main_layout.addWidget(suffix_layout)
        main_layout.addWidget(search_replace_layout)
        main_layout.addStretch()
        
    #########################################################################################
    
    def rename_Command(self, *args):
        
        self.selection = cmds.ls(sl=True)
        
        name_text = self.name_line.text()
        
        for s in self.selection:
            cmds.rename(s, name_text)
            
    #########################################################################################
        
    def prefix_Command(self, *args):
        
        self.selection = cmds.ls(sl=True)
        
        prefix_text = self.prefix_line.text()

        if self.radio_prefix_btn_1.isChecked():
            selected_prefix = prefix_text
        elif self.radio_prefix_btn_2.isChecked():
            selected_prefix = "C_"
        elif self.radio_prefix_btn_3.isChecked():
            selected_prefix = "L_"
        elif self.radio_prefix_btn_4.isChecked():
            selected_prefix = "R_"
        else:
            selected_prefix = ""

        for s in self.selection:
            
            new_name = s
            new_name = selected_prefix + new_name
            cmds.rename(s, new_name)
            
    #########################################################################################
    
    def suffix_Command(self, *args):
        
        self.selection = cmds.ls(sl=True)
        
        suffix_text = self.suffix_line.text()

        if self.radio_suffix_btn_1.isChecked():
            selected_suffix = suffix_text
        elif self.radio_suffix_btn_2.isChecked():
            selected_suffix = "_GRP"
        elif self.radio_suffix_btn_3.isChecked():
            selected_suffix = "_CON"
        elif self.radio_suffix_btn_4.isChecked():
            selected_suffix = "_MSH"
        else:
            selected_suffix = ""

        for s in self.selection:
            
            new_name = s
            new_name = new_name + selected_suffix
            cmds.rename(s, new_name)
            
    #########################################################################################
    
    def search_Replace_Command(self, args):

        self.selection = cmds.ls(sl=True)
        
        search_text = self.search_line.text()
        replace_text = self.replace_line.text()

        for s in cmds.ls(sl=True):
            if (s.find(search_text) != -1):
                if replace_text == '':
                    name = s.replace(search_text, '')
                else:
                    name = s.replace(search_text, replace_text)
                cmds.rename(s, name)
                
#########################################################################################     
      
app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)
    
        
if __name__ == "__main__":
    try:
        renamer_window.close()
        renamer_window.deleteLater()
    except:
        pass

renamer_window = UT_UV_Manager(parent=maya_main_window())
renamer_window.show()
