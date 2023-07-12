import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Create a QWebEngineView instance
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))

        # Create the navigation bar
        navigation_bar = QToolBar("Navigation")
        self.addToolBar(navigation_bar)

        # Add the forward button to the navigation bar
        forward_button = QAction("Forward", self)
        # forward_button.setIcon(QIcon("forward.png"))
        forward_button.triggered.connect(self.browser.forward)
        navigation_bar.addAction(forward_button)

        # Add the backward button to the navigation bar
        backward_button = QAction("Back", self)
        # backward_button.setIcon(QIcon("back.png"))
        backward_button.triggered.connect(self.browser.back)
        navigation_bar.addAction(backward_button)

        # Add the refresh button to the navigation bar
        refresh_button = QAction("Refresh", self)
        # refresh_button.setIcon(QIcon("refresh.png"))
        refresh_button.triggered.connect(self.browser.reload)
        navigation_bar.addAction(refresh_button)
        
        

        # # Add the address bar to the navigation bar
        # self.address_bar = QLineEdit()
        # self.address_bar.returnPressed.connect(self.load_url)
        # navigation_bar.addWidget(self.address_bar)

        # Add the search bar to the navigation bar
        self.search_bar = QLineEdit()
        self.search_bar.returnPressed.connect(self.search)
        navigation_bar.addWidget(self.search_bar)
        
        

        # Set the main window's central widget to be the browser
        self.setCentralWidget(self.browser)

        # Show the main window
        self.showMaximized()

    def load_url(self):
        url = self.address_bar.text()
        self.browser.setUrl(QUrl(url))
        

    def search(self):
        search_term = self.search_bar.text()
        url = "https://www.google.com/search?q=" + search_term
        self.browser.setUrl(QUrl(url))


app = QApplication(sys.argv)
QApplication.setApplicationName("RPBrowser")
window = MainWindow()
app.exec_()
