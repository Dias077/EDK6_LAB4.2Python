#!/usr/bin/env python3
# coding=utf-8

import re
import string
import sys
import random

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('main.ui', self)

        self.setWindowTitle('Работа со строками в Python')

        self.btn_solve.clicked.connect(self.solve)
        self.btn_solve_2.clicked.connect(self.solve_2)
        self.btn_clear.clicked.connect(self.clear)

    def solve(self):
        self.textEdit_words.clear()
        text = self.textEdit_text.toPlainText().split()

        itog = ""

        for word in text:
            for i in range(len(word)):
                if i % 2 == 0:
                    itog += word[i]
            itog += " "
        self.textEdit_words.insertPlainText(itog)

    def solve_2(self):
        self.textEdit_words_2.clear()
        text_2 = self.textEdit_text_2.toPlainText().split()

        itog_2 = ""
        alphabet_lower = [chr(ord("а") + i) for i in range(32)]

        for word in text_2:
            for i in range(len(word)):
                itog_2 += word[i]
                itog_2 += random.choice(alphabet_lower)
            itog_2 += " "
        self.textEdit_words_2.insertPlainText(itog_2)

    def clear(self):
        self.textEdit_text.clear()
        self.textEdit_words.clear()
        self.textEdit_text_2.clear()
        self.textEdit_words_2.clear()


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
