# RPBrowser Documentation

## Introduction

RPBrowser is a simple web browser application built using the PyQt5 library. It provides basic web browsing functionality, including navigation to websites and searching on Google. This documentation aims to provide an overview of the code and its functionality.

## Prerequisites

Before running RPBrowser, you need to ensure that you have the following installed:
- Python (3.x)
- PyQt5 library

You can install PyQt5 using pip:

```bash
pip install PyQt5 PyQtWebEngine
```

## Code Structure

The RPBrowser code is organized into a single Python file. Here's a breakdown of the code structure:

### Importing Libraries

```python
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
```

- `sys`: The `sys` module is used to access command-line arguments and interact with the Python runtime environment.
- `PyQt5`: This library is the core of the application, providing the necessary components for creating the graphical user interface (GUI).
- `QtWebEngineWidgets`: This module provides the web browsing functionality for the application.

### `MainWindow` Class

The `MainWindow` class is the heart of the RPBrowser application. It is a subclass of `QMainWindow` and defines the main window's layout and functionality.

#### Constructor `__init__(self)`

The constructor initializes the main window and its components. Here's what it does:

1. Creates a `QWebEngineView` instance to display web content.
2. Sets the initial URL to "https://www.google.com".
3. Creates a navigation bar (`QToolBar`) and adds it to the main window.
4. Adds forward, backward, and refresh buttons to the navigation bar, each with associated actions to perform navigation and refreshing.
5. Creates a search bar (`QLineEdit`) and adds it to the navigation bar, allowing users to enter search queries.
6. Sets the central widget of the main window to be the web browser.
7. Maximizes and displays the main window.

#### `load_url(self)`

This method is called when the user presses Enter in the address bar (currently commented out). It extracts the URL from the address bar and loads it into the web browser.

#### `search(self)`

This method is called when the user presses Enter in the search bar. It extracts the search term, constructs a Google search URL, and loads it into the web browser.

### Initializing the Application

The code initializes the PyQt5 application, sets its name to "RPBrowser," and creates an instance of the `MainWindow` class. Finally, it starts the application event loop using `app.exec_()`.

## Usage

1. Run the RPBrowser application using Python.
2. The application will open with a web browser displaying Google's homepage.
3. Use the forward and backward buttons to navigate between pages.
4. Click the refresh button to reload the current page.
5. Enter a search query in the search bar and press Enter to perform a Google search.

## Conclusion

RPBrowser is a simple PyQt5-based web browser application that provides basic web navigation and searching capabilities. It can serve as a foundation for building more advanced web browsers or as a learning resource for PyQt5 development.
