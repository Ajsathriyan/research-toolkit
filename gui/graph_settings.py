# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 00:10:26 2026

@author: AJITH
"""

from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QComboBox,
    QSpinBox,
    QPushButton
)


class GraphSettings(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Graph Settings")

        layout = QVBoxLayout()

        # Color
        layout.addWidget(QLabel("Color"))
        self.color = QComboBox()
        self.color.addItems([
            "blue",
            "red",
            "green",
            "black",
            "orange",
            "purple"
        ])
        layout.addWidget(self.color)

        # Marker
        layout.addWidget(QLabel("Marker"))

        self.marker = QComboBox()
        self.marker.addItems([
            "o",
            "s",
            "^",
            "D",
            "x",
            "+"
        ])
        layout.addWidget(self.marker)

        # Size
        layout.addWidget(QLabel("Marker Size"))

        self.size = QSpinBox()
        self.size.setRange(2,20)
        self.size.setValue(8)

        layout.addWidget(self.size)

        ok = QPushButton("OK")
        ok.clicked.connect(self.accept)

        layout.addWidget(ok)

        self.setLayout(layout)