"""
Author      : Mostafa Sayed Ahmed Taha
Description : python file contain variables that contain QSS for different themes (Maybe Replaced Later).
Date        : 11/27/2024
Future Work : Add More Themes.

General Notes:
    - Opt: Indicates areas for potential optimization.
    - adv/feature/: Denotes future improvements or features.
"""

# Morning Theme
morningStyle =   \
"""
        /* QWidget#centralwidget  to make it apply to background only*/
        QWidget {
            background-image: url("./GUI/images/Morning.png");
            background-position: center;
            background-repeat: no-repeat;
            background-size: cover; /* Makes the image scale to fill the window */
            background-color: #f5f5f5;  /* Light gray background */
            font-family: 'Roboto', sans-serif;  /* Clean modern font */
            font-size: 14px;
            color: #333333;  /* Dark text color */
        }
        
        .QPushButton
        {
        
        color: #333;
        border: 2px solid #555;
        border-radius: 50px;
        
        
        }
        
        QPushButton#checkStreak
        {
        background-color: darkblue;
        color:white;
        font-size: 12px;
        font-weight: bold;
        border: 5px solid white;
        }
        
        QPushButton#checkStreak:hover , QPushButton#checkStreak:focus
        {
        background-color: black;
        color: yellow;
        
        }
        QPushButton#checkStreak::pressed
        {
        background-color: red;
        color: yellow;
        
        }
        
        QPushButton#logIn
        {
        background-color: green;
        color:white;
        font-size: 16px;
        font-weight: bold;
        border: 5px solid white;
        
        }
        QPushButton#logIn:hover , QPushButton#logIn:focus
        {
        background-color: black;
        color: yellow;
        
        }
        QPushButton#logIn::pressed
        {
        background-color: red;
        color: yellow;
        }
        
        
        QLCDNumber
        {
        
            background-color: rgba(0, 0, 0, 1) ; /* Semi-transparent dark background */
            color: #ff4444; /* Bright red for numbers */
            font-size: 32px;
            font-weight: bold;
            border-radius: 12px;
            padding: 10px;
            text-align: center;
        
        }
        
        QListView
        {
        font-size:32px;
        background-color:darkblue;
        color:black;
        text-shadow:2px 2px 5px #FFF;
        font-weight:900;
        
        
        
        }
        
        QMainWindow
        {
        background-color: rgba(255, 255, 255);
        }
        
        QMenuBar
        {
        background-color: rgba(255, 255, 255);
        }
        
        QStatusBar
        {
        background-color: rgba(255, 255, 255);
        }
        
        QCalendarWidget {
            background-color: #ffffff;  /* White background */
            border: 1px solid #cccccc; /* Light gray border */
            border-radius: 8px;
            padding: 5px;
        }
        
        QCalendarWidget QAbstractItemView {
            selection-background-color: #4caf50; /* Green for selected dates */
            selection-color: #ffffff; /* White text for selected dates */
        }
        
        QCalendarWidget QToolButton {
            background-color: #4caf50; /* Green buttons */
            color: #ffffff; /* White text */
            border-radius: 6px;
            padding: 5px;
        }
        
        QCalendarWidget QToolButton:hover {
            background-color: #388e3c; /* Darker green on hover */
        }
        
        QComboBox {
            background-color: #ffffff; /* White background */
            color: #333333; /* Dark gray text */
            border: 1px solid #cccccc; /* Light gray border */
            border-radius: 6px;
            padding: 5px;
        }
        
        QComboBox::drop-down {
            border-left: 1px solid #cccccc;
            background-color:purple;
        }
        
        QComboBox QAbstractItemView {
            selection-background-color: #4caf50; /* Green selection */
            selection-color: #ffffff; /* White text for selected item */
        }
         """
# Night Theme
nightStyle = \
    """
        QWidget {
            background-image: url("./GUI/images/Night.png");
            background-position: center;
            background-repeat: no-repeat;
            background-size: cover; /* Makes the image scale to fill the window */
            background-color: #f5f5f5;  /* Light gray background */
            font-family: 'Roboto', sans-serif;  /* Clean modern font */
            font-size: 14px;
            color: #333333;  /* Dark text color */
        }
        
        .QPushButton
        {
        
        color: #333;
        border: 2px solid #555;
        border-radius: 50px;
        
        
        }
        
        QPushButton#checkStreak
        {
        background-color: darkblue;
        color:white;
        font-size: 12px;
        font-weight: bold;
        border: 5px solid white;
        }
        
        QPushButton#checkStreak:hover , QPushButton#checkStreak:focus
        {
        background-color: black;
        color: yellow;
        
        }
        QPushButton#checkStreak::pressed
        {
        background-color: red;
        color: yellow;
        
        }
        
        QPushButton#logIn
        {
        background-color: green;
        color:white;
        font-size: 16px;
        font-weight: bold;
        border: 5px solid white;
        
        }
        QPushButton#logIn:hover , QPushButton#logIn:focus
        {
        background-color: black;
        color: yellow;
        
        }
        QPushButton#logIn::pressed
        {
        background-color: red;
        color: yellow;
        }
        
        
        QLCDNumber
        {
        
            background-color: rgba(0, 0, 0, 1) ; /* Semi-transparent dark background */
            color: #ff4444; /* Bright red for numbers */
            font-size: 32px;
            font-weight: bold;
            border-radius: 12px;
            padding: 10px;
            text-align: center;
        
        }
        
        QListView
        {
        font-size:32px;
        background-color:darkblue;
        color:black;
        text-shadow:2px 2px 5px #FFF;
        font-weight:900;
        
        
        
        }
        
        QMainWindow
        {
        background-color: rgba(255, 255, 255);
        }
        
        QMenuBar
        {
        background-color: rgba(255, 255, 255);
        }
        
        QStatusBar
        {
        background-color: rgba(255, 255, 255);
        }
        
        QCalendarWidget {
            background-color: #ffffff;  /* White background */
            border: 1px solid #cccccc; /* Light gray border */
            border-radius: 8px;
            padding: 5px;
        }
        
        QCalendarWidget QAbstractItemView {
            selection-background-color: #4caf50; /* Green for selected dates */
            selection-color: #ffffff; /* White text for selected dates */
        }
        
        QCalendarWidget QToolButton {
            background-color: #4caf50; /* Green buttons */
            color: #ffffff; /* White text */
            border-radius: 6px;
            padding: 5px;
        }
        
        QCalendarWidget QToolButton:hover {
            background-color: #388e3c; /* Darker green on hover */
        }
        
        QComboBox {
            background-color: #ffffff; /* White background */
            color: #333333; /* Dark gray text */
            border: 1px solid #cccccc; /* Light gray border */
            border-radius: 6px;
            padding: 5px;
        }
        
        QComboBox::drop-down {
            border-left: 1px solid #cccccc;
            background-color:purple;
        }
        
        QComboBox QAbstractItemView {
            selection-background-color: #4caf50; /* Green selection */
            selection-color: #ffffff; /* White text for selected item */
        }
         """