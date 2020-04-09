# -*- coding: utf-8 -*-

from widgets import *

app = QApplication(sys.argv)

window = MainWindow()
window.show() # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
sys.exit(app.exec_())